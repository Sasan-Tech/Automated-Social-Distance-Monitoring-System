# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trying.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 803)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(90, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Montserrat Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255); border: 0px solid;")
        icon = QIcon()
        icon.addFile(u"images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setMaximumSize(QSize(16777215, 16777215))
        self.Content.setStyleSheet(u"")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(90, 0))
        self.frame_left_menu.setMaximumSize(QSize(90, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_Menu_1 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_1.setObjectName(u"Btn_Menu_1")
        self.Btn_Menu_1.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(10)
        self.Btn_Menu_1.setFont(font1)
        self.Btn_Menu_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Menu_1)

        self.Btn_Menu_2 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setObjectName(u"Btn_Menu_2")
        self.Btn_Menu_2.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_2.setFont(font1)
        self.Btn_Menu_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Menu_2)

        self.Btn_Menu_3 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_3.setObjectName(u"Btn_Menu_3")
        self.Btn_Menu_3.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_3.setFont(font1)
        self.Btn_Menu_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_Menu_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        font2 = QFont()
        font2.setPointSize(30)
        self.Pages_Widget.setFont(font2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_images = QFrame(self.page)
        self.frame_images.setObjectName(u"frame_images")
        self.frame_images.setMinimumSize(QSize(0, 0))
        self.frame_images.setMaximumSize(QSize(16777215, 500))
        self.frame_images.setFrameShape(QFrame.NoFrame)
        self.frame_images.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_images)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.result_image = QLabel(self.frame_images)
        self.result_image.setObjectName(u"result_image")

        self.horizontalLayout_6.addWidget(self.result_image)

        self.default_image = QLabel(self.frame_images)
        self.default_image.setObjectName(u"default_image")

        self.horizontalLayout_6.addWidget(self.default_image)


        self.verticalLayout_6.addWidget(self.frame_images)

        self.extension_image_result_section = QFrame(self.page)
        self.extension_image_result_section.setObjectName(u"extension_image_result_section")
        self.extension_image_result_section.setMaximumSize(QSize(16777215, 500))
        self.extension_image_result_section.setFrameShape(QFrame.NoFrame)
        self.extension_image_result_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.extension_image_result_section)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.centroid_image_result = QLabel(self.extension_image_result_section)
        self.centroid_image_result.setObjectName(u"centroid_image_result")

        self.horizontalLayout_8.addWidget(self.centroid_image_result)


        self.verticalLayout_6.addWidget(self.extension_image_result_section)

        self.button_section = QFrame(self.page)
        self.button_section.setObjectName(u"button_section")
        self.button_section.setMaximumSize(QSize(16777215, 200))
        self.button_section.setFrameShape(QFrame.NoFrame)
        self.button_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.button_section)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.upload_image_section = QFrame(self.button_section)
        self.upload_image_section.setObjectName(u"upload_image_section")
        self.upload_image_section.setFrameShape(QFrame.StyledPanel)
        self.upload_image_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.upload_image_section)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.upload_image_button = QPushButton(self.upload_image_section)
        self.upload_image_button.setObjectName(u"upload_image_button")
        self.upload_image_button.setMaximumSize(QSize(500, 50))
        font3 = QFont()
        font3.setFamily(u"Montserrat")
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setWeight(75)
        self.upload_image_button.setFont(font3)
        self.upload_image_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.upload_image_button)

        self.pushButton_2 = QPushButton(self.upload_image_section)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(500, 50))
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout_8.addWidget(self.upload_image_section)

        self.model_button_section = QFrame(self.button_section)
        self.model_button_section.setObjectName(u"model_button_section")
        self.model_button_section.setFrameShape(QFrame.NoFrame)
        self.model_button_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.model_button_section)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.model_2 = QPushButton(self.model_button_section)
        self.model_2.setObjectName(u"model_2")
        self.model_2.setMaximumSize(QSize(400, 40))
        font4 = QFont()
        font4.setFamily(u"Montserrat")
        font4.setBold(True)
        font4.setWeight(75)
        self.model_2.setFont(font4)
        self.model_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.model_2)

        self.model_1 = QPushButton(self.model_button_section)
        self.model_1.setObjectName(u"model_1")
        self.model_1.setMaximumSize(QSize(400, 40))
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.model_1.setFont(font5)
        self.model_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.model_1)

        self.model_3 = QPushButton(self.model_button_section)
        self.model_3.setObjectName(u"model_3")
        self.model_3.setMaximumSize(QSize(400, 40))
        self.model_3.setFont(font5)
        self.model_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.model_3)


        self.verticalLayout_8.addWidget(self.model_button_section)


        self.verticalLayout_6.addWidget(self.button_section)

        self.Pages_Widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 6)
        self.videoWidget = QWidget(self.page_2)
        self.videoWidget.setObjectName(u"videoWidget")

        self.verticalLayout_7.addWidget(self.videoWidget)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.play_button = QPushButton(self.frame)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setMaximumSize(QSize(50, 50))
        self.play_button.setStyleSheet(u"QPushButton {\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QSize(15, 15))

        self.horizontalLayout_5.addWidget(self.play_button)

        self.video_slider = QSlider(self.frame)
        self.video_slider.setObjectName(u"video_slider")
        self.video_slider.setMaximumSize(QSize(800, 16777215))
        self.video_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.video_slider)


        self.verticalLayout_7.addWidget(self.frame)

        self.video_button_section = QFrame(self.page_2)
        self.video_button_section.setObjectName(u"video_button_section")
        self.video_button_section.setMaximumSize(QSize(16777215, 80))
        self.video_button_section.setFrameShape(QFrame.StyledPanel)
        self.video_button_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.video_button_section)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.VideoButton = QPushButton(self.video_button_section)
        self.VideoButton.setObjectName(u"VideoButton")
        self.VideoButton.setMaximumSize(QSize(500, 50))
        self.VideoButton.setFont(font3)
        self.VideoButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.VideoButton)


        self.verticalLayout_7.addWidget(self.video_button_section)

        self.Pages_Widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.analyze_video_result_section = QFrame(self.page_3)
        self.analyze_video_result_section.setObjectName(u"analyze_video_result_section")
        self.analyze_video_result_section.setFrameShape(QFrame.NoFrame)
        self.analyze_video_result_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.analyze_video_result_section)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.analyze_default_video = QLabel(self.analyze_video_result_section)
        self.analyze_default_video.setObjectName(u"analyze_default_video")

        self.horizontalLayout_9.addWidget(self.analyze_default_video)

        self.analyze_line_graph_video = QLabel(self.analyze_video_result_section)
        self.analyze_line_graph_video.setObjectName(u"analyze_line_graph_video")

        self.horizontalLayout_9.addWidget(self.analyze_line_graph_video)

        self.analyze_masking_video = QLabel(self.analyze_video_result_section)
        self.analyze_masking_video.setObjectName(u"analyze_masking_video")

        self.horizontalLayout_9.addWidget(self.analyze_masking_video)


        self.verticalLayout_9.addWidget(self.analyze_video_result_section)

        self.analyze_button_section = QFrame(self.page_3)
        self.analyze_button_section.setObjectName(u"analyze_button_section")
        self.analyze_button_section.setMaximumSize(QSize(16777215, 200))
        self.analyze_button_section.setFrameShape(QFrame.NoFrame)
        self.analyze_button_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.analyze_button_section)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.analyze_button_sectionn1 = QFrame(self.analyze_button_section)
        self.analyze_button_sectionn1.setObjectName(u"analyze_button_sectionn1")
        self.analyze_button_sectionn1.setFrameShape(QFrame.StyledPanel)
        self.analyze_button_sectionn1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.analyze_button_sectionn1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.analyze_upload_video_button = QPushButton(self.analyze_button_sectionn1)
        self.analyze_upload_video_button.setObjectName(u"analyze_upload_video_button")
        self.analyze_upload_video_button.setMaximumSize(QSize(500, 50))
        font6 = QFont()
        font6.setFamily(u"Montserrat")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.analyze_upload_video_button.setFont(font6)
        self.analyze_upload_video_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.analyze_upload_video_button)


        self.verticalLayout_10.addWidget(self.analyze_button_sectionn1)

        self.analyze_button_section2 = QFrame(self.analyze_button_section)
        self.analyze_button_section2.setObjectName(u"analyze_button_section2")
        self.analyze_button_section2.setFrameShape(QFrame.StyledPanel)
        self.analyze_button_section2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.analyze_button_section2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.analyze_model1 = QPushButton(self.analyze_button_section2)
        self.analyze_model1.setObjectName(u"analyze_model1")
        self.analyze_model1.setMaximumSize(QSize(400, 40))
        self.analyze_model1.setFont(font4)
        self.analyze_model1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.analyze_model1)

        self.analyze_model2 = QPushButton(self.analyze_button_section2)
        self.analyze_model2.setObjectName(u"analyze_model2")
        self.analyze_model2.setMaximumSize(QSize(400, 40))
        self.analyze_model2.setFont(font4)
        self.analyze_model2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.analyze_model2)

        self.analyze_model3 = QPushButton(self.analyze_button_section2)
        self.analyze_model3.setObjectName(u"analyze_model3")
        self.analyze_model3.setMaximumSize(QSize(400, 40))
        self.analyze_model3.setFont(font4)
        self.analyze_model3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.analyze_model3)


        self.verticalLayout_10.addWidget(self.analyze_button_section2)


        self.verticalLayout_9.addWidget(self.analyze_button_section)

        self.Pages_Widget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.Btn_Menu_1.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.Btn_Menu_2.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.Btn_Menu_3.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.result_image.setText("")
        self.default_image.setText("")
        self.centroid_image_result.setText("")
        self.upload_image_button.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.model_2.setText(QCoreApplication.translate("MainWindow", u"SSD Inception", None))
        self.model_1.setText(QCoreApplication.translate("MainWindow", u"RFCN", None))
        self.model_3.setText(QCoreApplication.translate("MainWindow", u"SSD Mobilenet", None))
        self.play_button.setText("")
        self.VideoButton.setText(QCoreApplication.translate("MainWindow", u"Upload Video", None))
        self.analyze_default_video.setText("")
        self.analyze_line_graph_video.setText("")
        self.analyze_masking_video.setText("")
        self.analyze_upload_video_button.setText(QCoreApplication.translate("MainWindow", u"Upload Video", None))
        self.analyze_model1.setText(QCoreApplication.translate("MainWindow", u"SSD Inception", None))
        self.analyze_model2.setText(QCoreApplication.translate("MainWindow", u"RFCN", None))
        self.analyze_model3.setText(QCoreApplication.translate("MainWindow", u"SSD Mobilenet", None))
    # retranslateUi

