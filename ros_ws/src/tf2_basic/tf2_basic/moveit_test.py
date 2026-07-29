"""MoveItPy로 OpenManipulator-X의 arm과 gripper를 제어한다."""

import os
import sys

import rclpy
from moveit.planning import MoveItPy
from rclpy.logging import get_logger


def plan_and_execute(
    moveit: MoveItPy,
    component,
    configuration_name: str,
    controller_name: str,
) -> bool:
    """Named state까지 경로를 계획하고 실행한다."""
    component.set_start_state_to_current_state()
    component.set_goal_state(configuration_name=configuration_name)

    plan_result = component.plan()

    moveit.execute(
        plan_result.trajectory,
        controllers=[controller_name],
    )
    return True


def main() -> None:
    rclpy.init()
    logger = get_logger("moveit_test")
    moveit = MoveItPy(node_name="open_manipulator_moveit_py")
    arm = moveit.get_planning_component("arm")
    gripper = moveit.get_planning_component("gripper")

    for goal_name in ("home", "init", "home", "init"):
        plan_and_execute(
            moveit,
            arm,
            configuration_name=goal_name,
            controller_name="arm_controller",
        )
    for goal_name in ("open", "close", "open", "close"):
        plan_and_execute(
            moveit,
            gripper,
            configuration_name=goal_name,
            controller_name="gripper_controller",
        )

    logger.info("실습 완료")

    # MoveItPy 2.12.4는 MoveItCpp 소멸 중 SIGSEGV가 발생할 수 있다.
    # 이 일회성 노드는 성공 시 문제가 있는 C++ 소멸자 경로를 우회한다.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)


if __name__ == "__main__":
    main()