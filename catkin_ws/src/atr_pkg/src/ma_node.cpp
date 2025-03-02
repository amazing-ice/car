#include <ros/ros.h>
#include <std_msgs/String.h>
#include <qq_msgs/Carry.h>

void chao_callback(qq_msgs::Carry msg)
{
    ROS_WARN(msg.grade.c_str());
    ROS_WARN("%d 星", msg.star);
    ROS_INFO(msg.data.c_str());
    //printf("\n");
}

void yao_callback(qq_msgs::Carry msg)
{
    ROS_WARN(msg.data.c_str());
    //printf("\n");
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc, argv, "ma_node");

    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("kuai_shang_che", 10, chao_callback);
    ros::Subscriber sub_2 = nh.subscribe("ge_ge", 10, yao_callback);
    
    while(ros::ok())
    {
        ros::spinOnce();
    }

    return 0;
}
