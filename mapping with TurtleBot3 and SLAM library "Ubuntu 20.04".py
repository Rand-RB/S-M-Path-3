#open the terminal and run the following commands
cd catkin_ws/
git clone https://github.com/ros-perception/openslam_gmapping src/openslam_gmapping
git clone https://github.com/ros-perception/slam_gmapping src/slam_gmapping
rosdep install --from-paths src/ -i
catkin_make -DCMAKE_BUILD_TYPE=RelWithDebInfo

#to run turtlebot simulation
source devel/setup.bash
#then choose one from the following simulation environment
# TurtleBot3 World
roslaunch turtlebot3_gazebo turtlebot3_world.launch
#or TurtleBot3 House
roslaunch turtlebot3_gazebo turtlebot3_house.launch

#to launch SLAM open new terminal and write
source devel/setup.bash
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
#Remotely Control TurtleBot3 open new terminal and write
source devel/setup.bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch




