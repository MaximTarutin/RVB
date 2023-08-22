# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'time_tracking.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
#################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1346, 689)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 182, 226, 175), stop:1 rgba(255, 255, 255, 255));")
        self.action_admin = QAction(MainWindow)
        self.action_admin.setObjectName(u"action_admin")
        self.action_user = QAction(MainWindow)
        self.action_user.setObjectName(u"action_user")
        self.action_return = QAction(MainWindow)
        self.action_return.setObjectName(u"action_return")
        self.action_workers = QAction(MainWindow)
        self.action_workers.setObjectName(u"action_workers")
        self.action_stations = QAction(MainWindow)
        self.action_stations.setObjectName(u"action_stations")
        self.action_password = QAction(MainWindow)
        self.action_password.setObjectName(u"action_password")
        self.action_moduls = QAction(MainWindow)
        self.action_moduls.setObjectName(u"action_moduls")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_otgul = QAction(MainWindow)
        self.action_otgul.setObjectName(u"action_otgul")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(1178, 23, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButton_return = QPushButton(self.centralwidget)
        self.pushButton_return.setObjectName(u"pushButton_return")
        self.pushButton_return.setMaximumSize(QSize(80, 31))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_return.setFont(font)
        self.pushButton_return.setStyleSheet(u"background-color: rgb(235, 235, 235);")

        self.horizontalLayout_3.addWidget(self.pushButton_return)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 7, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(951, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_name.setFont(font1)
        self.label_name.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.label_name.setFrameShape(QFrame.NoFrame)
        self.label_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_name)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_20 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_20)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(31, 21))
        self.label.setMaximumSize(QSize(31, 21))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: yellow;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 1, 2, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(131, 21))
        self.label_3.setMaximumSize(QSize(131, 21))
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 0, 3, 2, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(31, 21))
        self.label_7.setMaximumSize(QSize(31, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: lightgreen;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 4, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 0, 5, 2, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(131, 21))
        self.label_8.setMaximumSize(QSize(131, 21))
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 6, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 0, 7, 2, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(31, 21))
        self.label_10.setMaximumSize(QSize(31, 21))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color: cyan;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 8, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 0, 9, 2, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(131, 21))
        self.label_9.setMaximumSize(QSize(131, 21))
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 0, 10, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 1, 4, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 1, 6, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 1, 10, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 2, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 2, 8, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_19, 2, 11, 2, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(31, 21))
        self.label_14.setMaximumSize(QSize(31, 21))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color: pink;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 2, 12, 2, 1)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 2, 13, 2, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(131, 21))
        self.label_13.setMaximumSize(QSize(131, 21))
        self.label_13.setFont(font)

        self.gridLayout_2.addWidget(self.label_13, 2, 14, 2, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(31, 21))
        self.label_2.setMaximumSize(QSize(31, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: red;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 3, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(131, 21))
        self.label_4.setMaximumSize(QSize(131, 21))
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 3, 2, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_16, 3, 3, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(31, 21))
        self.label_6.setMaximumSize(QSize(31, 21))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: lightblue;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 3, 4, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 3, 5, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(131, 21))
        self.label_5.setMaximumSize(QSize(131, 21))
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 3, 6, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 3, 7, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(31, 21))
        self.label_11.setMaximumSize(QSize(31, 21))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"background-color: magenta;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 3, 8, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 3, 9, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(131, 21))
        self.label_12.setMaximumSize(QSize(131, 21))
        self.label_12.setFont(font)

        self.gridLayout_2.addWidget(self.label_12, 3, 10, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalSpacer_21 = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_21)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_25)

        self.checkBox_korr = QCheckBox(self.centralwidget)
        self.checkBox_korr.setObjectName(u"checkBox_korr")
        self.checkBox_korr.setEnabled(True)
        self.checkBox_korr.setMinimumSize(QSize(250, 30))
        self.checkBox_korr.setMaximumSize(QSize(250, 30))
        self.checkBox_korr.setFont(font)
        self.checkBox_korr.setAcceptDrops(False)
        self.checkBox_korr.setStyleSheet(u"background-color: rgb(201, 239, 255);")
        self.checkBox_korr.setChecked(False)

        self.horizontalLayout_4.addWidget(self.checkBox_korr)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_26)

        self.pushButton_Otgul = QPushButton(self.centralwidget)
        self.pushButton_Otgul.setObjectName(u"pushButton_Otgul")
        self.pushButton_Otgul.setMinimumSize(QSize(120, 25))
        self.pushButton_Otgul.setMaximumSize(QSize(120, 25))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.pushButton_Otgul.setFont(font2)
        self.pushButton_Otgul.setStyleSheet(u"background-color: rgb(229, 229, 229);")

        self.horizontalLayout_4.addWidget(self.pushButton_Otgul)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_24)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 5, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_month = QComboBox(self.centralwidget)
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.addItem("")
        self.comboBox_month.setObjectName(u"comboBox_month")
        self.comboBox_month.setMaximumSize(QSize(171, 31))
        self.comboBox_month.setFont(font)
        self.comboBox_month.setStyleSheet(u"background-color: rgb(229, 229, 229);")

        self.horizontalLayout.addWidget(self.comboBox_month)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.spinBox_year = QSpinBox(self.centralwidget)
        self.spinBox_year.setObjectName(u"spinBox_year")
        self.spinBox_year.setMaximumSize(QSize(71, 31))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.spinBox_year.setFont(font3)
        self.spinBox_year.setStyleSheet(u"background-color: rgb(229, 229, 229);")
        self.spinBox_year.setMinimum(2022)
        self.spinBox_year.setMaximum(9999)

        self.horizontalLayout.addWidget(self.spinBox_year)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_22)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(120, 25))
        self.pushButton_save.setMaximumSize(QSize(120, 25))
        self.pushButton_save.setFont(font2)
        self.pushButton_save.setStyleSheet(u"background-color: rgb(229, 229, 229);")

        self.horizontalLayout_5.addWidget(self.pushButton_save)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_23)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        self.tableView.setStyleSheet(u"background-color: rgb(235, 235, 235);")

        self.gridLayout.addWidget(self.tableView, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(17, 25, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_10, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1346, 22))
        self.menu_service = QMenu(self.menubar)
        self.menu_service.setObjectName(u"menu_service")
        self.menu_editor = QMenu(self.menubar)
        self.menu_editor.setObjectName(u"menu_editor")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_service.menuAction())
        self.menubar.addAction(self.menu_editor.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_service.addAction(self.action_admin)
        self.menu_service.addAction(self.action_user)
        self.menu_service.addSeparator()
        self.menu_service.addAction(self.action_otgul)
        self.menu_service.addSeparator()
        self.menu_service.addAction(self.action_return)
        self.menu_editor.addAction(self.action_workers)
        self.menu_editor.addAction(self.action_stations)
        self.menu_editor.addSeparator()
        self.menu_editor.addAction(self.action_password)
        self.menu_help.addAction(self.action_moduls)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.action_admin.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_user.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c &\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.action_return.setText(QCoreApplication.translate("MainWindow", u"&\u0412\u043e\u0437\u0432\u0440\u0430\u0442", None))
        self.action_workers.setText(QCoreApplication.translate("MainWindow", u"&\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.action_stations.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0446\u0438\u0438 \u0438 &\u043f\u0435\u0440\u0435\u0433\u043e\u043d\u044b", None))
        self.action_password.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_moduls.setText(QCoreApplication.translate("MainWindow", u"&\u041c\u043e\u0434\u0443\u043b\u0438", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"&\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_otgul.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u043d\u0430\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u0430 \u043e\u0442\u0433\u0443\u043b\u043e\u0432", None))
        self.pushButton_return.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0442 \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0443\u0441\u043a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u043e\u0439", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0423", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0431\u0430", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0411", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043b\u044c\u043d\u0438\u0447\u043d\u044b\u0439", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0443\u043b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041d", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0433\u0443\u043b", None))
        self.checkBox_korr.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.pushButton_Otgul.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0433\u0443\u043b\u044b", None))
        self.comboBox_month.setItemText(0, QCoreApplication.translate("MainWindow", u"\u042f\u043d\u0432\u0430\u0440\u044c", None))
        self.comboBox_month.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0424\u0435\u0432\u0440\u0430\u043b\u044c", None))
        self.comboBox_month.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0442", None))
        self.comboBox_month.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0410\u043f\u0440\u0435\u043b\u044c", None))
        self.comboBox_month.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0439", None))
        self.comboBox_month.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0418\u044e\u043d\u044c", None))
        self.comboBox_month.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0418\u044e\u043b\u044c", None))
        self.comboBox_month.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0433\u0443\u0441\u0442", None))
        self.comboBox_month.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043d\u0442\u044f\u0431\u0440\u044c", None))
        self.comboBox_month.setItemText(9, QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0442\u044f\u0431\u0440\u044c", None))
        self.comboBox_month.setItemText(10, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u044f\u0431\u0440\u044c", None))
        self.comboBox_month.setItemText(11, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u0430\u0431\u0440\u044c", None))

        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.menu_service.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        self.menu_editor.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u044b", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

