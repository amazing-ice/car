#include <ros/ros.h>
#include <std_msgs/String.h>
#include <qq_msgs/Carry.h>

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "chao_node");
    printf("aaaaa\n");

    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<qq_msgs::Carry>("kuai_shang_che", 10);

    ros::Rate loop_rate(10);

    while (ros::ok())
    {
        printf("1111\n");
        qq_msgs::Carry msg;
        msg.data = "带飞";
        msg.grade = "王者";
        msg.star = 50;
        pub.publish(msg);
        loop_rate.sleep();
    }
    return 0;
}
