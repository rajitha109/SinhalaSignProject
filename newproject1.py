# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newproject.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap 
from sign import Ui_signWindow
from speech import Ui_speechWindow
from introduction import Ui_introWindow

class Ui_MainWin(object):

    def sign(self):
        self.signWindow = QtWidgets.QMainWindow()
        self.ui = Ui_signWindow()
        self.ui.setupUi( self.signWindow)
        self.signWindow.show()
        
    def speech(self):
        self.speechWindow = QtWidgets.QMainWindow()
        self.ui = Ui_speechWindow()
        self.ui.setupUi(self.speechWindow)
        self.speechWindow.show()

    def introduction(self):
        self.introWindow = QtWidgets.QMainWindow()
        self.ui = Ui_introWindow()
        self.ui.setupUi(self.introWindow)
        self.introWindow.show()    
        
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(1072, 623)
        MainWin.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.centralwidget = QtWidgets.QWidget(MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 1021, 101))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        

        self.info_btn = QtWidgets.QPushButton(self.centralwidget)
        self.info_btn.setGeometry(QtCore.QRect(100, 510, 280, 50))
        self.info_btn.setStyleSheet("background-color: rgb(170, 170, 255);\n")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.info_btn.setFont(font)
        self.info_btn.setIconSize(QtCore.QSize(20, 20))
        self.info_btn.setObjectName("info_btn")
        self.info_btn.clicked.connect(self.introduction)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 510, 280, 50))
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sign)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 510, 280, 50))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.speech)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(95, 120, 901, 350))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menubar.setObjectName("menubar")
        MainWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWin)
        self.statusbar.setObjectName("statusbar")
        MainWin.setStatusBar(self.statusbar)

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

        #add an image to the label
        pixmap = QPixmap("C:/Users/CHATHUMINI/Desktop/pro_practical/image1.jpg")
        self.label_2.setPixmap(pixmap.scaled(900,500,QtCore.Qt.KeepAspectRatio))

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "MainWindow"))
        self.label.setText(_translate("MainWin", "<html><head/><body><p align=\"center\">REAL-TIME LANGUAGE TRANSLATOR FOR SINHALA SIGN LANGUAGE ,</p><p align=\"center\">SINHALA TEXT &amp; SINHALA SPEECH </p></body></html>"))
        self.pushButton.setText(_translate("MainWin", "SIGN TO TEXT MODE"))
        self.pushButton_2.setText(_translate("MainWin", "SPEECH TO SIGN MODE"))
        self.info_btn.setText(_translate("MainWin", "INTRODUCTION"))        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWin()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec_())
