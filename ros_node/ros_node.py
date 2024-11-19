import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ROS2Node(Node):
    def __init__(self):
        super().__init__('flask_ros2_bridge')
        self.publisher_ = self.create_publisher(String, '/web_command', 10)
        self.subscriber_ = self.create_subscription(
            String,
            '/ros2_topic',
            self.listener_callback,
            10
        )
        self.latest_message = None

    def listener_callback(self, msg):
        self.get_logger().info(f'Received message: {msg.data}')
        self.latest_message = msg.data

    def publish_command(self, command):
        msg = String()
        msg.data = command
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {command}')

# ROS 2 실행 함수
def ros2_runner():
    rclpy.init()
    global ros_node
    ros_node = ROS2Node()
    rclpy.spin(ros_node)
    ros_node.destroy_node()
    rclpy.shutdown()