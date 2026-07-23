import sys

import rclpy
from action_msgs.msg import GoalStatus
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle
from rclpy.node import Node
from rclpy.task import Future

from user_interface.action import Fibonacci
from user_interface.action._fibonacci import Fibonacci_GetResult_Response


class ActionClientNode(Node):
    def __init__(self, cancel_after: float | None = None):
        super().__init__("action_client")

        self.action_client = ActionClient(
            self,
            Fibonacci,
            "fibonacci_server",
        )

        # 몇 초 후 취소할 것인지 저장
        self.cancel_after = cancel_after

        self.goal_handle: ClientGoalHandle | None = None
        self.cancel_timer = None

    def send_goal(self, step: int):
        goal_msg = Fibonacci.Goal()
        goal_msg.step = step

        while not self.action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info(
                "fibonacci server를 기다리는 중입니다."
            )

        self.get_logger().info(
            f"Goal 전송 | step={step}"
        )

        send_goal_future = self.action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback,
        )

        send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future: Future):
        self.goal_handle = future.result()

        if self.goal_handle is None:
            self.get_logger().error(
                "Goal 응답을 받지 못했습니다."
            )
            return

        if not self.goal_handle.accepted:
            self.get_logger().warning(
                "Goal이 거절되었습니다."
            )
            return

        goal_id = bytes(
            self.goal_handle.goal_id.uuid
        ).hex()[:8]

        self.get_logger().info(
            f"[Goal:{goal_id}] Goal이 승인되었습니다."
        )

        # 서버의 최종 결과를 기다림
        result_future = self.goal_handle.get_result_async()
        result_future.add_done_callback(
            self.get_result_callback
        )

        # 취소 시간이 지정되었다면 타이머 생성
        if self.cancel_after is not None:
            self.get_logger().info(
                f"[Goal:{goal_id}] "
                f"{self.cancel_after}초 후 취소를 요청합니다."
            )

            self.cancel_timer = self.create_timer(
                self.cancel_after,
                self.cancel_goal,
            )

    def cancel_goal(self):
        # ROS 타이머는 반복 실행되므로 먼저 취소
        if self.cancel_timer is not None:
            self.cancel_timer.cancel()
            self.destroy_timer(self.cancel_timer)
            self.cancel_timer = None

        if self.goal_handle is None:
            self.get_logger().warning(
                "취소할 Goal이 없습니다."
            )
            return

        goal_id = bytes(
            self.goal_handle.goal_id.uuid
        ).hex()[:8]

        self.get_logger().info(
            f"[Goal:{goal_id}] 취소 요청 전송"
        )

        cancel_future = self.goal_handle.cancel_goal_async()
        cancel_future.add_done_callback(
            self.cancel_response_callback
        )

    def cancel_response_callback(self, future: Future):
        cancel_response = future.result()

        if cancel_response is None:
            self.get_logger().error(
                "취소 응답을 받지 못했습니다."
            )
            return

        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info(
                "서버가 취소 요청을 승인했습니다."
            )
        else:
            self.get_logger().warning(
                "서버가 취소 요청을 승인하지 않았습니다."
            )

    def feedback_callback(self, feedback_msg):
        sequence = list(
            feedback_msg.feedback.temp_seq
        )

        self.get_logger().info(
            f"feedback: {sequence}"
        )

    def get_result_callback(self, future: Future):
        response: Fibonacci_GetResult_Response = future.result()

        status = response.status
        sequence = list(response.result.seq)

        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(
                f"Goal 성공 | result={sequence}"
            )

        elif status == GoalStatus.STATUS_CANCELED:
            self.get_logger().info(
                f"Goal 취소 완료 | result={sequence}"
            )

        elif status == GoalStatus.STATUS_ABORTED:
            self.get_logger().error(
                f"Goal 중단 | result={sequence}"
            )

        else:
            self.get_logger().warning(
                f"Goal 종료 | status={status} | "
                f"result={sequence}"
            )

        # 결과를 받은 뒤 spin을 종료
        rclpy.shutdown()

    def destroy_node(self):
        self.action_client.destroy()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) not in (2, 3):
        print(
            "사용법: "
            "ros2 run ros_basic action_client "
            "[step: int] [cancel_after: float]"
        )
        print(
            "예시: ros2 run ros_basic action_client 10 3"
        )

        rclpy.shutdown()
        return

    try:
        step = int(sys.argv[1])

        cancel_after = None

        if len(sys.argv) == 3:
            cancel_after = float(sys.argv[2])

            if cancel_after <= 0:
                raise ValueError(
                    "취소 시간은 0보다 커야 합니다."
                )

    except ValueError as error:
        print(f"잘못된 입력입니다: {error}")
        rclpy.shutdown()
        return

    node = ActionClientNode(
        cancel_after=cancel_after
    )

    node.send_goal(step)

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.get_logger().info(
            "키보드 인터럽트"
        )

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()