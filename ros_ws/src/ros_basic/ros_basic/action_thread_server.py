import time

import rclpy
from action_msgs.msg import GoalStatus
from rclpy.action import ActionServer, CancelResponse
from rclpy.action.server import ServerGoalHandle
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

from user_interface.action import Fibonacci


class ActionThreadServer(Node):
    def __init__(self):
        super().__init__("action_thread_server")

        self.callback_group = ReentrantCallbackGroup()

        self.action_server = ActionServer(
            self,
            Fibonacci,
            "fibonacci_server",
            execute_callback=self.execute_callback,
            cancel_callback=self.cancel_callback,
            callback_group=self.callback_group,
        )

    def execute_callback(
        self,
        goal_handle: ServerGoalHandle,
    ) -> Fibonacci.Result:
        # Goal을 구분하기 위한 UUID
        goal_id = bytes(goal_handle.goal_id.uuid).hex()
        short_goal_id = goal_id[:8]

        step = goal_handle.request.step

        self.get_logger().info(
            f"[Goal:{short_goal_id}] 실행 시작 | "
            f"step={step} | status={goal_handle.status}"
        )

        if goal_handle.status == GoalStatus.STATUS_EXECUTING:
            self.get_logger().info(
                f"[Goal:{short_goal_id}] 현재 실행 중입니다."
            )

        feedback_msg = Fibonacci.Feedback()
        feedback_msg.temp_seq = [0, 1]

        result = Fibonacci.Result()

        for i in range(1, step):
            # 클라이언트가 취소 요청을 보냈는지 확인
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()

                result.seq = feedback_msg.temp_seq

                self.get_logger().info(
                    f"[Goal:{short_goal_id}] 취소 완료 | "
                    f"status={goal_handle.status} | "
                    f"result={list(result.seq)}"
                )

                return result

            next_number = (
                feedback_msg.temp_seq[i]
                + feedback_msg.temp_seq[i - 1]
            )
            feedback_msg.temp_seq.append(next_number)

            goal_handle.publish_feedback(feedback_msg)

            self.get_logger().info(
                f"[Goal:{short_goal_id}] "
                f"step={step} | 진행 인덱스={i} | "
                f"feedback={list(feedback_msg.temp_seq)}"
            )

            time.sleep(1.0)

            # step이 20을 초과하면 20까지만 수행한 뒤 중단
            if i >= 19 and step > 20:
                result.seq = feedback_msg.temp_seq

                self.get_logger().error(
                    f"[Goal:{short_goal_id}] "
                    f"step 요청값이 20을 초과하여 중단합니다. "
                    f"요청값={step}, 수행값=20"
                )

                goal_handle.abort()
                return result

        goal_handle.succeed()
        result.seq = feedback_msg.temp_seq

        self.get_logger().info(
            f"[Goal:{short_goal_id}] 실행 성공 | "
            f"status={goal_handle.status} | "
            f"result={list(result.seq)}"
        )

        return result

    def cancel_callback(
        self,
        goal_handle: ServerGoalHandle,
    ) -> CancelResponse:
        goal_id = bytes(goal_handle.goal_id.uuid).hex()[:8]

        self.get_logger().info(
            f"[Goal:{goal_id}] 취소 요청을 승인합니다."
        )

        return CancelResponse.ACCEPT

    def destroy_node(self):
        self.action_server.destroy()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = ActionThreadServer()

    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)

    try:
        executor.spin()

    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")

    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()