# volcano_robotsim_R2020
ROS package for Webots R2020 ver1

## 注意点
1. volcano_robotsim 功能包，适用于R2020 ver1版本的webots使用。

## 1.创建工作空间
```shell
$ mkdir volcano_ws/src -p
$ cd ~/volcano_ws/src
```
## 2.部署volcano_robotsim功能包
``` shell
$ cd ~/volcano_ws/src
$ git clone https://github.com/JackyMao1999/volcano_robotsim.git
```
## 3.编译工作空间 volcano_ws
```shell
$ source /opt/ros/melodic/setup.bash
$ cd ~/volcano_ws/
$ catkin_make
$ echo "source ~/volcano_ws/devel/setup.bash --extend" >> ~/.bashrc
```
## 4.gmapping建图使用方法
1. 启动webots仿真软件
``` shell
roslaunch volcano_robotsim volcano_webots.launch 
```
2. 初始化机器人
``` shell
rosrun volcano_robotsim volcano_base_bringup
```
3. 启动cartographer建图和move_base导航，其他导航算法启动方法类似
``` shell
roslaunch volcano_robotsim slam_base_cartographer.launch
```
4. 启动机器人控制移动程序
``` shell
rosrun volcano_robotsim volcano_velocity_v3
```
5. 操控机器人建图

## 5.cartographer建图使用方法
1. 启动webots仿真软件
```shell
roslaunch volcano_robotsim volcano_webots.launch 
```
2. 初始化机器人
```shell
rosrun volcano_robotsim volcano_cartographer_bringup
```
3. 启动cartographer建图和move_base导航，其他导航算法启动方法类似
```shell
roslaunch volcano_robotsim slam_base_gmapping.launch
```
4. 启动机器人控制移动程序
```shell
rosrun volcano_robotsim volcano_velocity_v3
```
5. 操控机器人建图

## 6.设定目标点导航
1. 启动webots仿真软件
```shell
roslaunch volcano_robotsim volcano_webots.launch 
```
2. 初始化机器人
```shell
rosrun volcano_robotsim volcano_cartographer_bringup
```
3. 启动cartographer建图或者gmapping建图和move_base导航，其他导航算法启动方法类似
```shell
roslaunch volcano_robotsim slam_base_cartographer.launch
```
4. 启动机器人控制移动程序
```shell
rosrun volcano_robotsim volcano_set_goals
```
5. 启动机器人控制移动程序
```shell
rosrun volcano_robotsim volcano_velocity_v3
```
6. 使用Riz中的`2D Nav Goal`按钮设置导航点，机器人就会导航了




其中所有功能都可在bilibili上查看：[毕业设计视频-图书馆管理机器人](https://www.bilibili.com/video/BV1mU4y1L77b?share_source=copy_web)
CSDN教程地址(持续更新)：[ROS联合webots实战案例目录](https://blog.csdn.net/xiaokai1999/article/details/112601720?spm=1001.2014.3001.5502)
锡城筱凯 备 2021/06/05
