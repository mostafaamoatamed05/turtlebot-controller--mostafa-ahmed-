#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # Import Twist from geometry_msgs [cite: 21]

class TurtlebotMonitor(Node):
    def __init__(self):
        super().__init__('turtlebot_monitor')
        # Create a subscriber to receive messages on /cmd_vel topic [cite: 22, 53]
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback, # Define callback function to handle incoming data [cite: 23]
            10)
        self.get_logger().info("TurtleBot Monitor Node started. Waiting for dashboard data...")

    def cmd_vel_callback(self, msg):
        # Extract linear x and angular z values from the incoming Twist message [cite: 24, 25, 54, 55]
        linear_x = msg.linear.x
        angular_z = msg.angular.z
        
        # Print the values received in a clean, readable format [cite: 26, 56]
        print(f"--- [ DASHBOARD STATUS ] ---")
        print(f"Forward/Backward Velocity (linear.x) : {linear_x:.2f} m/s")
        print(f"Turning Velocity (angular.z)         : {angular_z:.2f} rad/s")
        print(f"-----------------------------\n")

def main(args=None):
    rclpy.init(args=args)
    node = TurtlebotMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
