# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

# import some PyQt5 modules
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


import dataset_builder as db
import skin_reco
import numpy as np
import os
import tensorflow as tf

from keras.preprocessing.image import array_to_img, img_to_array

#CATEGORIES = ["A","AA","U","W","Y"]
#CATEGORIES = ["A","AA","blank"]
#CATEGORIES = ["ayubowan","hamuweema","I_Love_You","sathutak","your","blank"]
CATEGORIES = ["ආයුබෝවන්","හමුවීම","මම ඔබට ආදරෙයි","සතුටක්","ඔබ","හිස්"]

def max_index_of(array):
    m = -1
    index = -1
    for i in range(len(array)):
        if array[i] > m:
            m = array[i]
            index = i
    return index


# import Opencv module
import cv2

class Ui_signWindow(object):
    def setupUi(self, signWindow):
        signWindow.setObjectName("signWindow")
        signWindow.resize(800, 665)
        signWindow.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.centralwidget = QtWidgets.QWidget(signWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 461, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.cameralbl = QtWidgets.QLabel(self.centralwidget)
        self.cameralbl.setGeometry(QtCore.QRect(120, 80, 600, 351))
        self.cameralbl.setAcceptDrops(False)
        self.cameralbl.setAutoFillBackground(False)
        self.cameralbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.cameralbl.setText("")
        self.cameralbl.setObjectName("cameralbl")
        self.textlbl = QtWidgets.QLabel(self.centralwidget)
        self.textlbl.setGeometry(QtCore.QRect(120, 460, 621, 51))
        self.textlbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textlbl.setFrameShape(QtWidgets.QFrame.Box)
        self.textlbl.setText("")
        self.textlbl.setObjectName("textlbl")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 540, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 540, 141, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 470, 100, 36))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(190, 540, 141, 51))
        self.exit_btn.setStyleSheet("background-color: rgb(170, 170, 255);")
        #lambda is used when using extra arg in the method
        self.exit_btn.clicked.connect(lambda:self.closescr(signWindow))
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        signWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(signWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        signWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(signWindow)
        self.statusbar.setObjectName("statusbar")
        signWindow.setStatusBar(self.statusbar)

        self.retranslateUi(signWindow)
        QtCore.QMetaObject.connectSlotsByName(signWindow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.pushButton.clicked.connect(self.controlTimer)
        self.pushButton_2.clicked.connect(self.controlTimer)

    def closescr(self,signWindow):
        #hide the screen when exit btn is clicked
        signWindow.hide()


        
    def retranslateUi(self, signWindow):
        _translate = QtCore.QCoreApplication.translate
        signWindow.setWindowTitle(_translate("signWindow", "MainWindow"))
        self.label.setText(_translate("signWindow", "<html><head/><body><p align=\"center\">  SIGN TO TEXT MODE</p></body></html>"))
        self.pushButton.setText(_translate("signWindow", "START"))
        self.pushButton_2.setText(_translate("signWindow", "STOP"))
        self.label_2.setText(_translate("signWindow", "OUTPUT :"))
        self.exit_btn.setText(_translate("signWindow", "EXIT"))

    def viewCam(self):
        #model = tf.keras.models.load_model("K:/python/Cam/src/sign_language_sinhala_3.model")
        ret,image = self.cap.read()
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        cv2.rectangle(image, (100,100), (300,300), (0,0,255), 1)
        image = cv2.GaussianBlur(image,(5,5),0)
        


        
        grey = cv2.cvtColor(image[100:300, 100:300], cv2.COLOR_BGR2GRAY)
        
        thresh = cv2.threshold(grey,210,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
        image2 = cv2.resize(thresh, (db.width, db.height))
        image2= img_to_array(image2)
        image2 = np.array(image2, dtype="float") / 255.0
        image2 = image2.reshape(1, db.width, db.height, db.channel)
            
            # use the model to predict the output
        output = model.predict(image2)
        pred_name = CATEGORIES[np.argmax(output)]
        print(pred_name)
        self.textlbl.setText(pred_name)
        font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(image,pred_name, (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)
        cv2.imshow('result', thresh)
        height,width,channel = image.shape
        step = channel*width
        qImg = QImage(image.data,width,height,step,QImage.Format_RGB888)
        self.cameralbl.setPixmap(QPixmap.fromImage(qImg))
                                     
    def controlTimer(self):
       if not self.timer.isActive():
          self.cap = cv2.VideoCapture(0)
          self.timer.start(20)

       else:
         self.timer.stop()
         self.cap.release()                            
                                     
                                     

if __name__ == "__main__":
    

    import sys
    model = tf.keras.models.load_model("K:/python/Cam/src/sign_language_sinhala_3.model")
    app = QtWidgets.QApplication(sys.argv)
    signWindow = QtWidgets.QMainWindow()
    ui = Ui_signWindow()
    ui.setupUi(signWindow)
    signWindow.show()
    sys.exit(app.exec_())
