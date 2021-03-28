
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication, QPushButton
from ui_splash_screen import Ui_SplashScreen
from ui_Login_screen import Ui_Login_screen
from ui_Home_window import Ui_MainWindow


counter = 0
jumper = 10
x = True

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.progressBarValue(0)
        



        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)

        self.show()



    def progress (self):
        global counter
        global jumper
        value = counter

        htmlText = """<p><span style=" font-size:36pt; color:#ff55ff;">{VALUE}</span><span style=" font-size:26pt; color:#ff55ff; vertical-align:super;">%</span></p>"""

        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            self.ui.labelpercentage.setText(newHtml)
            jumper += 2
 

        if value >= 100: value = 1.000
        self.progressBarValue(value)

        if jumper == 50:
            text = '<strong>Extracting Files...<strong>'
            self.ui.label.setText(text)

        if jumper == 70:
            text = '<strong>Almost done...<strong>'
            self.ui.label.setText(text)

        if counter > 100:
            self.timer.stop()

            self.login = LoginWindow()
            self.login.show()

            self.close()

        counter += 0.2

    def progressBarValue(self, value):

        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        self.ui.circularProgress.setStyleSheet(newStylesheet)










class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login_screen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        
        self.ui.mini_button.clicked.connect(lambda: self.resizeMainWindow(118,75))
        self.ui.max_button.clicked.connect(lambda: self.resizeMainWindow(410,510))
        self.ui.close_button.clicked.connect(lambda: self.resizeMainWindow(0,0))
        self.ui.login_button.clicked.connect(lambda: self.openMainwindow())





    def resizeMainWindow(self, width, height):
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(1000)
        self.animation.setEndValue(QtCore.QSize(width,height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.start()
        if width ==0 and height==0:
            self.close()


    def openMainwindow(self):
        self.main_window = Home_window()
        self.main_window.show()
        self.close()

class Home_window(QMainWindow):
     
        def __init__(self):
            QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.ui.max_button_home.clicked.connect(lambda: self.max_button_clicked(1280,800))
            self.ui.close_button_home.clicked.connect(lambda: self.resizeHomeWindow(0,0))
            self.ui.mini_button_home.clicked.connect(lambda: self.mini_button_clicked(800,600))
            self.ui.pushButton.clicked.connect(lambda: self.toggleMenu())          
            self.ui.back_button.clicked.connect(lambda: self.backmenu())
            self.ui.settings_button.clicked.connect(lambda: self.settings_button_clicked())
            self.ui.down_button_settings.clicked.connect(lambda: self.setting_down_botton_clicked())
        def resizeHomeWindow(self, width, height):
            self.animation = QPropertyAnimation(self, b"size")
            self.animation.setDuration(1000)
            self.animation.setEndValue(QtCore.QSize(width,height))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation.start()
            if width ==0 and height==0:
                self.close()
        
        def toggleMenu(self):

            if self.ui.container.height() == 790:
                if self.ui.settings_bar.height() == 81:
                    self.animation = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation.setDuration(1000)
                    self.animation.setEndValue(QtCore.QSize(348,640))
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation.start()
                elif self.ui.settings_bar.height() == 651:
                    self.animation = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation.setDuration(1000)
                    self.animation.setEndValue(QtCore.QSize(348,71))
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation.start()                    

            elif self.ui.container.height() == 590:
                if self.ui.settings_bar.height() == 81:
                    self.animation = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation.setDuration(1000)
                    self.animation.setEndValue(QtCore.QSize(348,440))
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation.start()                    
                elif self.ui.settings_bar.height() == 651:
                    self.animation = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation.setDuration(1000)
                    self.animation.setEndValue(QtCore.QSize(348,71))
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation.start()  


        def backmenu(self):

            if self.ui.container.height() == 790:
                if self.ui.settings_bar.height() == 81:
                    self.animation = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation.setDuration(1000)
                    self.animation.setEndValue(QtCore.QSize(85,641))
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation.start()                    
                elif self.ui.settings_bar.height() == 651:
                    self.animation = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation.setDuration(1000)
                    self.animation.setEndValue(QtCore.QSize(85,71))
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation.start()

            elif self.ui.container.height() == 590:
                self.animation = QPropertyAnimation(self.ui.toggle_bar, b"size")
                self.animation.setDuration(1000)
                self.animation.setEndValue(QtCore.QSize(85,440))
                self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                self.animation.start()


        def mini_button_clicked(self, width, height):
            self.animation = QPropertyAnimation(self, b"size")
            self.animation.setDuration(1000)
            self.animation.setEndValue(QtCore.QSize(width,height))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation.start()          
            self.animation2 = QPropertyAnimation(self.ui.toggle_bar, b"size")
            self.animation2.setDuration(1000)
            self.animation2.setEndValue(QtCore.QSize(85,440))
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation2.start()
            self.animation3 = QPropertyAnimation(self.ui.container, b"size")
            self.animation3.setDuration(1000)
            self.animation3.setEndValue(QtCore.QSize(790,590))
            self.animation3.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation3.start()
            self.animation4 = QPropertyAnimation(self.ui.background, b"size")
            self.animation4.setDuration(1000)
            self.animation4.setEndValue(QtCore.QSize(760,560))
            self.animation4.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation4.start()
            self.animation5 = QPropertyAnimation(self.ui.frame_2, b"size")
            self.animation5.setDuration(1000)
            self.animation5.setEndValue(QtCore.QSize(740,530))
            self.animation5.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation5.start()
            self.animation6 = QPropertyAnimation(self.ui.max_button_home, b"geometry")
            self.animation6.setDuration(1000)
            self.animation6.setEndValue(QtCore.QRect(700, 10, 20, 20))
            self.animation6.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation6.start()
            self.animation7 = QPropertyAnimation(self.ui.mini_button_home, b"geometry")
            self.animation7.setDuration(1000)
            self.animation7.setEndValue(QtCore.QRect(673, 10, 20, 20))
            self.animation7.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation7.start()
            self.animation8 = QPropertyAnimation(self.ui.close_button_home, b"geometry")
            self.animation8.setDuration(1000)
            self.animation8.setEndValue(QtCore.QRect(645, 10, 20, 20))
            self.animation8.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation8.start()
            self.animation9 = QPropertyAnimation(self.ui.settings_button, b"geometry")
            self.animation9.setDuration(1000)
            self.animation9.setEndValue(QtCore.QRect(5, 8, 71, 61))
            self.animation9.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation9.start()
            self.animation10 = QPropertyAnimation(self.ui.settings_bar, b"geometry")
            self.animation10.setDuration(1000)
            self.animation10.setEndValue(QtCore.QRect(0, 450, 81, 81))
            self.animation10.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation10.start()


        def max_button_clicked(self, width, height):
            self.animation = QPropertyAnimation(self, b"size")
            self.animation.setDuration(1000)
            self.animation.setEndValue(QtCore.QSize(width,height))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation.start()          
            self.animation2 = QPropertyAnimation(self.ui.toggle_bar, b"size")
            self.animation2.setDuration(1000)
            self.animation2.setEndValue(QtCore.QSize(85, 641))
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation2.start()
            self.animation3 = QPropertyAnimation(self.ui.container, b"size")
            self.animation3.setDuration(1000)
            self.animation3.setEndValue(QtCore.QSize(1270, 790))
            self.animation3.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation3.start()
            self.animation4 = QPropertyAnimation(self.ui.background, b"size")
            self.animation4.setDuration(1000)
            self.animation4.setEndValue(QtCore.QSize(1240, 760))
            self.animation4.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation4.start()
            self.animation5 = QPropertyAnimation(self.ui.frame_2, b"size")
            self.animation5.setDuration(1000)
            self.animation5.setEndValue(QtCore.QSize(1220, 730))
            self.animation5.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation5.start()
            self.animation6 = QPropertyAnimation(self.ui.max_button_home, b"geometry")
            self.animation6.setDuration(1000)
            self.animation6.setEndValue(QtCore.QRect(1190, 10, 20, 20))
            self.animation6.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation6.start()
            self.animation7 = QPropertyAnimation(self.ui.mini_button_home, b"geometry")
            self.animation7.setDuration(1000)
            self.animation7.setEndValue(QtCore.QRect(1160, 10, 20, 20))
            self.animation7.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation7.start()
            self.animation8 = QPropertyAnimation(self.ui.close_button_home, b"geometry")
            self.animation8.setDuration(1000)
            self.animation8.setEndValue(QtCore.QRect(1130, 10, 20, 20))
            self.animation8.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation8.start()
            self.animation9 = QPropertyAnimation(self.ui.settings_button, b"geometry")
            self.animation9.setDuration(1000)
            self.animation9.setEndValue(QtCore.QRect(5, 8, 71, 61))
            self.animation9.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation9.start()
            self.animation10 = QPropertyAnimation(self.ui.settings_bar, b"geometry")
            self.animation10.setDuration(1000)
            self.animation10.setEndValue(QtCore.QRect(0, 649, 81, 81))
            self.animation10.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation10.start()


        def settings_button_clicked(self):
            if self.ui.container.height() == 790:
                if self.ui.toggle_bar.width() == 85:
                    self.animation = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation.setDuration(1000)
                    self.animation.setEndValue(QtCore.QSize(85,71))
                    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation.start()            
                else:
                    self.animation4 = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation4.setDuration(1000)
                    self.animation4.setEndValue(QtCore.QSize(348,71))
                    self.animation4.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation4.start()


                self.animation3 = QPropertyAnimation(self.ui.settings_bar, b"geometry")
                self.animation3.setDuration(1000)
                self.animation3.setEndValue(QtCore.QRect(0,80,85,81))
                self.animation3.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                self.animation3.start()  

                self.animation2 = QPropertyAnimation(self.ui.settings_bar, b"size")
                self.animation2.setDuration(1000)
                self.animation2.setEndValue(QtCore.QSize(85,651))
                self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animation2.start()



        def setting_down_botton_clicked(self):
            if self.ui.container.height() == 790:
                self.animation = QPropertyAnimation(self.ui.settings_bar, b"size")
                self.animation.setDuration(1000)
                self.animation.setEndValue(QtCore.QSize(85,81))
                self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                self.animation.start()               

                self.animation2 = QPropertyAnimation(self.ui.settings_bar, b"geometry")
                self.animation2.setDuration(1000)
                self.animation2.setEndValue(QtCore.QRect(0,650,85,81))
                self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                self.animation2.start()  

                if self.ui.toggle_bar.width() == 85:
                    self.animation3 = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation3.setDuration(1000)
                    self.animation3.setEndValue(QtCore.QSize(85,641))
                    self.animation3.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation3.start()
                else:
                    self.animation4 = QPropertyAnimation(self.ui.toggle_bar, b"size")
                    self.animation4.setDuration(1000)
                    self.animation4.setEndValue(QtCore.QSize(348,641))
                    self.animation4.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
                    self.animation4.start()                    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())