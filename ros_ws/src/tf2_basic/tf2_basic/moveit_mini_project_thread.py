# 중복된 코드를 함수화 해서 적용하기 - Object 추가
# srdf 수정해서 custom pose 추가 해서 운용 configuration 에 문자로 작동하게
# 벽을 여러개 추가해서 로봇팔이 벽 사이를 이동하게 작성 360도 주위를 다 활용
# Attached 코드는 .. 하지 않아도 됨 할사람은 구현해도 됨.
# srdf 파일은 data 폴더안에 복사해 놓았음

"""MoveItPy 미니 프로젝트: 원형 바닥과 방사형 벽 사이로 로봇팔 이동."""

import math
import os
import sys

import rclpy
from geometry_msgs.msg import Pose
from moveit.planning import MoveItPy
from moveit_msgs.msg import CollisionObject
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from shape_msgs.msg import SolidPrimitive
from std_srvs.srv import Empty


class MoveItMiniProjectNode(Node):
    """SRDF named pose와 Planning Scene을 이용하는 미니 프로젝트 노드."""

    # OMPL은 샘플링 기반 planner이므로 같은 목표도 결과가 달라질 수 있다.
    # 한 번 실패했다고 바로 포기하지 않고 지정 횟수만큼 다시 계획한다.
    MAX_PLANNING_ATTEMPTS = 3

    # SRDF에 정의한 pose 이름이다.
    # 벽은 0, 60, 120 ... 도에 있고, pose는 벽 사이의 중앙을 향한다.
    SECTOR_POSES = (
        "sector_030",
        "sector_090",
        "sector_150",
        "sector_210",
        "sector_270",
        "sector_330",
    )

    def __init__(self):
        """MoveIt과 Planning Scene을 초기화하고 미니 프로젝트를 실행한다."""
        super().__init__("moveit_mini_project")
        self.moveit = MoveItPy(node_name="moveit_mini_project_moveit_py")
        self.arm = self.moveit.get_planning_component("arm")
        self.planning_scene_monitor = self.moveit.get_planning_scene_monitor()

        # 먼저 충돌 환경을 구성한 뒤 경로 계획을 시작한다.
        table_added = self.add_cylinder_table()
        walls_added = self.add_radial_walls()
        self.print_collision_objects()
        self.scene_ready = table_added and walls_added
        if not self.scene_ready:
            self.get_logger().error(
                "충돌 환경 구성이 완료되지 않아 로봇 이동을 시작하지 않습니다."
            )

        # 서비스 요청은 한 번에 하나씩 실행한다.
        self.service_group = MutuallyExclusiveCallbackGroup()

        # 서비스 동작 중에도 timer callback을 처리한다.
        self.timer_group = MutuallyExclusiveCallbackGroup()

        self.service = self.create_service(
            Empty,
            "move_mini_project",
            self.move_service_callback,
            callback_group=self.service_group,
        )
        self.timer = self.create_timer(
            1.0,
            self.timer_callback,
            callback_group=self.timer_group,
        )
        self.get_logger().info(
            "서비스 준비 완료: "
            "ros2 service call /move_mini_project std_srvs/srv/Empty '{}'"
        )

    def timer_callback(self) -> None:
        """서비스 실행 중에도 executor가 동작하는지 확인한다."""
        self.get_logger().info("moveit mini project node running")

    def move_service_callback(self, request, response):
        """서비스가 호출되면 벽 사이 이동을 한 번 실행한다."""
        self.get_logger().info("Move mini project service started")

        if not self.scene_ready:
            self.get_logger().error("Planning Scene 준비 실패로 이동할 수 없습니다.")
            return response

        try:
            self.move_between_walls()
            self.get_logger().info("Move mini project service completed")
        except Exception as error:
            self.get_logger().error(
                f"Move mini project service failed: {error}"
            )

        return response

    def add_collision_object(
        self,
        object_id: str,
        primitive_type: int,
        dimensions: list[float],
        position: tuple[float, float, float],
        yaw: float = 0.0,
    ) -> bool:
        """BOX와 CYLINDER에 공통으로 사용하는 CollisionObject 추가 함수."""
        collision_object = CollisionObject()
        collision_object.header.frame_id = "world"
        collision_object.header.stamp = self.get_clock().now().to_msg()
        collision_object.id = object_id

        primitive = SolidPrimitive()
        primitive.type = primitive_type
        primitive.dimensions = dimensions

        object_pose = Pose()
        object_pose.position.x = position[0]
        object_pose.position.y = position[1]
        object_pose.position.z = position[2]

        # 벽의 z축 회전각(yaw)을 quaternion으로 변환한다.
        object_pose.orientation.z = math.sin(yaw / 2.0)
        object_pose.orientation.w = math.cos(yaw / 2.0)

        collision_object.primitives.append(primitive)  # type: ignore
        collision_object.primitive_poses.append(object_pose)  # type: ignore
        collision_object.operation = CollisionObject.ADD

        success = self.planning_scene_monitor.process_collision_object(
            collision_object
        )
        if success:
            self.get_logger().info(f"CollisionObject 추가: {object_id}")
        else:
            self.get_logger().error(f"CollisionObject 추가 실패: {object_id}")
        return success

    def add_cylinder_table(self) -> bool:
        """로봇 아래의 바닥 table을 원통으로 추가한다."""
        table_height = 0.05
        table_radius = 0.50

        # CYLINDER dimensions 순서는 [높이, 반지름]이다.
        # 윗면이 world의 z=0에 오도록 중심을 -높이/2에 배치한다.
        return self.add_collision_object(
            object_id="cylinder_table",
            primitive_type=SolidPrimitive.CYLINDER,
            dimensions=[table_height, table_radius],
            position=(0.0, 0.0, -table_height),
        )

    def add_radial_walls(self) -> bool:
        """로봇 주위에 60도 간격으로 방사형 벽 6개를 추가한다."""
        wall_count = 6
        wall_length = 0.28
        wall_thickness = 0.015
        wall_height = 0.15
        wall_inner_radius = 0.17
        wall_center_radius = wall_inner_radius + wall_length / 2.0
        all_success = True

        for index in range(wall_count):
            wall_angle = math.radians(index * 60.0)

            # BOX의 긴 x축이 로봇 중심에서 바깥쪽을 향하도록 배치한다.
            wall_x = wall_center_radius * math.cos(wall_angle)
            wall_y = wall_center_radius * math.sin(wall_angle)
            wall_z = wall_height / 2.0

            success = self.add_collision_object(
                object_id=f"radial_wall_{index + 1}",
                primitive_type=SolidPrimitive.BOX,
                dimensions=[wall_length, wall_thickness, wall_height],
                position=(wall_x, wall_y, wall_z),
                yaw=wall_angle,
            )
            all_success = success and all_success

        return all_success

    def print_collision_objects(self) -> None:
        """Planning Scene에 등록된 객체를 확인한다."""
        with self.planning_scene_monitor.read_only() as scene:
            scene_msg = scene.planning_scene_message
            self.get_logger().info(f"planning frame: {scene.planning_frame}")

            for collision_object in scene_msg.world.collision_objects:
                self.get_logger().info(
                    "scene object: "
                    f"id={collision_object.id}, "
                    f"frame={collision_object.header.frame_id}"
                )

    def plan_and_execute(self, configuration_name: str) -> bool:
        """Named pose 계획을 재시도하고 성공한 경로만 실행한다."""
        for attempt in range(1, self.MAX_PLANNING_ATTEMPTS + 1):
            # 재시도할 때마다 실제 현재 관절 상태를 시작 상태로 다시 사용한다.
            self.arm.set_start_state_to_current_state()
            self.arm.set_goal_state(configuration_name=configuration_name)

            plan_result = self.arm.plan()
            if not plan_result:
                self.get_logger().warning(
                    f"경로 계획 실패: {configuration_name} "
                    f"({attempt}/{self.MAX_PLANNING_ATTEMPTS})"
                )
                continue

            self.moveit.execute(
                plan_result.trajectory,
                controllers=["arm_controller"],
            )
            self.get_logger().info(
                f"이동 완료: {configuration_name} ({attempt}번째 계획에서 성공)"
            )
            return True

        self.get_logger().error(
            f"경로 계획 최종 실패: {configuration_name}, 다음 pose로 진행합니다."
        )
        return False

    def move_between_walls(self) -> None:
        """home에서 시작해 여섯 벽 사이를 순서대로 이동한다."""
        # home 계획이 실패해도 현재 위치에서 첫 번째 sector 계획을 계속 시도한다.
        if not self.plan_and_execute("home"):
            self.get_logger().warning("home 이동을 건너뛰고 sector 이동을 시작합니다.")

        for pose_name in self.SECTOR_POSES:
            if not self.plan_and_execute(pose_name):
                # 실패한 pose만 생략하고 다음 벽 사이의 pose를 계속 계획한다.
                self.get_logger().warning(
                    f"{pose_name} 이동을 건너뛰고 다음 pose로 진행합니다."
                )

        # 마지막 home 복귀도 실패 여부와 관계없이 전체 순회를 종료한다.
        self.plan_and_execute("home")


def main() -> None:
    """미니 프로젝트 노드를 실행한다."""
    rclpy.init()
    node = MoveItMiniProjectNode()

    # 서비스 callback과 timer callback을 서로 다른 thread에서 처리한다.
    executor = MultiThreadedExecutor(num_threads=2)
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.try_shutdown()

        # 현재 수업 환경의 MoveItPy 종료 과정에서 발생할 수 있는
        # C++ 소멸자 SIGSEGV를 피하기 위해 기존 예제와 같은 방식으로 종료한다.
        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(0)


if __name__ == "__main__":
    main()