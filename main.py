################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PyQt5.QtWidgets import QApplication, QMainWindow
#from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

# GUI FILE
from trying import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import UIFunctions

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        
    
        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.Btn_Menu_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page))

        # PAGE 2
        self.ui.Btn_Menu_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2))
        
        # PAGE 3
        self.ui.Btn_Menu_3.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))
        
        
        ### MODEL PATH ###
        rfcn_frozen_path = "exported/rfcn_exported/frozen_inference_graph.pb"
        ssd_inception_frozen_path = "exported/ssd_inception_exported/frozen_inference_graph.pb"
        ssd_mobilenet_v1_coco_frozen_path = "exported/ssd_mobilenet_v1_coco_exported/frozen_inference_graph.pb"
        
        ### IMAGE SECTION ###
        self.ui.analyze_image_button.setEnabled(False)
        self.ui.model_1.setEnabled(False)
        self.ui.model_2.setEnabled(False)
        self.ui.model_3.setEnabled(False)
        
        
        self.ui.upload_image_button.clicked.connect(lambda: UIFunctions.uploadImage(self, rfcn_frozen_path))
        self.ui.model_1.clicked.connect(lambda: UIFunctions.loadModelForImage(self, ssd_inception_frozen_path))
        self.ui.model_2.clicked.connect(lambda: UIFunctions.loadModelForImage(self, rfcn_frozen_path))
        self.ui.model_3.clicked.connect(lambda: UIFunctions.loadModelForImage(self, ssd_mobilenet_v1_coco_frozen_path))
        
        self.ui.analyze_image_button.clicked.connect(lambda: UIFunctions.maskingForImage(self))

        ### VIDEO SECTION ###
        self.media = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        video = QVideoWidget()
        
        vBox = QVBoxLayout()
        vBox.addWidget(video)
        self.ui.videoWidget.setLayout(vBox)
        
        self.ui.VideoButton.clicked.connect(lambda: UIFunctions.loadVideo(self))
        
        self.ui.play_button.setEnabled(False)
        self.ui.play_button.clicked.connect(lambda: UIFunctions.playVideo(self))
        
        self.ui.video_slider.setRange(0, 0)
        self.ui.video_slider.sliderMoved.connect(lambda: UIFunctions.setVideoPosition(self, self.ui.video_slider.sliderPosition()))
        
        self.media.setVideoOutput(video)
        self.media.stateChanged.connect(lambda: UIFunctions.stateChanged(self))
        self.media.positionChanged.connect(lambda: UIFunctions.positionChanged(self, self.ui.video_slider.sliderPosition()))
        self.media.durationChanged.connect(lambda: UIFunctions.durationChanged(self, self.media.duration()))
        
        
        ### ANALYZE SECTION ###
        self.analyze_media = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        analyzeVideo = QVideoWidget()
        
        vAnalyzedBox = QVBoxLayout()
        vAnalyzedBox.addWidget(analyzeVideo)
        self.ui.analyze_video_container.setLayout(vAnalyzedBox)
        
        self.ui.analyze_upload_video_button.clicked.connect(lambda: UIFunctions.loadVideoAnalyzedSection(self))
        
        self.analyze_media.setVideoOutput(analyzeVideo)
        
        

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
