from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QStyle
from PIL.ImageQt import ImageQt

from run_photo import *
from analyse_area import *
from run_video import *

class UIFunctions(QMainWindow):
    
    ####################
    ### MENU SECTION ###
    ####################
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
    
    
    #####################
    ### IMAGE SECTION ###
    #####################
    def uploadImage(self, frozen_path):
        global image, IMG_WIDTH, IMG_HEIGHT
        imagePath = QFileDialog.getOpenFileName()
        IMG_WIDTH = 768
        IMG_HEIGHT = 432
        
        if not (imagePath[0] == ""):
            image = imagePath[0]
            
            self.ui.model_1.setEnabled(True)
            self.ui.model_2.setEnabled(True)
            self.ui.model_3.setEnabled(True)
                       
            pixmap = QPixmap(imagePath[0])
            resize_pixmap = pixmap.scaled(IMG_WIDTH, IMG_HEIGHT)
            self.ui.default_image.setPixmap(resize_pixmap)
            self.ui.default_image.resize(resize_pixmap.width(), resize_pixmap.height())      
        else:
            self.ui.analyze_image_button.setEnabled(False)
            self.ui.model_1.setEnabled(False)
            self.ui.model_2.setEnabled(False)
            self.ui.model_3.setEnabled(False)
        
    def loadModelForImage(self, frozen_path):
        global img, centroids, coordinates
        img, centroids, coordinates = predict_photo(frozen_path, image)
        qimage = ImageQt(img)
        
        pixmap = QtGui.QPixmap.fromImage(qimage)
        resize_pixmap = pixmap.scaled(IMG_WIDTH, IMG_HEIGHT)
        
        self.ui.result_image.setPixmap(resize_pixmap)
        self.ui.result_image.resize(resize_pixmap.width(), resize_pixmap.height())    
        self.ui.analyze_image_button.setEnabled(True) 
        
    def maskingForImage(self):
        qimage = ImageQt(mask_area(centroids, coordinates, image))
        
        pixmap = QtGui.QPixmap.fromImage(qimage)
        resize_pixmap = pixmap.scaled(IMG_WIDTH, IMG_HEIGHT)
        
        self.ui.centroid_image_result.setPixmap(resize_pixmap)
        self.ui.centroid_image_result.resize(resize_pixmap.width(), resize_pixmap.height()) 
        
        
    #####################
    ### VIDEO SECTION ###
    #####################    
        
    def loadVideo(self):
        fileName = QFileDialog.getOpenFileName()

        if fileName[0] != "":
            self.videoLink = fileName[0]
            # Call the predict video
            self.ui.ReplayButton.setEnabled(True)
            print("Done upload video")    
            

    def loadModelVideoSection(self, frozen_graph):
        self.media.setMedia(QMediaContent())
        _, _, _, _ = predict_video(frozen_graph, self.videoLink)
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile("temp/tempVideo.avi")))
        self.media.play()   
        
                 
    #######################
    ### ANALYZE SECTION ###
    ####################### 
            
    def loadVideoAnalyzedSection(self):
        fileName = QFileDialog.getOpenFileName()
        
        if fileName[0] != "":
            self.analyze_media.setMedia(QMediaContent(QUrl.fromLocalFile(fileName[0])))
            self.analyze_media.play()    
    
    
    ##########################
    ### NAVIGATION SECTION ###
    ##########################       
              
    def page1(self):
        self.ui.Pages_Widget.setCurrentWidget(self.ui.page)
        
    def page2(self):
        self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2)
        
        # Clearing Image section content
        self.ui.default_image.clear()
        self.ui.result_image.clear()
        self.ui.centroid_image_result.clear()
        
    def page3(self):
        self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3)
        
        # Clearing Image section content
        self.ui.default_image.clear()
        self.ui.result_image.clear()
        self.ui.centroid_image_result.clear()
        

    

