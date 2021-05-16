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
        self.ui.Btn_Menu_1.clicked.connect(lambda: UIFunctions.page1(self))

        # PAGE 2
        self.ui.Btn_Menu_2.clicked.connect(lambda: UIFunctions.page2(self))
        
        # PAGE 3
        self.ui.Btn_Menu_3.clicked.connect(lambda: UIFunctions.page3(self))
        
        
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
        self.ui.ReplayButton.setEnabled(False)
        self.ui.video_section_model1.setEnabled(False)
        self.ui.video_section_model2.setEnabled(False)
        self.ui.video_section_model3.setEnabled(False)

        self.ui.VideoButton.clicked.connect(lambda: UIFunctions.loadVideo(self))
        
        self.ui.video_section_model1.clicked.connect(lambda: UIFunctions.loadModelVideoSection(self, ssd_inception_frozen_path))
        self.ui.video_section_model2.clicked.connect(lambda: UIFunctions.loadModelVideoSection(self, rfcn_frozen_path))
        self.ui.video_section_model3.clicked.connect(lambda: UIFunctions.loadModelVideoSection(self, ssd_mobilenet_v1_coco_frozen_path))
        
        video = QVideoWidget()
        vBox = QVBoxLayout()
        vBox.addWidget(video)

        self.ui.videoWidget.setLayout(vBox)    
        self.media.setVideoOutput(video)
        self.ui.ReplayButton.clicked.connect(lambda: self.media.play())
        

        ### ANALYZE SECTION ###
        self.analyze_media = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.ui.analyze_model1.setEnabled(False)
        self.ui.analyze_model2.setEnabled(False)
        self.ui.analyze_model3.setEnabled(False)

        self.ui.analyze_upload_video_button.clicked.connect(lambda: UIFunctions.loadVideoAnalyzed(self))

        self.ui.analyze_model1.clicked.connect(lambda: UIFunctions.loadModelAnalyzeSection(self, ssd_inception_frozen_path))
        self.ui.analyze_model2.clicked.connect(lambda: UIFunctions.loadModelAnalyzeSection(self, rfcn_frozen_path))
        self.ui.analyze_model3.clicked.connect(lambda: UIFunctions.loadModelAnalyzeSection(self, ssd_mobilenet_v1_coco_frozen_path))
        
        analyzeVideo = QVideoWidget()
        vAnalyzedBox = QVBoxLayout()
        vAnalyzedBox.addWidget(analyzeVideo)

        self.ui.analyze_video_container.setLayout(vAnalyzedBox)
        self.analyze_media.setVideoOutput(analyzeVideo)
        
        

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())