# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 679)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(40, 30, 791, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(700, 230, 160, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_select.setDefault(False)
        self.btn_select.setObjectName("btn_select")
        self.verticalLayout.addWidget(self.btn_select)
        self.btn_book = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_book.setObjectName("btn_book")
        self.verticalLayout.addWidget(self.btn_book)
        self.btn_robot_state = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_robot_state.setObjectName("btn_robot_state")
        self.verticalLayout.addWidget(self.btn_robot_state)
        self.btn_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(590, 100, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_time.setFont(font)
        self.label_time.setText("")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.gBox_location = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_location.setEnabled(True)
        self.gBox_location.setGeometry(QtCore.QRect(9, 160, 671, 511))
        self.gBox_location.setMouseTracking(False)
        self.gBox_location.setTabletTracking(False)
        self.gBox_location.setAutoFillBackground(True)
        self.gBox_location.setFlat(False)
        self.gBox_location.setCheckable(False)
        self.gBox_location.setObjectName("gBox_location")
        self.btn_select_ok = QtWidgets.QPushButton(self.gBox_location)
        self.btn_select_ok.setGeometry(QtCore.QRect(560, 440, 111, 51))
        self.btn_select_ok.setObjectName("btn_select_ok")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 50, 21, 63))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_1.setText("")
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_2.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(90, 50, 21, 63))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_3.addWidget(self.checkBox_4)
        self.label = QtWidgets.QLabel(self.gBox_location)
        self.label.setGeometry(QtCore.QRect(-1, 30, 681, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("volcano_robot_map_1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 130, 21, 63))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_4.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_4.addWidget(self.checkBox_6)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(90, 130, 122, 97))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_7 = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_5.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.verticalLayoutWidget_5)
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_5.addWidget(self.checkBox_8)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(160, 50, 21, 63))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_9 = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_6.addWidget(self.checkBox_9)
        self.checkBox_10 = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_6.addWidget(self.checkBox_10)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(210, 50, 21, 63))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkBox_11 = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_11.setText("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout_7.addWidget(self.checkBox_11)
        self.checkBox_12 = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.checkBox_12.setText("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_7.addWidget(self.checkBox_12)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(160, 130, 21, 63))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox_13 = QtWidgets.QCheckBox(self.verticalLayoutWidget_8)
        self.checkBox_13.setText("")
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_8.addWidget(self.checkBox_13)
        self.checkBox_14 = QtWidgets.QCheckBox(self.verticalLayoutWidget_8)
        self.checkBox_14.setText("")
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout_8.addWidget(self.checkBox_14)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(210, 130, 21, 63))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_15 = QtWidgets.QCheckBox(self.verticalLayoutWidget_9)
        self.checkBox_15.setText("")
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout_9.addWidget(self.checkBox_15)
        self.checkBox_16 = QtWidgets.QCheckBox(self.verticalLayoutWidget_9)
        self.checkBox_16.setText("")
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_9.addWidget(self.checkBox_16)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(470, 40, 112, 171))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBox_17 = QtWidgets.QCheckBox(self.verticalLayoutWidget_10)
        self.checkBox_17.setText("")
        self.checkBox_17.setObjectName("checkBox_17")
        self.verticalLayout_10.addWidget(self.checkBox_17)
        self.checkBox_18 = QtWidgets.QCheckBox(self.verticalLayoutWidget_10)
        self.checkBox_18.setText("")
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout_10.addWidget(self.checkBox_18)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(550, 40, 112, 171))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.checkBox_19 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.checkBox_19.setText("")
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout_11.addWidget(self.checkBox_19)
        self.checkBox_20 = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.checkBox_20.setText("")
        self.checkBox_20.setObjectName("checkBox_20")
        self.verticalLayout_11.addWidget(self.checkBox_20)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(630, 80, 112, 95))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.checkBox_21 = QtWidgets.QCheckBox(self.verticalLayoutWidget_12)
        self.checkBox_21.setText("")
        self.checkBox_21.setObjectName("checkBox_21")
        self.verticalLayout_12.addWidget(self.checkBox_21)
        self.checkBox_22 = QtWidgets.QCheckBox(self.verticalLayoutWidget_12)
        self.checkBox_22.setText("")
        self.checkBox_22.setObjectName("checkBox_22")
        self.verticalLayout_12.addWidget(self.checkBox_22)
        self.checkBox_23 = QtWidgets.QCheckBox(self.verticalLayoutWidget_12)
        self.checkBox_23.setText("")
        self.checkBox_23.setObjectName("checkBox_23")
        self.verticalLayout_12.addWidget(self.checkBox_23)
        self.checkBox_24 = QtWidgets.QCheckBox(self.verticalLayoutWidget_12)
        self.checkBox_24.setText("")
        self.checkBox_24.setObjectName("checkBox_24")
        self.verticalLayout_12.addWidget(self.checkBox_24)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(30, 200, 21, 95))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.checkBox_25 = QtWidgets.QCheckBox(self.verticalLayoutWidget_13)
        self.checkBox_25.setText("")
        self.checkBox_25.setObjectName("checkBox_25")
        self.verticalLayout_13.addWidget(self.checkBox_25)
        self.checkBox_26 = QtWidgets.QCheckBox(self.verticalLayoutWidget_13)
        self.checkBox_26.setText("")
        self.checkBox_26.setObjectName("checkBox_26")
        self.verticalLayout_13.addWidget(self.checkBox_26)
        self.checkBox_27 = QtWidgets.QCheckBox(self.verticalLayoutWidget_13)
        self.checkBox_27.setText("")
        self.checkBox_27.setObjectName("checkBox_27")
        self.verticalLayout_13.addWidget(self.checkBox_27)
        self.checkBox_28 = QtWidgets.QCheckBox(self.verticalLayoutWidget_13)
        self.checkBox_28.setText("")
        self.checkBox_28.setObjectName("checkBox_28")
        self.verticalLayout_13.addWidget(self.checkBox_28)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.gBox_location)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(30, 310, 21, 95))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.checkBox_29 = QtWidgets.QCheckBox(self.verticalLayoutWidget_14)
        self.checkBox_29.setText("")
        self.checkBox_29.setObjectName("checkBox_29")
        self.verticalLayout_14.addWidget(self.checkBox_29)
        self.checkBox_30 = QtWidgets.QCheckBox(self.verticalLayoutWidget_14)
        self.checkBox_30.setText("")
        self.checkBox_30.setObjectName("checkBox_30")
        self.verticalLayout_14.addWidget(self.checkBox_30)
        self.checkBox_31 = QtWidgets.QCheckBox(self.verticalLayoutWidget_14)
        self.checkBox_31.setText("")
        self.checkBox_31.setObjectName("checkBox_31")
        self.verticalLayout_14.addWidget(self.checkBox_31)
        self.checkBox_32 = QtWidgets.QCheckBox(self.verticalLayoutWidget_14)
        self.checkBox_32.setText("")
        self.checkBox_32.setObjectName("checkBox_32")
        self.verticalLayout_14.addWidget(self.checkBox_32)
        self.label.raise_()
        self.btn_select_ok.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.verticalLayoutWidget_6.raise_()
        self.verticalLayoutWidget_7.raise_()
        self.verticalLayoutWidget_8.raise_()
        self.verticalLayoutWidget_9.raise_()
        self.verticalLayoutWidget_10.raise_()
        self.verticalLayoutWidget_11.raise_()
        self.verticalLayoutWidget_12.raise_()
        self.verticalLayoutWidget_13.raise_()
        self.verticalLayoutWidget_14.raise_()
        self.gBox_book = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_book.setGeometry(QtCore.QRect(10, 160, 671, 511))
        self.gBox_book.setAutoFillBackground(True)
        self.gBox_book.setObjectName("gBox_book")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.gBox_book)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(16, 30, 631, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_book = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_book.setObjectName("lineEdit_book")
        self.horizontalLayout.addWidget(self.lineEdit_book)
        self.btn_robot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_robot.setObjectName("btn_robot")
        self.horizontalLayout.addWidget(self.btn_robot)
        self.webView = QtWebEngineWidgets.QWebEngineView(self.gBox_book)
        self.webView.setGeometry(QtCore.QRect(9, 89, 651, 411))
        self.webView.setUrl(QtCore.QUrl("http://p-8080.10.28.60.4.vpn.lib.cslg.edu.cn/opac/search_adv.php#/index"))
        self.webView.setObjectName("webView")
        self.gBox_robot = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_robot.setGeometry(QtCore.QRect(10, 160, 671, 511))
        self.gBox_robot.setTabletTracking(False)
        self.gBox_robot.setAcceptDrops(False)
        self.gBox_robot.setAutoFillBackground(True)
        self.gBox_robot.setObjectName("gBox_robot")
        self.groupBox = QtWidgets.QGroupBox(self.gBox_robot)
        self.groupBox.setGeometry(QtCore.QRect(340, 30, 321, 231))
        self.groupBox.setObjectName("groupBox")
        self.btn_control_qj = QtWidgets.QPushButton(self.groupBox)
        self.btn_control_qj.setGeometry(QtCore.QRect(120, 30, 91, 30))
        self.btn_control_qj.setObjectName("btn_control_qj")
        self.btn_control_yz = QtWidgets.QPushButton(self.groupBox)
        self.btn_control_yz.setGeometry(QtCore.QRect(210, 70, 91, 30))
        self.btn_control_yz.setObjectName("btn_control_yz")
        self.btn_control_ht = QtWidgets.QPushButton(self.groupBox)
        self.btn_control_ht.setGeometry(QtCore.QRect(120, 110, 91, 30))
        self.btn_control_ht.setObjectName("btn_control_ht")
        self.btn_control_zz = QtWidgets.QPushButton(self.groupBox)
        self.btn_control_zz.setGeometry(QtCore.QRect(30, 70, 91, 30))
        self.btn_control_zz.setObjectName("btn_control_zz")
        self.btn_control_tz = QtWidgets.QPushButton(self.groupBox)
        self.btn_control_tz.setGeometry(QtCore.QRect(120, 70, 91, 30))
        self.btn_control_tz.setAutoDefault(False)
        self.btn_control_tz.setDefault(False)
        self.btn_control_tz.setObjectName("btn_control_tz")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 150, 301, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.h_slider_linear = QtWidgets.QSlider(self.gridLayoutWidget)
        self.h_slider_linear.setOrientation(QtCore.Qt.Horizontal)
        self.h_slider_linear.setObjectName("h_slider_linear")
        self.gridLayout.addWidget(self.h_slider_linear, 1, 1, 1, 1)
        self.h_slider_angular = QtWidgets.QSlider(self.gridLayoutWidget)
        self.h_slider_angular.setMaximum(99)
        self.h_slider_angular.setSingleStep(1)
        self.h_slider_angular.setProperty("value", 0)
        self.h_slider_angular.setOrientation(QtCore.Qt.Horizontal)
        self.h_slider_angular.setObjectName("h_slider_angular")
        self.gridLayout.addWidget(self.h_slider_angular, 0, 1, 1, 1)
        self.label_angular_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_angular_val.setObjectName("label_angular_val")
        self.gridLayout.addWidget(self.label_angular_val, 0, 2, 1, 1)
        self.label_linear_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_linear_val.setObjectName("label_linear_val")
        self.gridLayout.addWidget(self.label_linear_val, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gBox_robot)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 260, 321, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 301, 79))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_point_x = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_point_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_point_x.setObjectName("label_point_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_point_x)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_point_y = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_point_y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_point_y.setObjectName("label_point_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_point_y)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_point_z = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_point_z.setAlignment(QtCore.Qt.AlignCenter)
        self.label_point_z.setObjectName("label_point_z")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_point_z)
        self.groupBox_3 = QtWidgets.QGroupBox(self.gBox_robot)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 30, 321, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphicsView.setGeometry(QtCore.QRect(5, 31, 311, 191))
        self.graphicsView.setObjectName("graphicsView")
        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setGeometry(QtCore.QRect(111, 91, 334, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_class.setFont(font)
        self.label_class.setAlignment(QtCore.Qt.AlignCenter)
        self.label_class.setObjectName("label_class")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(111, 124, 334, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_title.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_time.raise_()
        self.label_class.raise_()
        self.label_name.raise_()
        self.gBox_book.raise_()
        self.gBox_location.raise_()
        self.gBox_robot.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图书馆导航服务和书籍管理机器人系统平台"))
        self.label_title.setText(_translate("MainWindow", "图书馆导航服务和书籍管理机器人系统平台"))
        self.btn_select.setText(_translate("MainWindow", "位置选座"))
        self.btn_book.setText(_translate("MainWindow", "查找书籍"))
        self.btn_robot_state.setText(_translate("MainWindow", "机器人状态"))
        self.btn_exit.setText(_translate("MainWindow", "退出系统"))
        self.gBox_location.setTitle(_translate("MainWindow", "位置选座"))
        self.btn_select_ok.setText(_translate("MainWindow", "确定"))
        self.gBox_book.setTitle(_translate("MainWindow", "查找书籍"))
        self.label_4.setText(_translate("MainWindow", "索书号："))
        self.btn_robot.setText(_translate("MainWindow", "机器人引导"))
        self.gBox_robot.setTitle(_translate("MainWindow", "机器人状态"))
        self.groupBox.setTitle(_translate("MainWindow", "基础控制"))
        self.btn_control_qj.setText(_translate("MainWindow", "前进"))
        self.btn_control_yz.setText(_translate("MainWindow", "右转"))
        self.btn_control_ht.setText(_translate("MainWindow", "后退"))
        self.btn_control_zz.setText(_translate("MainWindow", "左转"))
        self.btn_control_tz.setText(_translate("MainWindow", "停止"))
        self.label_5.setText(_translate("MainWindow", "线速度："))
        self.label_2.setText(_translate("MainWindow", "角速度:"))
        self.label_angular_val.setText(_translate("MainWindow", "0.0"))
        self.label_linear_val.setText(_translate("MainWindow", "0.0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GPS定位"))
        self.label_7.setText(_translate("MainWindow", "Point.X:"))
        self.label_point_x.setText(_translate("MainWindow", "NA"))
        self.label_9.setText(_translate("MainWindow", "Point.Y:"))
        self.label_point_y.setText(_translate("MainWindow", "NA"))
        self.label_11.setText(_translate("MainWindow", "Point.Z:"))
        self.label_point_z.setText(_translate("MainWindow", "NA"))
        self.groupBox_3.setTitle(_translate("MainWindow", "视频"))
        self.label_class.setText(_translate("MainWindow", "电气工程及其自动化(单招)171"))
        self.label_name.setText(_translate("MainWindow", "毛成凯"))
from PyQt5 import QtWebEngineWidgets