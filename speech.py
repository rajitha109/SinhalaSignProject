# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speech.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import speech_recognition as sr 

class Ui_speechWindow(object):
    def setupUi(self, speechWindow):
        speechWindow.setObjectName("speechWindow")
        speechWindow.resize(800, 520)
        speechWindow.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.centralwidget = QtWidgets.QWidget(speechWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 461, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        
        self.cameralbl = QtWidgets.QLabel(self.centralwidget)
        self.cameralbl.setGeometry(QtCore.QRect(320, 100, 431, 351))
        self.cameralbl.setAcceptDrops(False)
        self.cameralbl.setAutoFillBackground(False)
        self.cameralbl.setFrameShape(QtWidgets.QFrame.Panel)
        self.cameralbl.setText("")
        self.cameralbl.setObjectName("cameralbl")
        
        self.PlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PlainTextEdit.setGeometry(QtCore.QRect(30, 230, 271, 91))
        self.PlainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PlainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.PlainTextEdit.setPlainText("")
        self.PlainTextEdit.setObjectName("PlainTextEdit")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PlainTextEdit.setFont(font)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(93, 188, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30,115, 120, 51))
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        
        self.stopbtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopbtn.setGeometry(QtCore.QRect(170,115, 120, 51))
        self.stopbtn.setStyleSheet("background-color: rgb(170, 170, 255);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stopbtn.setFont(font)
        self.stopbtn.setObjectName("stopbtn")        
        
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(90, 370, 141, 51))
        self.Exit.setStyleSheet("background-color: rgb(170, 170, 255);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Exit.setFont(font)
        self.Exit.setObjectName("Exit")
        self.Exit.clicked.connect(lambda:self.closescrn(speechWindow))
        
        speechWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(speechWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        speechWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(speechWindow)
        self.statusbar.setObjectName("statusbar")
        speechWindow.setStatusBar(self.statusbar)

        self.retranslateUi(speechWindow)
        QtCore.QMetaObject.connectSlotsByName(speechWindow)

        self.pushButton.clicked.connect(self.convertAudio)
        self.stopbtn.clicked.connect(self.stop)

    def closescrn(self,speechWindow):
        #hide the screen
        speechWindow.hide()
        
    def retranslateUi(self, speechWindow):
        _translate = QtCore.QCoreApplication.translate
        speechWindow.setWindowTitle(_translate("speechWindow", "MainWindow"))
        self.label.setText(_translate("speechWindow", "<html><head/><body><p align=\"center\">SPEECH TO SIGN MODE</p></body></html>"))
        self.label_2.setText(_translate("speechWindow", "<html><head/><body><p align=\"center\">INPUT TEXT :</p></body></html>"))
        self.pushButton.setText(_translate("speechWindow", "START"))
        self.Exit.setText(_translate("speechWindow", "EXIT"))
        self.stopbtn.setText(_translate("speechWindow", "STOP"))

    def convertAudio(self):
 
        r =  sr.Recognizer()
        with sr.Microphone() as source :
            msg = QMessageBox()
            msg.setWindowTitle("message")
            msg.setText("speak now....")
            msg.setIcon(QMessageBox.Information)

            x = msg.exec_()

            audio = r.listen(source)
                
        try :
            text = r.recognize_google(audio,language = 'si-LK')
            self.PlainTextEdit.setPlainText(text)
            word = text.split()
            print(word)
        except :
            self.PlainTextEdit.setPlainText("I can't hear")
           

    def stop(self):
        self.PlainTextEdit.clear()
        #msg = QMessageBox()
        #msg.setWindowTitle("message")
       # msg.setText("click start to convert....")
        #msg.setIcon(QMessageBox.Information)

       # x = msg.exec_()            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    speechWindow = QtWidgets.QMainWindow()
    ui = Ui_speechWindow()
    ui.setupUi(speechWindow)
    speechWindow.show()
    sys.exit(app.exec_())
