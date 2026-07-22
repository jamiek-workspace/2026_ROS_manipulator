import time
import rclpy
from rclpy.node import Node
from user_interface.srv import AddAndOdd
import threading
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup



class Service_server(Node):
    def __init__(self):
        super().__init__("service_server")

        self.lock = threading.Lock()

        # Callback Group 생성
        self.callback_group = ReentrantCallbackGroup()

        # Service 생성
        self.create_service(
            AddAndOdd,
            "add_server",
            self.add_callback,
            callback_group=self.callback_group
        )

    def add_callback(self, request: AddAndOdd.Request, response: AddAndOdd.Response):
        with self.lock:
            response.sum = request.inta + request.intb
        time.sleep(5)  # Simulate a long-running operation
        if response.sum % 2:
            response.odd = "Two ints sum is odd"
        else:
            response.odd = "Two ints sum is not odd"
        return response


def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = Service_server()
    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()