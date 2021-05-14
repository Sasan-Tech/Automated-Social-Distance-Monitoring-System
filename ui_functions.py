from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QStyle
from PIL.ImageQt import ImageQt

from run_photo import *
from analyse_area import *

class UIFunctions(QMainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 90
            
            if width == 90:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()
            
    def uploadImage(self, frozen_path):
        imagePath = QFileDialog.getOpenFileName()
        img, centroids, coordinates = predict_photo(frozen_path, imagePath[0])

        #Turn this on to get the distance detection
        #qimage = ImageQt(img)


        # Turn this one to get the masked photo
        qimage = ImageQt(mask_area(centroids, coordinates, imagePath[0]))
        

        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.ui.image_label.setPixmap(pixmap)
        self.ui.image_label.resize(pixmap.width(), pixmap.height())        
        
    def loadVideo(self):
        fileName = QFileDialog.getOpenFileName()
        
        if fileName[0] != "":
            self.media.setMedia(QMediaContent(QUrl.fromLocalFile(fileName[0])))
            self.ui.play_button.setEnabled(True)
        
    def stateChanged(self):
        if self.media.state() == QMediaPlayer.PlayingState:
            pause_icon = QtGui.QIcon()
            pause_icon.addPixmap(QtGui.QPixmap("images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.play_button.setIcon(pause_icon)
            
        else:
            play_icon = QtGui.QIcon()
            play_icon.addPixmap(QtGui.QPixmap("images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.play_button.setIcon(play_icon)
            
    def positionChanged(self, position):
        self.ui.video_slider.setValue(position)
        
    
    def durationChanged(self, duration):
        self.ui.video_slider.setRange(0, duration)
        
    def playVideo(self):
        if self.media.state() == QMediaPlayer.PlayingState:
            self.media.pause()
        else:
            self.media.play()
            
    def setVideoPosition(self, position):
        self.media.setPosition(position)