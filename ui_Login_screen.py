from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Login_screen(object):
    def setupUi(self, Login_screen):
        if Login_screen.objectName():
            Login_screen.setObjectName(u"Login_screen")
        Login_screen.resize(408, 510)
        self.centralwidget = QWidget(Login_screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 410, 510))
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.background)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(5, 5, 400, 500))
        self.container.setStyleSheet(u"background-color: rgb(61, 61, 61);\n"
"border-radius: 15px;\n"
"")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.background_2 = QFrame(self.container)
        self.background_2.setObjectName(u"background_2")
        self.background_2.setGeometry(QRect(10, 10, 381, 481))
        self.background_2.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(81, 81, 81);\n"
"	color: rgb(255, 155, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.background_2.setFrameShape(QFrame.NoFrame)
        self.background_2.setFrameShadow(QFrame.Raised)
        self.login_button = QPushButton(self.background_2)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(40, 370, 300, 50))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(70, 70, 70); \n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border : 2px solid rgb(45, 45, 45);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(61, 61, 61); \n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.login_button.setFlat(False)
        self.name = QLineEdit(self.background_2)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(40, 170, 300, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.name.setFont(font1)
        self.name.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color: rgb(70, 70, 70);\n"
"	border : 2px solid rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:  3px solid rgb(45, 45, 45) ;\n"
"}")
        self.name.setMaxLength(32767)
        self.name.setAlignment(Qt.AlignCenter)
        self.max_button = QPushButton(self.background_2)
        self.max_button.setObjectName(u"max_button")
        self.max_button.setGeometry(QRect(70, 20, 20, 20))
        self.max_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(52, 199, 73);\n"
"}")
        self.mini_button = QPushButton(self.background_2)
        self.mini_button.setObjectName(u"mini_button")
        self.mini_button.setGeometry(QRect(40, 20, 20, 20))
        self.mini_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(248, 187, 63);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(255, 209, 115);\n"
"	\n"
"}")
        self.close_button = QPushButton(self.background_2)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(10, 20, 20, 20))
        self.close_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(249, 98, 93);\n"
"}")
        self.password = QLineEdit(self.background_2)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(40, 270, 300, 41))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color: rgb(70, 70, 70);\n"
"	border : 2px solid rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:  3px solid rgb(45, 45, 45) ;\n"
"}")
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.label_2 = QLabel(self.background_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 371, 471))
        self.label_2.setStyleSheet(u"background-color: none;")
        self.label_2.raise_()
        self.login_button.raise_()
        self.name.raise_()
        self.max_button.raise_()
        self.mini_button.raise_()
        self.close_button.raise_()
        self.password.raise_()
        Login_screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_screen)

        QMetaObject.connectSlotsByName(Login_screen)
    # setupUi

    def retranslateUi(self, Login_screen):
        Login_screen.setWindowTitle(QCoreApplication.translate("Login_screen", u"MainWindow", None))
        self.login_button.setText(QCoreApplication.translate("Login_screen", u"Login ", None))
        self.name.setInputMask("")
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("Login_screen", u"Username", None))
        self.max_button.setText("")
        self.mini_button.setText("")
        self.close_button.setText("")
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Login_screen", u"Password ", None))
        self.label_2.setText("")
    # retranslateUi

