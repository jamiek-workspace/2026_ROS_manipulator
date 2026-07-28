"""MoveItPy로 OpenManipulator-X의 arm과 gripper를 실행한다."""

import time

import rclpy
from moveit.planning import MoveItPy


def plan_and_execute(
    moveit: MoveItPy,
    component,
    configuration_name: str,
    controller_name: str,
) -> bool:
    """현재 상태에서 named state까지 계획한 뒤 지정 controller로 실행한다."""
    component.set_start_state_to_current_state()
    component.set_goal_state(configuration_name=configuration_name)

    print(f"경로 계획 중: {configuration_name}")
    plan_result = component.plan()
    if not plan_result:
        print(f"경로 계획 실패: {configuration_name}")
        return False

    print(f"경로 실행 중: {configuration_name}")
    moveit.execute(
        plan_result.trajectory,
        controllers=[controller_name],
    )
    return True


def main() -> None:
    """arm을 home으로 이동하고 gripper를 열고 닫는다."""
    rclpy.init()
    try:
        moveit = MoveItPy(node_name="open_manipulator_moveit_py")
        arm = moveit.get_planning_component("arm")
        gripper = moveit.get_planning_component("gripper")

        if not plan_and_execute(
            moveit,
            arm,
            configuration_name="home",
            controller_name="arm_controller",
        ):
            return

        time.sleep(0.5)
        for goal_name in ("open", "close", "open"):
            if not plan_and_execute(
                moveit,
                gripper,
                configuration_name=goal_name,
                controller_name="gripper_controller",
            ):
                return
            time.sleep(0.7)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()