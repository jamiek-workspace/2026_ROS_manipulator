import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from user_interface.srv import AddAndOdd


class Service_server(Node):
    def __init__(self):
        super().__init__("service_server")
        self.create_service(AddAndOdd, "add_server", self.add_callback)

    def add_callback(self, request: AddAndOdd.Request, response: AddAndOdd.Response):
        response.sum = request.inta + request.intb
        if response.sum % 2:
            response.odd = "Two ints sum is odd"
        else:
            response.odd = "Two ints sum is not odd"
        return response


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = Service_server()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()