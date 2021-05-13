#!/usr/bin/env python3
import cv2
import numpy as np
import time
from threading import Thread 
import rospy
from sensor_msgs.msg import Image
from webots_ros.srv import set_int 
from webots_ros.msg import RecognitionObject
TIME_STEP = 32
i = 0
# 始能RGB相机服务
def kinect_color_service():
    rospy.wait_for_service("/volcano/kinect_color/enable")
    try:
        camera_client = rospy.ServiceProxy("/volcano/kinect_color/enable", set_int)
        response = camera_client(TIME_STEP)
        return response.success
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
# 始能深度服务
def kinect_range_service():
    rospy.wait_for_service("/volcano/kinect_range/enable")
    try:
        camera_Recognition_client = rospy.ServiceProxy("/volcano/kinect_range/enable",set_int)
        response = camera_Recognition_client(TIME_STEP)
        return response.success
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


# 摄像头topic回调函数
def cameraCallback(data):
    img_array = np.frombuffer(data.data,dtype=np.uint8)
    img = img_array.reshape([190, 320, 4])
    depth = cv2.split(img)[2]
    # depth[depth>200]=255
    # depth = depth/1000.0
    # for x in range(20):
    #     for y in range(320):
    #         # print(depth[x,y])
    #         if depth[x,y]<90:
    #             print("stop")
    cv2.imshow("camera",depth)
    key = cv2.waitKey(3)
    if key == 66:
        global i
        cv2.imwrite(str(i) + ".png",img)
        i+=1
        print("saved success")
    


if __name__ == "__main__":
    rospy.init_node("robot_camera", anonymous=True)
    print(kinect_color_service())
    print(kinect_range_service())
    # rospy.Subscriber("/volcano/kinect_range/range_image", RecognitionObject, recognition_objects_callback)
    rospy.Subscriber("/volcano/kinect_range/range_image",Image, cameraCallback)
    rospy.spin()