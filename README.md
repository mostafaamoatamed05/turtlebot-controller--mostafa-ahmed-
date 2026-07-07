# ROS 2 Assignment 2 – TurtleBot3 Keyboard Controller

## Project Overview

This project demonstrates communication between ROS 2 nodes using the **Publisher/Subscriber** architecture.

The project consists of two Python nodes:

- **cmd_vel_publisher.py**
  - Reads keyboard commands.
  - Publishes `Twist` messages to the `/cmd_vel` topic.

- **cmd_vel_subscriber.py**
  - Subscribes to the `/cmd_vel` topic.
  - Displays the received linear and angular velocities.

The TurtleBot3 moves according to the keyboard commands.

---

# 1. Step-by-Step Setup Instructions

## Step 1: Create a ROS 2 Workspace

```bash
mkdir -p ~/etgah_ws/src
cd ~/etgah_ws
```

---

## Step 2: Create the Python Package

```bash
cd src

ros2 pkg create turtlebot_controller_pkg \
--build-type ament_python \
--dependencies rclpy geometry_msgs
```

---

## Step 3: Copy the Python Files

Place the following files inside:

```
turtlebot_controller_pkg/
```

- cmd_vel_publisher.py
- cmd_vel_subscriber.py

---

## Step 4: Build the Workspace

```bash
cd ~/etgah_ws

colcon build
```

---

## Step 5: Source the Workspace

```bash
source install/setup.bash
```

---

## Step 6: Run the Nodes

Terminal 1

```bash
ros2 run turtlebot_controller_pkg cmd_vel_subscriber
```

Terminal 2

```bash
ros2 run turtlebot_controller_pkg cmd_vel_publisher
```

---

# 2. Linux Commands Used

| Command | Description |
|----------|-------------|
| mkdir | Creates a new directory. |
| cd | Changes the current directory. |
| ls | Lists files and folders. |
| pwd | Displays the current working directory. |
| cp | Copies files. |
| nano | Opens a file in the Nano text editor. |
| chmod | Changes file permissions. |
| source | Loads environment variables into the current terminal. |

---

# 3. ROS 2 Commands Used

### Create Package

```bash
ros2 pkg create turtlebot_controller_pkg --build-type ament_python --dependencies rclpy geometry_msgs
```

Creates a new ROS 2 Python package.

---

### Build Workspace

```bash
colcon build
```

Builds all packages inside the workspace.

---

### Source Workspace

```bash
source install/setup.bash
```

Makes the built packages available in the current terminal.

---

### Run Publisher

```bash
ros2 run turtlebot_controller_pkg cmd_vel_publisher
```

Starts the keyboard controller node.

---

### Run Subscriber

```bash
ros2 run turtlebot_controller_pkg cmd_vel_subscriber
```

Starts the monitoring node.

---

### View Topic Data (Optional)

```bash
ros2 topic echo /cmd_vel
```

Displays all published Twist messages.

---

### List Running Topics (Optional)

```bash
ros2 topic list
```

Displays all active ROS 2 topics.

---

# 4. How to Test the Nodes

1. Launch the TurtleBot3 simulation.

2. Build the workspace.

```bash
colcon build
```

3. Source the workspace.

```bash
source install/setup.bash
```

4. Run the subscriber.

```bash
ros2 run turtlebot_controller_pkg cmd_vel_subscriber
```

5. Run the publisher.

```bash
ros2 run turtlebot_controller_pkg cmd_vel_publisher
```

6. Enter keyboard commands:

```
W -> Move Forward

S -> Move Backward

A -> Turn Left

D -> Turn Right

X -> Stop

Q -> Quit
```

7. Verify:

- The robot moves correctly in Gazebo.
- The subscriber prints the received velocities.
- The `/cmd_vel` topic publishes Twist messages.

---

# 5. Expected Output

Publisher Terminal

```
========== TurtleBot Controller ==========
W : Move Forward
S : Move Backward
A : Turn Left
D : Turn Right
X : Stop
Q : Quit

Enter Command: w

Moving Forward

Enter Command: a

Turning Left

Enter Command: x

Stopping Robot
```

---

Subscriber Terminal

```
Cmd Vel Subscriber Node has started.

Received:
linear.x = 0.5
angular.z = 0.0

Received:
linear.x = 0.0
angular.z = 1.0

Received:
linear.x = 0.0
angular.z = 0.0
```

---

# 6. Project Demo

The demo should include:

- Launching the TurtleBot3 simulation.
- Running the subscriber node.
- Running the publisher node.
- Sending keyboard commands (W, A, S, D, X, Q).
- Showing the robot moving inside Gazebo.
- Showing the subscriber receiving the published velocity commands.
- Showing both terminals while the project is running.

---

## Project Structure

```
etgah_ws/
│
├── src/
│   └── turtlebot_controller_pkg/
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       └── turtlebot_controller_pkg/
│           ├── __init__.py
│           ├── cmd_vel_publisher.py
│           └── cmd_vel_subscriber.py
│
├── build/
├── install/
└── log/
```

---

## Author

**Mostafa**
ROS 2 Assignment 2 – ETGAH Robotics
