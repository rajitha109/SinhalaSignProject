# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\CHATHUMINI\Desktop\pro_practical\introduction.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_introWindow(object):
    def setupUi(self, introWindow):
        introWindow.setObjectName("introWindow")
        introWindow.resize(1163, 914)
        introWindow.setAutoFillBackground(False)
        introWindow.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.centralwidget = QtWidgets.QWidget(introWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 250, 1111, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        
        self.aim_lbl = QtWidgets.QLabel(self.groupBox)
        self.aim_lbl.setGeometry(QtCore.QRect(40, 40, 1011, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aim_lbl.setFont(font)
        self.aim_lbl.setStyleSheet("background-color:rgb(138, 201, 204)")
        self.aim_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.aim_lbl.setObjectName("aim_lbl")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 10, 1111, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.intro_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.intro_lbl.setGeometry(QtCore.QRect(40, 50, 1011, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.intro_lbl.setFont(font)
        self.intro_lbl.setStyleSheet("background-color:rgb(138, 201, 204)")
        self.intro_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.intro_lbl.setObjectName("intro_lbl")
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 430, 1111, 331))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.team_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.team_lbl.setGeometry(QtCore.QRect(50, 50, 1001, 251))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.team_lbl.setFont(font)
        self.team_lbl.setStyleSheet("background-color:rgb(138, 201, 204)")
        self.team_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.team_lbl.setObjectName("team_lbl")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 790, 151, 50))
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 255);")
        #lambda is used when using extra arg in the method
        self.pushButton.clicked.connect(lambda:self.closescr(introWindow))
        font = QtGui.QFont("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 790, 311, 50))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        font = QtGui.QFont("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        introWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(introWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 26))
        self.menubar.setObjectName("menubar")
        introWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(introWindow)
        self.statusbar.setObjectName("statusbar")
        introWindow.setStatusBar(self.statusbar)

        self.retranslateUi(introWindow)
        QtCore.QMetaObject.connectSlotsByName(introWindow)

    def closescr(self,introWindow):
        #hide the screen when exit btn is clicked
        introWindow.hide()
        

    def retranslateUi(self, introWindow):
        _translate = QtCore.QCoreApplication.translate
        introWindow.setWindowTitle(_translate("introWindow", "introduction"))
        self.groupBox.setTitle(_translate("introWindow", "AIM  "))
        self.aim_lbl.setText(_translate("introWindow", "  Providing real time bidirectional language translation method for converting Sinhala sign language to \n"
"  Sinhala text and converting Sinhala speech to Sinhala sign language. "))
        self.groupBox_2.setTitle(_translate("introWindow", "INTRODUTION"))
        self.intro_lbl.setText(_translate("introWindow", " In this  system, Sinhala sign gestures are the source which is then converted into Sinhala text. \n"
" Further, Sinhala speech is also the source which is then converted into animated Sinhala sign gesture. \n"
" With this implementation, it is expected to allow the hearing impaired people in Sri Lanka to fulfill \n"
" their communicating requirements with ordinary people. "))
        self.groupBox_3.setTitle(_translate("introWindow", "OUR TEAM - SiCode"))
        self.team_lbl.setText(_translate("introWindow", "  1)A.R.V. Prabhathiya \n"
"\n"
"  2)R.S.Pussepitiya \n"
"\n"
"  3)B.H.I.A. Wijethilaka \n"
"\n"
"  4)W.M.B.T. Wanninayaka \n"
"\n"
"  5)K.D.C.I. Thathsarani"))
        self.pushButton.setText(_translate("introWindow", "EXIT"))
        self.pushButton_2.setText(_translate("introWindow", "DATA COLLECTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    introWindow = QtWidgets.QMainWindow()
    ui = Ui_introWindow()
    ui.setupUi(introWindow)
    introWindow.show()
    sys.exit(app.exec_())
