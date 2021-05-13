#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import rospy
from volcano_robotsim.msg import VolcanoGuiInfo
from geometry_msgs.msg import Twist,PointStamped
import time 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStyleFactory
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QTimer, QUrl, QRect
from PyQt5.QtGui import QIcon
from qt_gui_main import *
import rviz



class MyMainWindow(QMainWindow, Ui_MainWindow):
    # 初始化程序
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.InitTimer() # 初始化时钟
        ###### 设置icon ######
        self.setWindowIcon(QIcon("/home/mckros/catkin_ws/src/volcano_robotsim/scripts/qt_gui/icon1.png"))
        ###### 设置窗口风格 ######
        QApplication.setStyle("Windows")
        ###### 主界面按钮操作 ######
        self.btn_select.clicked.connect(self.gBox_location_window)
        self.btn_book.clicked.connect(self.gBox_book_window)
        self.btn_robot_state.clicked.connect(self.gBox_robot_window)
        self.gBox_location.hide()
        self.gBox_book.hide()
        self.gBox_robot.hide()
        ###### 位置选座界面 ######
        self.checked_num = 0
        self.checked_boxs = []
        self.checkBox_1.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_1,1))
        self.checkBox_2.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_2,2))
        self.checkBox_3.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_3,3))
        self.checkBox_4.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_4,4))
        self.checkBox_5.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_5,5))
        self.checkBox_6.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_6,6))
        self.checkBox_7.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_7,7))
        self.checkBox_8.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_8,8))
        self.checkBox_9.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_9,9))
        self.checkBox_10.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_10,10))
        self.checkBox_11.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_11,11))
        self.checkBox_12.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_12,12))
        self.checkBox_13.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_13,13))
        self.checkBox_14.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_14,14))
        self.checkBox_15.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_15,15))
        self.checkBox_16.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_16,16))
        self.checkBox_17.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_17,17))
        self.checkBox_18.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_18,18))
        self.checkBox_19.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_19,19))
        self.checkBox_20.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_20,20))
        self.checkBox_21.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_21,21))
        self.checkBox_22.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_22,22))
        self.checkBox_23.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_23,23))
        self.checkBox_24.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_24,24))
        self.checkBox_25.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_25,25))
        self.checkBox_26.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_26,26))
        self.checkBox_27.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_27,27))
        self.checkBox_28.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_28,28))
        self.checkBox_29.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_29,29))
        self.checkBox_30.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_30,30))
        self.checkBox_31.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_31,31))
        self.checkBox_32.stateChanged.connect(lambda:self.checkbox_state(self.checkBox_32,32))
        self.btn_select_ok.clicked.connect(self.select_seat_ok)
        ###### 查找书籍界面 ######
        self.btn_robot.clicked.connect(self.robot_follow)
        ###### 机器人状态界面 ######
        self.btn_control_qj.clicked.connect(lambda:self.robot_control_foo("qj")) # 前进
        self.btn_control_zz.clicked.connect(lambda:self.robot_control_foo("zz")) # 左转
        self.btn_control_yz.clicked.connect(lambda:self.robot_control_foo("yz")) # 右转
        self.btn_control_ht.clicked.connect(lambda:self.robot_control_foo("ht")) # 后退
        self.btn_control_tz.clicked.connect(lambda:self.robot_control_foo("tz")) # 停止
        self.angular_temp = 0
        self.linear_temp = 0
        self.h_slider_angular.valueChanged.connect(lambda:self.slider_control_foo("angular"))
        self.h_slider_linear.valueChanged.connect(lambda:self.slider_control_foo("linear"))

    def gps_val_label(self,x,y,z):
        self.label_point_x.setText(str(x))
        self.label_point_y.setText(str(y))
        self.label_point_z.setText(str(z))
    # 滑块控制函数
    def slider_control_foo(self,slider_f):
        if slider_f == 'angular':
            self.angular_temp = self.h_slider_angular.value()/100
            self.label_angular_val.setText(str(self.angular_temp))
        elif slider_f == 'linear':
            self.linear_temp = self.h_slider_linear.value()/100
            self.label_linear_val.setText(str(self.linear_temp))

    # 机器人远程控制函数
    # control_f 控制方式
    def robot_control_foo(self,control_f):
        Twist_msg = Twist()
        if control_f == 'qj':
            Twist_msg.angular.z = 0
            Twist_msg.linear.x = self.linear_temp
        elif control_f == 'zz':
            Twist_msg.angular.z = -(self.angular_temp)
            Twist_msg.linear.x = 0
        elif control_f == 'yz':
            Twist_msg.angular.z = self.angular_temp
            Twist_msg.linear.x = 0
        elif control_f == 'ht':
            Twist_msg.angular.z = 0
            Twist_msg.linear.x = -(self.linear_temp)
        elif control_f == 'tz':
            Twist_msg.angular.z = 0
            Twist_msg.linear.x = 0
        Twist_pub.publish(Twist_msg)

    # 获取复选框选择状态最多选择两个位置
    def checkbox_state(self,cbox_state,num):
        if cbox_state.isChecked():
            if self.checked_num >= 2:
                QMessageBox.warning(self.gBox_location,"提示","最多选择两个位置")
                cbox_state.setChecked(False)
            else:
                self.checked_num+=1;
                self.checked_boxs.append(num)
        else:
            self.checked_num-=1
            self.checked_boxs.remove(num)
       
    # 成功选择座位
    def select_seat_ok(self):
        VolcanoGuiInfo_msg = VolcanoGuiInfo()
        for i in range(len(self.checked_boxs)):
            VolcanoGuiInfo_msg.seat_number_on = self.checked_boxs[i]
            VolcanoGuiInfo_msg.seat_number_off = 0
            VolcanoGuiInfo_pub.publish(VolcanoGuiInfo_msg)
            time.sleep(0.5)
        
    # 机器人引导
    def robot_follow(self):
        if len(self.lineEdit_book.text()) == 0:
            QMessageBox.warning(self.gBox_book,"提示","索书号为空")
        else:
            VolcanoGuiInfo_msg = VolcanoGuiInfo()
            VolcanoGuiInfo_msg.book_number = self.lineEdit_book.text()
            VolcanoGuiInfo_msg.seat_number_on = 0
            VolcanoGuiInfo_msg.seat_number_off = 0
            VolcanoGuiInfo_msg.is_follow = 1
            VolcanoGuiInfo_pub.publish(VolcanoGuiInfo_msg)
    
    # 打开选座group窗口
    def gBox_location_window(self):
        self.gBox_robot.hide()
        self.gBox_book.hide()
        self.gBox_location.show()

    # 打开查找书籍group窗口
    def gBox_book_window(self):
        self.gBox_robot.hide()
        self.gBox_location.hide()
        self.gBox_book.show()
    
    # 打开机器人状态group窗口
    def gBox_robot_window(self):
        self.gBox_location.hide()
        self.gBox_book.hide()
        self.gBox_robot.show()
    
    # 初始化时钟，每一秒刷新时间
    def InitTimer(self):
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.showTime)
    
    # 在label_time上显示时间
    def showTime(self):
        self.label_time.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def GpsCallBack(msg):
    mywin.gps_val_label(msg.point.x, msg.point.y, msg.point.z)
    # self.label_point_x.setText(msg.point.x)
    # self.label_point_y.setText(msg.point.y)
    # self.label_point_z.setText(msg.point.z)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    rospy.init_node("robot_gui_node", anonymous=True)
    # 发布gui下一些信息
    VolcanoGuiInfo_pub = rospy.Publisher("/gui_info",VolcanoGuiInfo,queue_size=1)
    Twist_pub = rospy.Publisher("/cmd_vel",Twist,queue_size=1)
    rospy.Subscriber("/volcano/gps/values",PointStamped,GpsCallBack)

    sys.exit(app.exec_())
    rospy.spin()
