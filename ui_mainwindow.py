"""
################################################################################
##                    Форма главного окна программы
#################################################################################
"""

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMenu, QMenuBar, QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 599)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 182, 226, 175), stop:1 rgba(255, 255, 255, 255));")
        self.action_admin = QAction(MainWindow)
        self.action_admin.setObjectName(u"action_admin")
        self.action_user = QAction(MainWindow)
        self.action_user.setObjectName(u"action_user")
        self.action_time = QAction(MainWindow)
        self.action_time.setObjectName(u"action_time")
        self.action_remark = QAction(MainWindow)
        self.action_remark.setObjectName(u"action_remark")
        self.action_plan = QAction(MainWindow)
        self.action_plan.setObjectName(u"action_plan")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_worker = QAction(MainWindow)
        self.action_worker.setObjectName(u"action_worker")
        self.action_station = QAction(MainWindow)
        self.action_station.setObjectName(u"action_station")
        self.action_module = QAction(MainWindow)
        self.action_module.setObjectName(u"action_module")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action__new_password = QAction(MainWindow)
        self.action__new_password.setObjectName(u"action__new_password")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(0, 50))
        self.label_name.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.393443 rgba(35, 163, 255, 194), stop:1 rgba(255, 255, 255, 255));")
        self.label_name.setFrameShadow(QFrame.Raised)
        self.label_name.setTextFormat(Qt.PlainText)
        self.label_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_name)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setItalic(True)
        self.button_1.setFont(font1)
        self.button_1.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout.addWidget(self.button_1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setFont(font1)
        self.button_2.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout.addWidget(self.button_2)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setFont(font1)
        self.button_3.setStyleSheet(u"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")

        self.verticalLayout.addWidget(self.button_3)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)

        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setStyleSheet(u"border-image: url(:/res/1.png);")

        self.gridLayout.addWidget(self.label_logo, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.label_fon = QLabel(self.centralwidget)
        self.label_fon.setObjectName(u"label_fon")
        self.label_fon.setStyleSheet(u"border-image: url(:/res/2.png);")

        self.horizontalLayout.addWidget(self.label_fon)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.Button_exit = QPushButton(self.centralwidget)
        self.Button_exit.setObjectName(u"Button_exit")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(True)
        self.Button_exit.setFont(font2)
        self.Button_exit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.169399 rgba(246, 14, 0, 229), stop:1 rgba(255, 255, 255, 255));")

        self.gridLayout_2.addWidget(self.Button_exit, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 22))
        self.menu_servis = QMenu(self.menubar)
        self.menu_servis.setObjectName(u"menu_servis")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_servis.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_servis.addAction(self.action_admin)
        self.menu_servis.addAction(self.action_user)
        self.menu_servis.addSeparator()
        self.menu_servis.addAction(self.action_time)
        self.menu_servis.addAction(self.action_remark)
        self.menu_servis.addAction(self.action_plan)
        self.menu_servis.addSeparator()
        self.menu_servis.addAction(self.action_exit)
        self.menu_edit.addAction(self.action_worker)
        self.menu_edit.addAction(self.action_station)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action__new_password)
        self.menu_help.addAction(self.action_module)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(MainWindow)
        self.action_exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_admin.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_user.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.action_time.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0442 \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.action_remark.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0439", None))
        self.action_plan.setText(QCoreApplication.translate("MainWindow", u" \u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_worker.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.action_station.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0446\u0438\u0438 \u0438 \u043f\u0435\u0440\u0435\u0433\u043e\u043d\u044b", None))
        self.action_module.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u0438", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action__new_password.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0442 \u0440\u0430\u0431\u043e\u0442\u044b \u0420\u0412\u0411", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u0442 \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0439", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442", None))
        self.label_logo.setText("")
        self.label_fon.setText("")
        self.Button_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.menu_servis.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u044b", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

