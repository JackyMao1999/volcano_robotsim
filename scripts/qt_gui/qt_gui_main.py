# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(-1, 0, 801, 601))
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("mainwindows.jpg"))
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 20, 791, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(590, 200, 160, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_select.setDefault(False)
        self.btn_select.setObjectName("btn_select")
        self.verticalLayout.addWidget(self.btn_select)
        self.btn_find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_find.setObjectName("btn_find")
        self.verticalLayout.addWidget(self.btn_find)
        self.btn_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(260, 100, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_time.setFont(font)
        self.label_time.setText("")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.gBox_location = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_location.setEnabled(True)
        self.gBox_location.setGeometry(QtCore.QRect(9, 149, 561, 431))
        self.gBox_location.setMouseTracking(False)
        self.gBox_location.setTabletTracking(False)
        self.gBox_location.setAutoFillBackground(True)
        self.gBox_location.setFlat(False)
        self.gBox_location.setCheckable(False)
        self.gBox_location.setObjectName("gBox_location")
        self.gBox_book = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_book.setGeometry(QtCore.QRect(10, 150, 561, 431))
        self.gBox_book.setAutoFillBackground(True)
        self.gBox_book.setObjectName("gBox_book")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "图书馆导航服务和书籍管理机器人系统平台"))
        self.btn_select.setText(_translate("MainWindow", "位置选座"))
        self.btn_find.setText(_translate("MainWindow", "查找书籍"))
        self.btn_exit.setText(_translate("MainWindow", "退出系统"))
        self.gBox_location.setTitle(_translate("MainWindow", "位置选座"))
        self.gBox_book.setTitle(_translate("MainWindow", "查找书籍"))

