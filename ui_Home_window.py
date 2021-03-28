# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home_windowjmSpOE.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: none;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(6, 6, 1270, 790))
        self.container.setStyleSheet(u"background-color: rgb(121, 121, 145);\n"
"border-radius: 10px;")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.background = QFrame(self.container)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(15, 15, 1240, 760))
        self.background.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(45, 45, 45);\n"
"\n"
"}")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.background)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 15, 1220, 730))
        self.frame_2.setStyleSheet(u"border: none;\n"
"background-color: rgb(61, 61, 61);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.toggle_bar = QFrame(self.frame_2)
        self.toggle_bar.setObjectName(u"toggle_bar")
        self.toggle_bar.setGeometry(QRect(0, 0, 171, 731))
        self.toggle_bar.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 155, 255);\n"
"border-radius: 10px;\n"
"border: none;")
        self.toggle_bar.setFrameShape(QFrame.StyledPanel)
        self.toggle_bar.setFrameShadow(QFrame.Raised)
        self.Home_button = QPushButton(self.toggle_bar)
        self.Home_button.setObjectName(u"Home_button")
        self.Home_button.setGeometry(QRect(5, 5, 161, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Home_button.setFont(font)
        self.Home_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(55, 55, 55);\n"
"	border: 3px solid rgb(61,61,61);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 3px solid rgb(61, 61, 61)\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(61, 61, 61);\n"
"	color: rgb(255, 170, 255);\n"
"	border: 4px solid rgb(45, 45, 45);\n"
"	border-radius: 10px\n"
"\n"
"}")
        self.Home_button.setIconSize(QSize(50, 60))
        self.Time_table = QPushButton(self.toggle_bar)
        self.Time_table.setObjectName(u"Time_table")
        self.Time_table.setGeometry(QRect(5, 70, 161, 61))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.Time_table.setFont(font1)
        self.Time_table.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(55, 55, 55);\n"
"	border: 3px solid rgb(61,61,61);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 3px solid rgb(61, 61, 61)\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(61, 61, 61);\n"
"	color: rgb(255, 255 255);\n"
"	border: 4px solid rgb(45, 45, 45);\n"
"	border-radius: 10px\n"
"\n"
"}")
        self.Time_table.setIconSize(QSize(50, 60))
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(180, 10, 1031, 711))
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.close_button_home = QPushButton(self.Home)
        self.close_button_home.setObjectName(u"close_button_home")
        self.close_button_home.setGeometry(QRect(1010, 0, 20, 20))
        self.close_button_home.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(249, 98, 93);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(249, 163, 161);\n"
"\n"
"\n"
"}")
        self.stackedWidget.addWidget(self.Home)
        self.Chemistry = QWidget()
        self.Chemistry.setObjectName(u"Chemistry")
        self.close_button_home_3 = QPushButton(self.Chemistry)
        self.close_button_home_3.setObjectName(u"close_button_home_3")
        self.close_button_home_3.setGeometry(QRect(1010, 0, 20, 20))
        self.close_button_home_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(249, 98, 93);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(249, 163, 161);\n"
"\n"
"\n"
"}")
        self.stackedWidget.addWidget(self.Chemistry)
        self.timetable = QWidget()
        self.timetable.setObjectName(u"timetable")
        self.tableWidget = QTableWidget(self.timetable)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 9):
            self.tableWidget.setRowCount(9)
        font3 = QFont()
        font3.setFamily(u"Cambria")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font3);
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 90, 1031, 581))
        font4 = QFont()
        font4.setPointSize(15)
        self.tableWidget.setFont(font4)
        self.tableWidget.setStyleSheet(u"\n"
"QTableWidget\n"
"{\n"
"	background-color: rgb(61, 61, 61);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	background-color: rgb(61, 61, 61);\n"
"	color: white;\n"
"	border: none;\n"
"	margin: 5px;\n"
"	text-align: center;\n"
"	font-family:Segoe UI ;\n"
"	font-size:25px;\n"
"	text-align:center;\n"
"} \n"
"\n"
"\n"
"QTableWidget::item::selected \n"
"{\n"
"	background-color: rgb(40, 40, 40);\n"
"	color: white;\n"
"	border: none;\n"
"	margin: 5px;\n"
"	text-align: right;\n"
"	font-family:Segoe UI ;\n"
"	font-size:25px;\n"
"	text-align:center;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(142)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(56)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QLabel(self.timetable)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 0, 421, 81))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(48)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 155, 255);\n"
"border-radius: 10px;\n"
"border: none;")
        self.close_button_home_4 = QPushButton(self.timetable)
        self.close_button_home_4.setObjectName(u"close_button_home_4")
        self.close_button_home_4.setGeometry(QRect(1010, 0, 20, 20))
        self.close_button_home_4.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(249, 98, 93);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(249, 163, 161);\n"
"\n"
"\n"
"}")
        self.stackedWidget.addWidget(self.timetable)
        self.Physics = QWidget()
        self.Physics.setObjectName(u"Physics")
        self.close_button_home_2 = QPushButton(self.Physics)
        self.close_button_home_2.setObjectName(u"close_button_home_2")
        self.close_button_home_2.setGeometry(QRect(1010, 0, 20, 20))
        self.close_button_home_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(249, 98, 93);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(249, 163, 161);\n"
"\n"
"\n"
"}")
        self.stackedWidget.addWidget(self.Physics)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jaypee Public School", None))
        self.Home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Time_table.setText(QCoreApplication.translate("MainWindow", u"Time Table", None))
        self.close_button_home.setText("")
        self.close_button_home_3.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Slots No", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Monday", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Thusday", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Friday", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Saturday", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"I", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"II", None));
        ___qtablewidgetitem9 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"III", None));
        ___qtablewidgetitem10 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"IV", None));
        ___qtablewidgetitem11 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"V", None));
        ___qtablewidgetitem12 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"VI", None));
        ___qtablewidgetitem13 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"VII", None));
        ___qtablewidgetitem14 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"VIII", None));
        ___qtablewidgetitem15 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"IX", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Time Table</span></p></body></html>", None))
        self.close_button_home_4.setText("")
        self.close_button_home_2.setText("")
    # retranslateUi

