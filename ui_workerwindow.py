# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workerwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_workerWindow(object):
    def setupUi(self, workerWindow):
        if not workerWindow.objectName():
            workerWindow.setObjectName(u"workerWindow")
        workerWindow.setWindowModality(Qt.ApplicationModal)
        workerWindow.resize(1200, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(workerWindow.sizePolicy().hasHeightForWidth())
        workerWindow.setSizePolicy(sizePolicy)
        workerWindow.setMinimumSize(QSize(1200, 0))
        workerWindow.setMaximumSize(QSize(1200, 600))
        workerWindow.setStyleSheet(u"background-color: rgb(231, 255, 252);")
        self.action_admin = QAction(workerWindow)
        self.action_admin.setObjectName(u"action_admin")
        self.action_user = QAction(workerWindow)
        self.action_user.setObjectName(u"action_user")
        self.action_return = QAction(workerWindow)
        self.action_return.setObjectName(u"action_return")
        self.action_module = QAction(workerWindow)
        self.action_module.setObjectName(u"action_module")
        self.action_about = QAction(workerWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(workerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 127);\n"
"background-color: rgb(255, 250, 181);")
        self.label.setFrameShape(QFrame.Panel)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.button_add = QPushButton(self.centralwidget)
        self.button_add.setObjectName(u"button_add")
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        self.button_add.setMinimumSize(QSize(220, 25))
        self.button_add.setMaximumSize(QSize(220, 25))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.button_add.setFont(font1)
        self.button_add.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.verticalLayout.addWidget(self.button_add)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_del = QPushButton(self.centralwidget)
        self.button_del.setObjectName(u"button_del")
        sizePolicy.setHeightForWidth(self.button_del.sizePolicy().hasHeightForWidth())
        self.button_del.setSizePolicy(sizePolicy)
        self.button_del.setMinimumSize(QSize(220, 25))
        self.button_del.setMaximumSize(QSize(220, 25))
        self.button_del.setFont(font1)
        self.button_del.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.verticalLayout.addWidget(self.button_del)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy2)
        self.tableView.setMinimumSize(QSize(533, 0))
        self.tableView.setMaximumSize(QSize(533, 16777215))
        self.tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.tableView)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(628, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.button_return = QPushButton(self.centralwidget)
        self.button_return.setObjectName(u"button_return")
        sizePolicy.setHeightForWidth(self.button_return.sizePolicy().hasHeightForWidth())
        self.button_return.setSizePolicy(sizePolicy)
        self.button_return.setFont(font1)
        self.button_return.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.horizontalLayout_2.addWidget(self.button_return)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        workerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(workerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menubar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 182, 226, 175), stop:1 rgba(255, 255, 255, 255));")
        self.menu_service = QMenu(self.menubar)
        self.menu_service.setObjectName(u"menu_service")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        workerWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(workerWindow)
        self.statusbar.setObjectName(u"statusbar")
        workerWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_service.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_service.addAction(self.action_admin)
        self.menu_service.addAction(self.action_user)
        self.menu_service.addSeparator()
        self.menu_service.addAction(self.action_return)
        self.menu_help.addAction(self.action_module)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(workerWindow)

        QMetaObject.connectSlotsByName(workerWindow)
    # setupUi

    def retranslateUi(self, workerWindow):
        workerWindow.setWindowTitle(QCoreApplication.translate("workerWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.action_admin.setText(QCoreApplication.translate("workerWindow", u"\u0420\u0435\u0436\u0438\u043c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_user.setText(QCoreApplication.translate("workerWindow", u"\u0420\u0435\u0436\u0438\u043c &\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.action_return.setText(QCoreApplication.translate("workerWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u044b\u0439 \u044d\u043a\u0440\u0430\u043d", None))
        self.action_module.setText(QCoreApplication.translate("workerWindow", u"&\u041c\u043e\u0434\u0443\u043b\u0438", None))
        self.action_about.setText(QCoreApplication.translate("workerWindow", u"\u041e &\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label.setText(QCoreApplication.translate("workerWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.button_add.setText(QCoreApplication.translate("workerWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.button_del.setText(QCoreApplication.translate("workerWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.button_return.setText(QCoreApplication.translate("workerWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.menu_service.setTitle(QCoreApplication.translate("workerWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        self.menu_help.setTitle(QCoreApplication.translate("workerWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

