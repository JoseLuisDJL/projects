# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceziugJv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(536, 564)
        MainWindow.setStyleSheet(u"*{ \n"
"	border:none;\n"
"}\n"
"QProgressBar{\n"
"	background-color : rgb(20,30,43);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-aling:center;\n"
"	color:rgb(255,0,0)\n"
"}\n"
"QProgressBar::chunk{\n"
"	backgorund-color:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0\n"
"stop:0 rgba(0,136,255,255),stop:1 rgba(255,255,255,255));\n"
"	border-radius:10px\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.header_left_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.open_close_side_bar_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon/feather/align-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setPixmap(QPixmap(u":/icons/icon/feather/airplay.png"))

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)

        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_night_frame = QFrame(self.header_frame)
        self.header_night_frame.setObjectName(u"header_night_frame")
        self.header_night_frame.setFrameShape(QFrame.StyledPanel)
        self.header_night_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_night_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_night_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/feather/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_night_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/feather/minimize (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_night_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/feather/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_night_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_count_frame = QFrame(self.main_body_frame)
        self.left_menu_count_frame.setObjectName(u"left_menu_count_frame")
        self.left_menu_count_frame.setMinimumSize(QSize(60, 0))
        self.left_menu_count_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_count_frame.setStyleSheet(u"background-color: rgb(85, 85, 127);")
        self.left_menu_count_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_count_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_count_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_count_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setEnabled(True)
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.menu_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, -1)
        self.cpu_btn = QPushButton(self.menu_frame)
        self.cpu_btn.setObjectName(u"cpu_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/feather/cpu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_btn.setIcon(icon4)
        self.cpu_btn.setIconSize(QSize(32, 32))

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.cpu_btn)

        self.battery_btn = QPushButton(self.menu_frame)
        self.battery_btn.setObjectName(u"battery_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/feather/bateria.png", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_btn.setIcon(icon5)
        self.battery_btn.setIconSize(QSize(32, 32))

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.battery_btn)

        self.activity_btn = QPushButton(self.menu_frame)
        self.activity_btn.setObjectName(u"activity_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/feather/monitor-de-ecg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_btn.setIcon(icon6)
        self.activity_btn.setIconSize(QSize(32, 32))

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.activity_btn)

        self.storage_btn = QPushButton(self.menu_frame)
        self.storage_btn.setObjectName(u"storage_btn")
        self.storage_btn.setEnabled(True)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icon/feather/server-storage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_btn.setIcon(icon7)
        self.storage_btn.setIconSize(QSize(32, 32))

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.storage_btn)

        self.sensors_page_btn = QPushButton(self.menu_frame)
        self.sensors_page_btn.setObjectName(u"sensors_page_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icon/feather/temperature-reader - copia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_page_btn.setIcon(icon8)
        self.sensors_page_btn.setIconSize(QSize(32, 32))

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.sensors_page_btn)

        self.networks_page_btn = QPushButton(self.menu_frame)
        self.networks_page_btn.setObjectName(u"networks_page_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icon/feather/signal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.networks_page_btn.setIcon(icon9)
        self.networks_page_btn.setIconSize(QSize(32, 32))

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.networks_page_btn)

        self.system_info_btn = QPushButton(self.menu_frame)
        self.system_info_btn.setObjectName(u"system_info_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icon/feather/monitor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.system_info_btn.setIcon(icon10)
        self.system_info_btn.setIconSize(QSize(32, 32))

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.system_info_btn)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMargin(5)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_4)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_5)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(5)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.label_6)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(5)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.label_7)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMargin(5)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.label_8)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(5)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.label_9)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMargin(5)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.label_10)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_count_frame)

        self.main_body_content = QFrame(self.main_body_frame)
        self.main_body_content.setObjectName(u"main_body_content")
        self.main_body_content.setStyleSheet(u"background-color: rgb(52, 52, 77);")
        self.main_body_content.setFrameShape(QFrame.StyledPanel)
        self.main_body_content.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.main_body_content)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget = QStackedWidget(self.main_body_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_3 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cpu_info = QFrame(self.cpu_and_memory)
        self.cpu_info.setObjectName(u"cpu_info")
        self.cpu_info.setFrameShape(QFrame.StyledPanel)
        self.cpu_info.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.cpu_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cpu_count = QLabel(self.cpu_info)
        self.cpu_count.setObjectName(u"cpu_count")

        self.gridLayout.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.cpu_usage = roundProgressBar(self.cpu_info)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setMinimumSize(QSize(150, 150))

        self.gridLayout.addWidget(self.cpu_usage, 0, 2, 3, 1)

        self.cpu_main = QLabel(self.cpu_info)
        self.cpu_main.setObjectName(u"cpu_main")

        self.gridLayout.addWidget(self.cpu_main, 2, 1, 1, 1)

        self.label_12 = QLabel(self.cpu_info)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_11 = QLabel(self.cpu_info)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.cpu_per = QLabel(self.cpu_info)
        self.cpu_per.setObjectName(u"cpu_per")

        self.gridLayout.addWidget(self.cpu_per, 1, 1, 1, 1)

        self.label_13 = QLabel(self.cpu_info)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.cpu_info)

        self.ram_info = QFrame(self.cpu_and_memory)
        self.ram_info.setObjectName(u"ram_info")
        self.ram_info.setFrameShape(QFrame.StyledPanel)
        self.ram_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.ram_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_21 = QLabel(self.ram_info)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 4, 0, 1, 1)

        self.label_20 = QLabel(self.ram_info)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 3, 0, 1, 1)

        self.free_ram = QLabel(self.ram_info)
        self.free_ram.setObjectName(u"free_ram")

        self.gridLayout_2.addWidget(self.free_ram, 3, 1, 1, 1)

        self.used_ram = QLabel(self.ram_info)
        self.used_ram.setObjectName(u"used_ram")

        self.gridLayout_2.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_17 = QLabel(self.ram_info)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)

        self.available_ram = QLabel(self.ram_info)
        self.available_ram.setObjectName(u"available_ram")

        self.gridLayout_2.addWidget(self.available_ram, 1, 1, 1, 1)

        self.label_19 = QLabel(self.ram_info)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)

        self.usage_ram = QLabel(self.ram_info)
        self.usage_ram.setObjectName(u"usage_ram")

        self.gridLayout_2.addWidget(self.usage_ram, 4, 1, 1, 1)

        self.total_ram = QLabel(self.ram_info)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_2.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_18 = QLabel(self.ram_info)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)

        self.ram_usage = spiralProgressBar(self.ram_info)
        self.ram_usage.setObjectName(u"ram_usage")
        self.ram_usage.setMinimumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.ram_usage, 0, 2, 5, 1)


        self.verticalLayout_3.addWidget(self.ram_info)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.gridLayout_4 = QGridLayout(self.battery)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_27 = QLabel(self.battery)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.gridLayout_4.addWidget(self.label_27, 0, 0, 1, 1, Qt.AlignBottom)

        self.frame = QFrame(self.battery)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_3.addWidget(self.label_31, 3, 0, 1, 1)

        self.battery_status = QLabel(self.frame)
        self.battery_status.setObjectName(u"battery_status")

        self.gridLayout_3.addWidget(self.battery_status, 0, 1, 1, 1)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_3.addWidget(self.label_30, 2, 0, 1, 1)

        self.battery_charge = QLabel(self.frame)
        self.battery_charge.setObjectName(u"battery_charge")

        self.gridLayout_3.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.battery_time_left = QLabel(self.frame)
        self.battery_time_left.setObjectName(u"battery_time_left")

        self.gridLayout_3.addWidget(self.battery_time_left, 2, 1, 1, 1)

        self.battery_plugged = QLabel(self.frame)
        self.battery_plugged.setObjectName(u"battery_plugged")

        self.gridLayout_3.addWidget(self.battery_plugged, 3, 1, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 1, 0, 1, 1)

        self.battery_usage = roundProgressBar(self.frame)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(150, 150))
        self.battery_usage.setMaximumSize(QSize(150, 150))

        self.gridLayout_3.addWidget(self.battery_usage, 0, 2, 4, 1)


        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.battery)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_2 = QVBoxLayout(self.system_information)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.system_information)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.system_date = QLabel(self.frame_2)
        self.system_date.setObjectName(u"system_date")

        self.gridLayout_6.addWidget(self.system_date, 4, 1, 1, 1)

        self.label_50 = QLabel(self.frame_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.gridLayout_6.addWidget(self.label_50, 3, 2, 1, 1)

        self.platform = QLabel(self.frame_2)
        self.platform.setObjectName(u"platform")

        self.gridLayout_6.addWidget(self.platform, 2, 1, 1, 1)

        self.label_48 = QLabel(self.frame_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.gridLayout_6.addWidget(self.label_48, 2, 2, 1, 1)

        self.label_36 = QLabel(self.frame_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.gridLayout_6.addWidget(self.label_36, 0, 0, 1, 1)

        self.systemy_information = QLabel(self.frame_2)
        self.systemy_information.setObjectName(u"systemy_information")

        self.gridLayout_6.addWidget(self.systemy_information, 1, 0, 1, 1)

        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)

        self.gridLayout_6.addWidget(self.label_39, 3, 0, 1, 1)

        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)

        self.gridLayout_6.addWidget(self.label_40, 4, 0, 1, 1)

        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.gridLayout_6.addWidget(self.label_38, 2, 0, 1, 1)

        self.label_49 = QLabel(self.frame_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)

        self.gridLayout_6.addWidget(self.label_49, 4, 2, 1, 1)

        self.version = QLabel(self.frame_2)
        self.version.setObjectName(u"version")

        self.gridLayout_6.addWidget(self.version, 3, 1, 1, 1)

        self.processor = QLabel(self.frame_2)
        self.processor.setObjectName(u"processor")

        self.gridLayout_6.addWidget(self.processor, 2, 3, 1, 1)

        self.machine = QLabel(self.frame_2)
        self.machine.setObjectName(u"machine")

        self.gridLayout_6.addWidget(self.machine, 3, 3, 1, 1)

        self.system_time = QLabel(self.frame_2)
        self.system_time.setObjectName(u"system_time")

        self.gridLayout_6.addWidget(self.system_time, 4, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.system_information)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_4 = QVBoxLayout(self.activities)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.activities)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_47 = QLabel(self.frame_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_47)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.activity_search = QLineEdit(self.frame_6)
        self.activity_search.setObjectName(u"activity_search")

        self.horizontalLayout_11.addWidget(self.activity_search)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icon/feather/compass-32x32-434015.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon11)

        self.horizontalLayout_11.addWidget(self.pushButton_3)


        self.horizontalLayout_10.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.activities)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_12.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_12.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_12.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_12.addWidget(self.pushButton_7)


        self.verticalLayout_4.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_6 = QVBoxLayout(self.storage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_51 = QLabel(self.storage)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.verticalLayout_6.addWidget(self.label_51)

        self.storage_table = QTableWidget(self.storage)
        if (self.storage_table.columnCount() < 10):
            self.storage_table.setColumnCount(10)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        self.storage_table.setObjectName(u"storage_table")

        self.verticalLayout_6.addWidget(self.storage_table)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_7 = QVBoxLayout(self.sensors)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_52 = QLabel(self.sensors)
        self.label_52.setObjectName(u"label_52")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_52.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_52)

        self.tableWidget_3 = QTableWidget(self.sensors)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_7.addWidget(self.tableWidget_3)

        self.stackedWidget.addWidget(self.sensors)
        self.networks = QWidget()
        self.networks.setObjectName(u"networks")
        self.verticalLayout_8 = QVBoxLayout(self.networks)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea = QScrollArea(self.networks)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 423, 448))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_53 = QLabel(self.frame_7)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_53)

        self.net_stats_table = QTableWidget(self.frame_7)
        if (self.net_stats_table.columnCount() < 5):
            self.net_stats_table.setColumnCount(5)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        self.net_stats_table.setObjectName(u"net_stats_table")

        self.verticalLayout_10.addWidget(self.net_stats_table)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_54 = QLabel(self.frame_8)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_54)

        self.net_io_table = QTableWidget(self.frame_8)
        if (self.net_io_table.columnCount() < 9):
            self.net_io_table.setColumnCount(9)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(8, __qtablewidgetitem37)
        self.net_io_table.setObjectName(u"net_io_table")

        self.verticalLayout_11.addWidget(self.net_io_table)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_55 = QLabel(self.frame_9)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_55)

        self.net_addresses_table = QTableWidget(self.frame_9)
        if (self.net_addresses_table.columnCount() < 6):
            self.net_addresses_table.setColumnCount(6)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        self.net_addresses_table.setObjectName(u"net_addresses_table")

        self.verticalLayout_12.addWidget(self.net_addresses_table)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_56 = QLabel(self.frame_10)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_56)

        self.net_connections_table = QTableWidget(self.frame_10)
        if (self.net_connections_table.columnCount() < 7):
            self.net_connections_table.setColumnCount(7)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(6, __qtablewidgetitem50)
        self.net_connections_table.setObjectName(u"net_connections_table")

        self.verticalLayout_13.addWidget(self.net_connections_table)


        self.verticalLayout_9.addWidget(self.frame_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.main_body_content)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(52, 52, 77);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PSU UTIL MANAGER", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.cpu_btn.setText("")
        self.battery_btn.setText("")
        self.activity_btn.setText("")
        self.storage_btn.setText("")
        self.sensors_page_btn.setText("")
        self.networks_page_btn.setText("")
        self.system_info_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_main.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CPU Cout", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU Main", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.usage_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Avialable RAM", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.systemy_information.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"System time", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.pushButton_3.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Disk Partition", None))
        ___qtablewidgetitem8 = self.storage_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem9 = self.storage_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem10 = self.storage_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem11 = self.storage_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"MAX", None));
        ___qtablewidgetitem12 = self.storage_table.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Max File", None));
        ___qtablewidgetitem13 = self.storage_table.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem14 = self.storage_table.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem15 = self.storage_table.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem16 = self.storage_table.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Free Storage", None));
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem21 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem22 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem23 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem24 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem25 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Network IO Counters", None))
        ___qtablewidgetitem26 = self.net_io_table.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem27 = self.net_io_table.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None));
        ___qtablewidgetitem28 = self.net_io_table.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Bytes Receive", None));
        ___qtablewidgetitem29 = self.net_io_table.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Packets Sent", None));
        ___qtablewidgetitem30 = self.net_io_table.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Packets Recieved", None));
        ___qtablewidgetitem31 = self.net_io_table.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERR In ", None));
        ___qtablewidgetitem32 = self.net_io_table.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ERR Out", None));
        ___qtablewidgetitem33 = self.net_io_table.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem34 = self.net_io_table.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem35 = self.net_addresses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem36 = self.net_addresses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem37 = self.net_addresses_table.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem38 = self.net_addresses_table.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Roadcast", None));
        ___qtablewidgetitem39 = self.net_addresses_table.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem40 = self.net_connections_table.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem41 = self.net_connections_table.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem42 = self.net_connections_table.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem43 = self.net_connections_table.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Laddr", None));
        ___qtablewidgetitem44 = self.net_connections_table.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Raddr", None));
        ___qtablewidgetitem45 = self.net_connections_table.horizontalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem46 = self.net_connections_table.horizontalHeaderItem(6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0| Copyright Debugger Co.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

