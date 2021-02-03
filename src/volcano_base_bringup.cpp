#include <sensor_msgs/Image.h>
#include <sensor_msgs/Imu.h>
#include <sensor_msgs/LaserScan.h>
#include <sensor_msgs/NavSatFix.h>
#include <nav_msgs/Odometry.h>
#include <signal.h>
#include <std_msgs/String.h>
#include <tf/transform_broadcaster.h>
#include "ros/ros.h"

#include <rosgraph_msgs/Clock.h>

#include <webots_ros/set_float.h>
#include <webots_ros/set_int.h>
#include <webots_ros/Int32Stamped.h>
#include <webots_ros/Float64Stamped.h>

using namespace std;

#define TIME_STEP 32    //时钟
// #define MAX_SPEED 6.4
// #define OBSTACLE_THRESHOLD 0.1
// #define DECREASE_FACTOR 0.9
// #define BACK_SLOWDOWN 0.9
ros::NodeHandle *n;

static int controllerCount;
static std::vector<std::string> controllerList; 

ros::ServiceClient timeStepClient;          //时钟通讯客户端
webots_ros::set_int timeStepSrv;            //时钟服务数据

// static std::vector<float> lidarValues;

double GPSvalues[3];
double Inertialvalues[4];
// double accvalues[3];
// double gyrovalues[3];


/*******************************************************
* Function name ：controllerNameCallback
* Description   ：控制器名回调函数，获取当前ROS存在的机器人控制器
* Parameter     ：
        @name   控制器名
* Return        ：无
**********************************************************/
// catch names of the controllers availables on ROS network
void controllerNameCallback(const std_msgs::String::ConstPtr &name) { 
    controllerCount++; 
    controllerList.push_back(name->data);//将控制器名加入到列表中
    ROS_INFO("Controller #%d: %s.", controllerCount, controllerList.back().c_str());

}

/*******************************************************
* Function name ：quit
* Description   ：退出函数
* Parameter     ：
        @sig   信号
* Return        ：无
**********************************************************/
void quit(int sig) {
    ROS_INFO("User stopped the '/volcano' node.");
    timeStepSrv.request.value = 0; 
    timeStepClient.call(timeStepSrv); 
    ros::shutdown();
    exit(0);
}

void broadcastTransform()
{
    static tf::TransformBroadcaster br;
    tf::Transform transform;
    transform.setOrigin(tf::Vector3(-GPSvalues[2],GPSvalues[0],GPSvalues[1]));
    tf::Quaternion q(Inertialvalues[0],Inertialvalues[1],Inertialvalues[2],Inertialvalues[3]);
    q = q.inverse();
    transform.setRotation(q);
    br.sendTransform(tf::StampedTransform(transform,ros::Time::now(),"odom","base_link"));
    transform.setIdentity();
    br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "base_link", "volcano/Sick_LMS_291"));
    // br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "base_link", "volcano/inertial_unit"));
    // br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "base_link", "volcano/gps"));
}


void InertialUnitCallback(const sensor_msgs::Imu::ConstPtr &value)
{
    
    Inertialvalues[0] = value->orientation.x;
    Inertialvalues[1] = value->orientation.y;
    Inertialvalues[2] = value->orientation.z;
    Inertialvalues[3] = value->orientation.w;
    broadcastTransform();
}
void GPSCallback(const sensor_msgs::NavSatFix::ConstPtr &value)
{
    GPSvalues[0] = value->latitude;
    GPSvalues[1] = value->altitude;
    GPSvalues[2] = value->longitude;
    broadcastTransform();  
}
// void GPSspeedCallback(const webots_ros::Float64Stamped::ConstPtr &value)
// {
//     liner_speed = value->data;

// }

// void AccCallback(const sensor_msgs::Imu::ConstPtr &value)
// {
    
//     accvalues[0] = value->linear_acceleration.x;
//     accvalues[1] = value->linear_acceleration.y;
//     accvalues[2] = value->linear_acceleration.z;
    
//     send_odom_data();
// }
// void gyroCallback(const sensor_msgs::Imu::ConstPtr &value)
// {
//     gyrovalues[0] = value->angular_velocity.x;
//     gyrovalues[1] = value->angular_velocity.y;
//     gyrovalues[2] = value->angular_velocity.z;

//     send_odom_data();
// }

