# volcano_robotsim_R2020
ROS package for Webots R2020 ver1

## 注意点
1. volcano_robotsim 功能包，适用于R2020 ver1版本的webots使用。

## 创建工作空间
$ mkdir volcano_ws/src -p

$ cd ~/volcano_ws/src

## 部署volcano_robotsim功能包
$ cd ~/volcano_ws/src

$ git clone https://github.com/JackyMao1999/volcano_robotsim.git

## 编译工作空间 volcano_ws
$ source /opt/ros/melodic/setup.bash

$ cd ~/volcano_ws/

$ catkin_make

$ echo "source ~/volcano_ws/devel/setup.bash --extend" >> ~/.bashrc


## gmapping建图使用方法
1. 启动webots仿真软件
roslaunch volcano_webots.launch 
2. 初始化机器人
rosrun volcano_base_bringup
3. 启动cartographer建图和move_base导航，其他导航算法启动方法类似
roslaunch slam_base_cartographer.launch
4. 启动机器人控制移动程序
rosrun volcano_velocity_v3
5. 操控机器人建图

## cartographer建图使用方法
1. 启动webots仿真软件
roslaunch volcano_webots.launch 
2. 初始化机器人
rosrun volcano_cartographer_bringup
3. 启动cartographer建图和move_base导航，其他导航算法启动方法类似
roslaunch slam_base_gmapping.launch
4. 启动机器人控制移动程序
rosrun volcano_velocity_v3
5. 操控机器人建图

## 设定目标点导航
1. 启动webots仿真软件
roslaunch volcano_webots.launch 
2. 初始化机器人
rosrun volcano_cartographer_bringup
3. 启动cartographer建图和move_base导航，其他导航算法启动方法类似
roslaunch slam_base_cartographer.launch
4. 启动机器人控制移动程序
rosrun volcano_set_goals


锡城筱凯 备 2021/06/01
