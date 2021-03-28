

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        font = QFont()
        font.setPointSize(68)
        SplashScreen.setFont(font)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularprogressbarbase = QFrame(self.centralwidget)
        self.circularprogressbarbase.setObjectName(u"circularprogressbarbase")
        self.circularprogressbarbase.setGeometry(QRect(10, 10, 320, 320))
        self.circularprogressbarbase.setFrameShape(QFrame.NoFrame)
        self.circularprogressbarbase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularprogressbarbase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749428 rgba(255, 0, 255, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
"	border-radius: 150px;\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularprogressbarbase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127,120);\n"
"}\n"
"")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularprogressbarbase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(30, 30, 260, 260))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 130px;\n"
"	\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.labetitle = QLabel(self.container)
        self.labetitle.setObjectName(u"labetitle")
        self.labetitle.setGeometry(QRect(30, 50, 201, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.labetitle.setFont(font1)
        self.labetitle.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labetitle.setFrameShape(QFrame.WinPanel)
        self.labetitle.setAlignment(Qt.AlignCenter)
        self.labelpercentage = QLabel(self.container)
        self.labelpercentage.setObjectName(u"labelpercentage")
        self.labelpercentage.setGeometry(QRect(60, 70, 151, 121))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(50)
        self.labelpercentage.setFont(font2)
        self.labelpercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelpercentage.setFrameShape(QFrame.WinPanel)
        self.labelpercentage.setAlignment(Qt.AlignCenter)
        self.labelpercentage.setMargin(0)
        self.label = QLabel(self.container)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 170, 181, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: #FFFFFF;\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(90, 90, 139);\n"
"	border-radius: 10px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labetitle.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:#ff9bff;\">GUI</span><span style=\" font-weight:600;\"> Maker </span></p></body></html>", None))
        self.labelpercentage.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-size:36pt; color:#ff55ff;\">0</span><span style=\" font-size:26pt; color:#ff55ff; vertical-align:super;\">%</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("SplashScreen", u"<strong>loading...<strong>", None))
    # retranslateUi

