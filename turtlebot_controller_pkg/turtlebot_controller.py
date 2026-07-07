#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # Import Twist from geometry_msgs [cite: 46]
import sys
import select
import tty
import termios

# Help message displaying controls to the user
msg = """
Control Your TurtleBot3!
---------------------------
Moving around:
        w
   a    s    d

q : Stop and quit
---------------------------
"""

# Settings required to save terminal state for key tracking
settings = termios.tcgetattr(sys.stdin)

def get_key():
    """Reads keyboard input directly from the terminal terminal without needing Enter."""
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class TurtlebotController(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')
        # Create a publisher to publish Twist messages to the /cmd_vel topic [cite: 47]
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Define linear and angular speeds
        self.linear_speed = 0.2  # m/s
        self.angular_speed = 0.5 # rad/s
        
        # Create a timer to constantly check for keyboard input [cite: 13]
        self.timer = self.create_timer(0.1, self.check_keyboard)
        print(msg)

    def check_keyboard(self):
        key = get_key()
        twist = Twist()

        if key == 'w':   # Handle W key: forward motion [cite: 48]
            twist.linear.x = self.linear_speed
            twist.angular.z = 0.0
            print("Moving Forward...")
        elif key == 's': # Handle S key: backward motion [cite: 49]
            twist.linear.x = -self.linear_speed
            twist.angular.z = 0.0
            print("Moving Backward...")
        elif key == 'a': # Handle A key: turn left [cite: 49]
            twist.linear.x = 0.0
            twist.angular.z = self.angular_speed
            print("Turning Left...")
        elif key == 'd': # Handle D key: turn right [cite: 50]
            twist.linear.x = 0.0
            twist.angular.z = -self.angular_speed
            print("Turning Right...")
        elif key == 'q': # Handle Q key: stop and exit [cite: 51]
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.publisher_.publish(twist)
            print("Stopping and Exiting...")
            # Restore terminal settings and destroy node safely
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
            self.destroy_node()
            rclpy.shutdown()
            sys.exit(0)
        else:
            # If no key is pressed, continue running without resetting velocity immediately
            return

        # Publish the movement commands [cite: 15]
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = TurtlebotController()
    try:
        rclpy.spin(node)
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        # Final safety measure to restore terminal attributes if it crashes
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

if __name__ == '__main__':
    main()
