import rclpy
from rclpy.parameter import Parameter
from rclpy.node import Node
from rclpy.parameter_client import AsyncParameterClient



class TParam(Node):
    def __init__(self):
        super().__init__("tparamAsync")  # 노드 이름
        # timer 등록
        self.target_node_name = "/tparam"
        self.parameter_client = AsyncParameterClient(self, self.target_node_name)
        self.create_timer(1.0, self.timer_callback)
        self.count = 0


    def timer_callback(self):
        parameter = Parameter(
            name="my_param",
            type_ = Parameter.Type.STRING,
            value=f"외부 노드에서 변경한 값 {self.count}",
            )
        self.count += 1
        future = self.parameter_client.set_parameters([parameter])
        future.add_done_callback(self.parameter_result_callback)

    def parameter_result_callback(self, future):
        try:
            response = future.result()

            for result in response.results:
                if result.successful:
                    self.get_logger().info("Parameter set successfully")
                else:
                    self.get_logger().error(
                        f"Failed to set parameter: {result.reason}"
                    )

        except Exception as error:
            self.get_logger().error(
                f"Parameter request failed: {error}"
            )

def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = TParam()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()