int main(int argc,char **argv)
{
    std::string controllerName;
    // create a node named 'volcano' on ROS network
    ros::init(argc, argv, "volcano_init", ros::init_options::AnonymousName);
    n = new ros::NodeHandle;

    signal(SIGINT, quit);

    // subscribe to the topic model_name to get the list of availables controllers
    ros::Subscriber nameSub = n->subscribe("model_name", 100, controllerNameCallback);
    while (controllerCount == 0 || controllerCount < nameSub.getNumPublishers()) {
        ros::spinOnce();
    }
    ros::spinOnce();

    timeStepClient = n->serviceClient<webots_ros::set_int>("volcano/robot/time_step");
    timeStepSrv.request.value = TIME_STEP;

    // if there is more than one controller available, it let the user choose
    if (controllerCount == 1)
        controllerName = controllerList[0];
    else {
        int wantedController = 0;
        std::cout << "Choose the # of the controller you want to use:\n";
        std::cin >> wantedController;
        if (1 <= wantedController && wantedController <= controllerCount)
        controllerName = controllerList[wantedController - 1];
        else {
        ROS_ERROR("Invalid number for controller choice.");
        return 1;
        }
    }
    ROS_INFO("Using controller: '%s'", controllerName.c_str());
    // leave topic once it is not necessary anymore
    nameSub.shutdown();

    // enable lidar
    ros::ServiceClient set_lidar_client;
    webots_ros::set_int lidar_srv;
    ros::Subscriber sub_lidar_scan;

    set_lidar_client = n->serviceClient<webots_ros::set_int>("volcano/Sick_LMS_291/enable");
    lidar_srv.request.value = TIME_STEP;
    if (set_lidar_client.call(lidar_srv) && lidar_srv.response.success) {
        ROS_INFO("Lidar enabled.");
        // sub_lidar_scan = n->subscribe("volcano/Sick_LMS_291/laser_scan/layer0", 10, lidarCallback);
        // ROS_INFO("Topic for lidar initialized.");
        // while (sub_lidar_scan.getNumPublishers() == 0) {
        // }
        // ROS_INFO("Topic for lidar scan connected.");
    } else {
        if (!lidar_srv.response.success)
        ROS_ERROR("Sampling period is not valid.");
        ROS_ERROR("Failed to enable lidar.");
        return 1;
    }

    // enable gps
    ros::ServiceClient set_GPS_client;
    webots_ros::set_int GPS_srv;
    ros::Subscriber sub_GPS;
    ros::Subscriber sub_GPS_speed;
    set_GPS_client = n->serviceClient<webots_ros::set_int>("volcano/gps/enable");
    GPS_srv.request.value = TIME_STEP;
    if (set_GPS_client.call(GPS_srv) && GPS_srv.response.success) {
        sub_GPS = n->subscribe("volcano/gps/values", 1, GPSCallback);
        // sub_GPS_speed = n->subscribe("volcano/gps/speed", 1, GPSspeedCallback);
        while (sub_GPS.getNumPublishers() == 0) {
        }
        ROS_INFO("GPS enabled.");
    } else {
        if (!GPS_srv.response.success)
        ROS_ERROR("Sampling period is not valid.");
        ROS_ERROR("Failed to enable GPS.");
        return 1;
    }

    // enable inertial unit
    ros::ServiceClient set_inertial_unit_client;
    webots_ros::set_int inertial_unit_srv;
    ros::Subscriber sub_inertial_unit;
    set_inertial_unit_client = n->serviceClient<webots_ros::set_int>("volcano/inertial_unit/enable");
    inertial_unit_srv.request.value = TIME_STEP;
    if (set_inertial_unit_client.call(inertial_unit_srv) && inertial_unit_srv.response.success) {
        sub_inertial_unit = n->subscribe("volcano/inertial_unit/roll_pitch_yaw", 1, InertialUnitCallback);
        while (sub_inertial_unit.getNumPublishers() == 0) {
        }
        ROS_INFO("Inertial unit enabled.");
    } else {
        if (!inertial_unit_srv.response.success)
        ROS_ERROR("Sampling period is not valid.");
        ROS_ERROR("Failed to enable inertial unit.");
        return 1;
    }

    // enable acceleration
    // ros::ServiceClient set_acc_client;
    // webots_ros::set_int acc_srv;
    // ros::Subscriber sub_acc;
    // set_acc_client = n->serviceClient<webots_ros::set_int>("volcano/accelerometer/enable");
    // acc_srv.request.value = TIME_STEP;
    // if (set_acc_client.call(acc_srv) && acc_srv.response.success) {
    //     sub_acc = n->subscribe("volcano/accelerometer/values", 1, AccCallback);
    //     while (sub_acc.getNumPublishers() == 0) {
    //     }
    //     ROS_INFO("Inertial unit enabled.");
    // } else {
    //     if (!inertial_unit_srv.response.success)
    //     ROS_ERROR("Sampling period is not valid.");
    //     ROS_ERROR("Failed to enable inertial unit.");
    //     return 1;
    // }

    // enable gyro
    // ros::ServiceClient set_gyro_client;
    // webots_ros::set_int gyro_srv;
    // ros::Subscriber sub_gyro;
    // set_gyro_client = n->serviceClient<webots_ros::set_int>("volcano/gyro/enable");
    // gyro_srv.request.value = TIME_STEP;
    // if (set_gyro_client.call(gyro_srv) && gyro_srv.response.success) {
    //     sub_gyro = n->subscribe("volcano/gyro/values", 1, gyroCallback);
    //     while (sub_gyro.getNumPublishers() == 0) {
    //     }
    //     ROS_INFO("Inertial unit enabled.");
    // } else {
    //     if (!inertial_unit_srv.response.success)
    //     ROS_ERROR("Sampling period is not valid.");
    //     ROS_ERROR("Failed to enable inertial unit.");
    //     return 1;
    // }

    


    ROS_INFO("You can now start the creation of the map using 'rosrun gmapping slam_gmapping "
            "scan:=/volcano/Sick_LMS_291/laser_scan/layer0 _xmax:=30 _xmin:=-30 _ymax:=30 _ymin:=-30 _delta:=0.2'.");
    ROS_INFO("You can now visualize the sensors output in rqt using 'rqt'.");

    // main loop
    while (ros::ok()) {
        if (!timeStepClient.call(timeStepSrv) || !timeStepSrv.response.success) {
        ROS_ERROR("Failed to call service time_step for next step.");
        break;
        }
        ros::spinOnce();
    }
    timeStepSrv.request.value = 0;
    timeStepClient.call(timeStepSrv);

    ros::shutdown();
    return 0;

}