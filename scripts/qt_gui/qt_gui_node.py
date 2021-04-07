#!/usr/bin/env python3
import sys
import rospy
import time 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from qt_gui_main import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    # 初始化程序
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.InitTimer()
        self.btn_select.clicked.connect(self.gBox_location_window)
        self.btn_find.clicked.connect(self.gBox_book_window)
        self.gBox_location.hide()
        self.gBox_book.hide()
    # 打开选座group窗口
    def gBox_location_window(self):
        self.gBox_book.hide()
        self.gBox_location.show()
    # 打开查找书籍group窗口
    def gBox_book_window(self):
        self.gBox_location.hide()
        self.gBox_book.show()
    # 初始化时钟，每一秒刷新时间
    def InitTimer(self):
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.showTime)
    # 在label_time上显示时间
    def showTime(self):
        self.label_time.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec_())
