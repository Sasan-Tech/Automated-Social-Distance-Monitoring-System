# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trying.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 803)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(90, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255); border: 0px solid;")
        self.Btn_Toggle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QtCore.QSize(20, 20))
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Content.setStyleSheet("")
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(90, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(90, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Btn_Menu_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.Btn_Menu_1.setFont(font)
        self.Btn_Menu_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_Menu_1.setObjectName("Btn_Menu_1")
        self.verticalLayout_4.addWidget(self.Btn_Menu_1)
        self.Btn_Menu_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.Btn_Menu_2.setFont(font)
        self.Btn_Menu_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_Menu_2.setObjectName("Btn_Menu_2")
        self.verticalLayout_4.addWidget(self.Btn_Menu_2)
        self.Btn_Menu_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.Btn_Menu_3.setFont(font)
        self.Btn_Menu_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_Menu_3.setObjectName("Btn_Menu_3")
        self.verticalLayout_4.addWidget(self.Btn_Menu_3)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.frame_pages)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Pages_Widget.setFont(font)
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_images = QtWidgets.QFrame(self.page)
        self.frame_images.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_images.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_images.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_images.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_images.setObjectName("frame_images")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_images)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.default_image = QtWidgets.QLabel(self.frame_images)
        self.default_image.setMaximumSize(QtCore.QSize(768, 432))
        self.default_image.setText("")
        self.default_image.setObjectName("default_image")
        self.horizontalLayout_6.addWidget(self.default_image)
        self.result_image = QtWidgets.QLabel(self.frame_images)
        self.result_image.setMaximumSize(QtCore.QSize(768, 432))
        self.result_image.setText("")
        self.result_image.setObjectName("result_image")
        self.horizontalLayout_6.addWidget(self.result_image)
        self.verticalLayout_6.addWidget(self.frame_images)
        self.extension_image_result_section = QtWidgets.QFrame(self.page)
        self.extension_image_result_section.setMaximumSize(QtCore.QSize(16777215, 500))
        self.extension_image_result_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extension_image_result_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extension_image_result_section.setObjectName("extension_image_result_section")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.extension_image_result_section)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.centroid_image_result = QtWidgets.QLabel(self.extension_image_result_section)
        self.centroid_image_result.setMaximumSize(QtCore.QSize(768, 432))
        self.centroid_image_result.setText("")
        self.centroid_image_result.setObjectName("centroid_image_result")
        self.horizontalLayout_8.addWidget(self.centroid_image_result)
        self.verticalLayout_6.addWidget(self.extension_image_result_section)
        self.button_section = QtWidgets.QFrame(self.page)
        self.button_section.setMaximumSize(QtCore.QSize(16777215, 120))
        self.button_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.button_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_section.setObjectName("button_section")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.button_section)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.upload_image_section = QtWidgets.QFrame(self.button_section)
        self.upload_image_section.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upload_image_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upload_image_section.setObjectName("upload_image_section")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.upload_image_section)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.upload_image_button = QtWidgets.QPushButton(self.upload_image_section)
        self.upload_image_button.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.upload_image_button.setFont(font)
        self.upload_image_button.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.upload_image_button.setObjectName("upload_image_button")
        self.horizontalLayout_7.addWidget(self.upload_image_button)
        self.analyze_image_button = QtWidgets.QPushButton(self.upload_image_section)
        self.analyze_image_button.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.analyze_image_button.setFont(font)
        self.analyze_image_button.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.analyze_image_button.setObjectName("analyze_image_button")
        self.horizontalLayout_7.addWidget(self.analyze_image_button)
        self.verticalLayout_8.addWidget(self.upload_image_section)
        self.model_button_section = QtWidgets.QFrame(self.button_section)
        self.model_button_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.model_button_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.model_button_section.setObjectName("model_button_section")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.model_button_section)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.model_1 = QtWidgets.QPushButton(self.model_button_section)
        self.model_1.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.model_1.setFont(font)
        self.model_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.model_1.setObjectName("model_1")
        self.horizontalLayout_3.addWidget(self.model_1)
        self.model_2 = QtWidgets.QPushButton(self.model_button_section)
        self.model_2.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.model_2.setFont(font)
        self.model_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.model_2.setObjectName("model_2")
        self.horizontalLayout_3.addWidget(self.model_2)
        self.model_3 = QtWidgets.QPushButton(self.model_button_section)
        self.model_3.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.model_3.setFont(font)
        self.model_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.model_3.setObjectName("model_3")
        self.horizontalLayout_3.addWidget(self.model_3)
        self.verticalLayout_8.addWidget(self.model_button_section)
        self.verticalLayout_6.addWidget(self.button_section)
        self.Pages_Widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.videoWidget = QtWidgets.QWidget(self.page_2)
        self.videoWidget.setObjectName("videoWidget")
        self.verticalLayout_7.addWidget(self.videoWidget)
        self.video_button_section = QtWidgets.QFrame(self.page_2)
        self.video_button_section.setMaximumSize(QtCore.QSize(16777215, 120))
        self.video_button_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.video_button_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_button_section.setObjectName("video_button_section")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.video_button_section)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.upper_half_section = QtWidgets.QFrame(self.video_button_section)
        self.upper_half_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.upper_half_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upper_half_section.setObjectName("upper_half_section")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.upper_half_section)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.VideoButton = QtWidgets.QPushButton(self.upper_half_section)
        self.VideoButton.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.VideoButton.setFont(font)
        self.VideoButton.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.VideoButton.setObjectName("VideoButton")
        self.horizontalLayout_12.addWidget(self.VideoButton)
        self.ReplayButton = QtWidgets.QPushButton(self.upper_half_section)
        self.ReplayButton.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ReplayButton.setFont(font)
        self.ReplayButton.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.ReplayButton.setObjectName("ReplayButton")
        self.horizontalLayout_12.addWidget(self.ReplayButton)
        self.verticalLayout_11.addWidget(self.upper_half_section)
        self.models_video_section = QtWidgets.QFrame(self.video_button_section)
        self.models_video_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.models_video_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.models_video_section.setObjectName("models_video_section")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.models_video_section)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.video_section_model1 = QtWidgets.QPushButton(self.models_video_section)
        self.video_section_model1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.video_section_model1.setFont(font)
        self.video_section_model1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.video_section_model1.setObjectName("video_section_model1")
        self.horizontalLayout_4.addWidget(self.video_section_model1)
        self.video_section_model2 = QtWidgets.QPushButton(self.models_video_section)
        self.video_section_model2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.video_section_model2.setFont(font)
        self.video_section_model2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.video_section_model2.setObjectName("video_section_model2")
        self.horizontalLayout_4.addWidget(self.video_section_model2)
        self.video_section_model3 = QtWidgets.QPushButton(self.models_video_section)
        self.video_section_model3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.video_section_model3.setFont(font)
        self.video_section_model3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.video_section_model3.setObjectName("video_section_model3")
        self.horizontalLayout_4.addWidget(self.video_section_model3)
        self.verticalLayout_11.addWidget(self.models_video_section)
        self.verticalLayout_7.addWidget(self.video_button_section)
        self.Pages_Widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.analyze_video_result_section = QtWidgets.QFrame(self.page_3)
        self.analyze_video_result_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.analyze_video_result_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analyze_video_result_section.setObjectName("analyze_video_result_section")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.analyze_video_result_section)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.analyze_video_container = QtWidgets.QWidget(self.analyze_video_result_section)
        self.analyze_video_container.setObjectName("analyze_video_container")
        self.horizontalLayout_9.addWidget(self.analyze_video_container)
        self.analyze_line_graph_video = QtWidgets.QLabel(self.analyze_video_result_section)
        self.analyze_line_graph_video.setText("")
        self.analyze_line_graph_video.setObjectName("analyze_line_graph_video")
        self.horizontalLayout_9.addWidget(self.analyze_line_graph_video)
        self.verticalLayout_9.addWidget(self.analyze_video_result_section)
        self.frame = QtWidgets.QFrame(self.page_3)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.analyze_video_masking_section = QtWidgets.QLabel(self.frame)
        self.analyze_video_masking_section.setText("")
        self.analyze_video_masking_section.setObjectName("analyze_video_masking_section")
        self.horizontalLayout_5.addWidget(self.analyze_video_masking_section, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_9.addWidget(self.frame)
        self.analyze_button_section = QtWidgets.QFrame(self.page_3)
        self.analyze_button_section.setMaximumSize(QtCore.QSize(16777215, 120))
        self.analyze_button_section.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.analyze_button_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analyze_button_section.setObjectName("analyze_button_section")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.analyze_button_section)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.analyze_button_sectionn1 = QtWidgets.QFrame(self.analyze_button_section)
        self.analyze_button_sectionn1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analyze_button_sectionn1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analyze_button_sectionn1.setObjectName("analyze_button_sectionn1")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.analyze_button_sectionn1)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.analyze_upload_video_button = QtWidgets.QPushButton(self.analyze_button_sectionn1)
        self.analyze_upload_video_button.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.analyze_upload_video_button.setFont(font)
        self.analyze_upload_video_button.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.analyze_upload_video_button.setObjectName("analyze_upload_video_button")
        self.horizontalLayout_10.addWidget(self.analyze_upload_video_button)
        self.verticalLayout_10.addWidget(self.analyze_button_sectionn1)
        self.analyze_button_section2 = QtWidgets.QFrame(self.analyze_button_section)
        self.analyze_button_section2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analyze_button_section2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analyze_button_section2.setObjectName("analyze_button_section2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.analyze_button_section2)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.analyze_model1 = QtWidgets.QPushButton(self.analyze_button_section2)
        self.analyze_model1.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.analyze_model1.setFont(font)
        self.analyze_model1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.analyze_model1.setObjectName("analyze_model1")
        self.horizontalLayout_11.addWidget(self.analyze_model1)
        self.analyze_model2 = QtWidgets.QPushButton(self.analyze_button_section2)
        self.analyze_model2.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.analyze_model2.setFont(font)
        self.analyze_model2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.analyze_model2.setObjectName("analyze_model2")
        self.horizontalLayout_11.addWidget(self.analyze_model2)
        self.analyze_model3 = QtWidgets.QPushButton(self.analyze_button_section2)
        self.analyze_model3.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.analyze_model3.setFont(font)
        self.analyze_model3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.analyze_model3.setObjectName("analyze_model3")
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automated Social Distancing Monitoring System"))
        self.Btn_Menu_1.setText(_translate("MainWindow", "Image"))
        self.Btn_Menu_2.setText(_translate("MainWindow", "Video"))
        self.Btn_Menu_3.setText(_translate("MainWindow", "Analyze"))
        self.upload_image_button.setText(_translate("MainWindow", "Upload Image"))
        self.analyze_image_button.setText(_translate("MainWindow", "Analyze"))
        self.model_1.setText(_translate("MainWindow", "SSD Inception"))
        self.model_2.setText(_translate("MainWindow", "RFCN"))
        self.model_3.setText(_translate("MainWindow", "SSD Mobilenet"))
        self.VideoButton.setText(_translate("MainWindow", "Upload Video"))
        self.ReplayButton.setText(_translate("MainWindow", "Replay"))
        self.video_section_model1.setText(_translate("MainWindow", "SSD Inception"))
        self.video_section_model2.setText(_translate("MainWindow", "RFCN"))
        self.video_section_model3.setText(_translate("MainWindow", "SSD Mobilenet"))
        self.analyze_upload_video_button.setText(_translate("MainWindow", "Upload Video"))
        self.analyze_model1.setText(_translate("MainWindow", "SSD Inception"))
        self.analyze_model2.setText(_translate("MainWindow", "RFCN"))
        self.analyze_model3.setText(_translate("MainWindow", "SSD Mobilenet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
