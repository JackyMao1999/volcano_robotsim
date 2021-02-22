#include "string.h"
#include "volcano_robotsim/VolcanoGoal.h" 
#include "geometry_msgs/PoseStamped.h"
#include "ros/ros.h"
 
using namespace std;
 
ros::NodeHandle *n;
ros::Publisher pub_goal;
void goalCallback(const volcano_robotsim::VolcanoGoal::ConstPtr &value);

int main(int argc, char **argv) {
   
    // create a node named 'volcano' on ROS network
    ros::init(argc, argv, "volcano_set_goal");
    n = new ros::NodeHandle;
    ros::Subscriber sub_goal;
    sub_goal = n->subscribe("/volcano/goal",1,goalCallback);
    
    pub_goal = n->advertise<geometry_msgs::PoseStamped>("/move_base_simple/goal",2);
    ROS_INFO("Started success ");
    ros::spin();
}
void goalCallback(const volcano_robotsim::VolcanoGoal::ConstPtr &value){
    int isture=0;
    string goal_name = value->goal_name;
    geometry_msgs::PoseStamped target_pose;
    target_pose.header.seq = 1;
    target_pose.header.frame_id = "map";
    
    if (goal_name == "A"||goal_name == "B")
    {
        target_pose.pose.position.x = -2.0;
        target_pose.pose.position.y = 6.29;
        target_pose.pose.orientation.z = 0.0016;
        target_pose.pose.orientation.w = 0.9999;
        isture = 1;
    }else if(goal_name == "C"||goal_name == "D")
    {
        target_pose.pose.position.x = -2.0;
        target_pose.pose.position.y = 3.7;
        target_pose.pose.orientation.z = 0.0016;
        target_pose.pose.orientation.w = 0.9999;
        isture = 1;
    }else if (goal_name == "E"||goal_name == "F")
    {
        target_pose.pose.position.x = -2.0;
        target_pose.pose.position.y = 1.21;
        target_pose.pose.orientation.z = 0.0016;
        target_pose.pose.orientation.w = 0.9999;
        isture = 1;
    }else if (goal_name == "G"||goal_name == "H")
    {
        target_pose.pose.position.x = -2.0;
        target_pose.pose.position.y = -1.21;
        target_pose.pose.orientation.z = 0.0016;
        target_pose.pose.orientation.w = 0.9999;
        isture = 1;
    }else if (goal_name == "T"||goal_name == "TB"||goal_name == "TD")
    {
        target_pose.pose.position.x = -7.0;
        target_pose.pose.position.y = 5.95;
        target_pose.pose.orientation.z = 0.9999;
        target_pose.pose.orientation.w = 0.0028;
        isture = 1;
    }else if (goal_name == "TE"||goal_name == "TF"||goal_name == "TG")
    {
        target_pose.pose.position.x = -7.0;
        target_pose.pose.position.y = 3.6;
        target_pose.pose.orientation.z = 0.9999;
        target_pose.pose.orientation.w = 0.0028;
        isture = 1;
    }else if (goal_name == "TH"||goal_name == "TJ"||goal_name == "TK")
    {
        target_pose.pose.position.x = -7.0;
        target_pose.pose.position.y = 1.11;
        target_pose.pose.orientation.z = 0.9999;
        target_pose.pose.orientation.w = 0.0028;
        isture = 1;
    }else if (goal_name == "TL"||goal_name == "TM"||goal_name == "TN")
    {
        target_pose.pose.position.x = -7.0;
        target_pose.pose.position.y = -1.19;
        target_pose.pose.orientation.z = 0.9999;
        target_pose.pose.orientation.w = 0.0028;
        isture = 1;
    }

    if (isture)
    {
        target_pose.header.stamp = ros::Time::now();
        pub_goal.publish(target_pose);
        ROS_INFO("Ready to go to the goal %s",goal_name.c_str());
    }
    else
    {
        ROS_ERROR("Can't compare the goal");
    }
}
