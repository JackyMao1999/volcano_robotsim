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
# 始能相机服务
def camera_service():
    rospy.wait_for_service("/ur10emm/camera/enable")
    try:
        camera_client = rospy.ServiceProxy("/ur10emm/camera/enable", set_int)
        response = camera_client(TIME_STEP)
        return response.success
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
# 始能相机分割服务
def camera_Recognition_service():
    rospy.wait_for_service("/ur10emm/camera/recognition_enable")
    try:
        camera_Recognition_client = rospy.ServiceProxy("/ur10emm/camera/recognition_enable",set_int)
        response = camera_Recognition_client(TIME_STEP)
        return response.success
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

# 识别物体数据回调
def recognition_objects_callback(data):
    print(data.model)

# # 摄像头topic回调函数
# def cameraCallback(data):
#     img_array = np.frombuffer(data.data,dtype=np.uint8)
#     img = img_array.reshape([128, 256, 4])
#     cv2.imshow("camera",img)
#     key = cv2.waitKey(3)
#     if key == 66:
#         global i
#         cv2.imwrite(str(i) + ".png",img)
#         i+=1
#         print("saved success")
    


if __name__ == "__main__":
    rospy.init_node("robot_camera", anonymous=True)
    print(camera_service())
    print(camera_Recognition_service())
    rospy.Subscriber("/ur10emm/camera/recognition_objects", RecognitionObject, recognition_objects_callback)
    # rospy.Subscriber("/ur5e/camera/image",Image, cameraCallback)
    rospy.spin()