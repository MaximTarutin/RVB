# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableView,
    QWidget)

class Ui_PlanWindow(object):
    def setupUi(self, PlanWindow):
        if not PlanWindow.objectName():
            PlanWindow.setObjectName(u"PlanWindow")
        PlanWindow.setWindowModality(Qt.ApplicationModal)
        PlanWindow.resize(1200, 780)
        PlanWindow.setMinimumSize(QSize(1200, 780))
        PlanWindow.setStyleSheet(u"background-color: rgb(172, 255, 249);")
        self.action_admin = QAction(PlanWindow)
        self.action_admin.setObjectName(u"action_admin")
        self.action_user = QAction(PlanWindow)
        self.action_user.setObjectName(u"action_user")
        self.action_workers = QAction(PlanWindow)
        self.action_workers.setObjectName(u"action_workers")
        self.action_stations = QAction(PlanWindow)
        self.action_stations.setObjectName(u"action_stations")
        self.action_admin_edit = QAction(PlanWindow)
        self.action_admin_edit.setObjectName(u"action_admin_edit")
        self.action_moduls = QAction(PlanWindow)
        self.action_moduls.setObjectName(u"action_moduls")
        self.action_about = QAction(PlanWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_return = QAction(PlanWindow)
        self.action_return.setObjectName(u"action_return")
        self.action_plan_edit = QAction(PlanWindow)
        self.action_plan_edit.setObjectName(u"action_plan_edit")
        self.centralwidget = QWidget(PlanWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 5, 5, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 11, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 7, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(170, 25))
        self.checkBox.setMaximumSize(QSize(170, 25))
        self.checkBox.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setToolTipDuration(-1)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setIconSize(QSize(25, 25))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)

        self.gridLayout.addWidget(self.checkBox, 5, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 6, 1, 1)

        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMinimumSize(QSize(125, 25))
        self.pushButton_add.setMaximumSize(QSize(125, 25))
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout.addWidget(self.pushButton_add, 12, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 0, 1, 3)

        self.pushButton_return = QPushButton(self.centralwidget)
        self.pushButton_return.setObjectName(u"pushButton_return")
        self.pushButton_return.setMinimumSize(QSize(100, 25))
        self.pushButton_return.setMaximumSize(QSize(100, 25))
        self.pushButton_return.setFont(font)
        self.pushButton_return.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout.addWidget(self.pushButton_return, 12, 9, 1, 1)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(125, 25))
        self.pushButton_delete.setMaximumSize(QSize(125, 25))
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.gridLayout.addWidget(self.pushButton_delete, 12, 7, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_initial = QLabel(self.centralwidget)
        self.label_initial.setObjectName(u"label_initial")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_initial.sizePolicy().hasHeightForWidth())
        self.label_initial.setSizePolicy(sizePolicy)
        self.label_initial.setMinimumSize(QSize(50, 25))
        self.label_initial.setMaximumSize(QSize(50, 25))
        self.label_initial.setFont(font)
        self.label_initial.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_initial)

        self.initial_dateEdit = QDateEdit(self.centralwidget)
        self.initial_dateEdit.setObjectName(u"initial_dateEdit")
        self.initial_dateEdit.setMinimumSize(QSize(120, 25))
        self.initial_dateEdit.setMaximumSize(QSize(120, 25))
        self.initial_dateEdit.setFont(font)
        self.initial_dateEdit.setTabletTracking(False)
        self.initial_dateEdit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.initial_dateEdit.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.initial_dateEdit.setMinimumDate(QDate(2023, 1, 1))
        self.initial_dateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.initial_dateEdit)

        self.label_initial_2 = QLabel(self.centralwidget)
        self.label_initial_2.setObjectName(u"label_initial_2")
        sizePolicy.setHeightForWidth(self.label_initial_2.sizePolicy().hasHeightForWidth())
        self.label_initial_2.setSizePolicy(sizePolicy)
        self.label_initial_2.setMinimumSize(QSize(50, 25))
        self.label_initial_2.setMaximumSize(QSize(50, 25))
        self.label_initial_2.setFont(font)
        self.label_initial_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_initial_2)

        self.ultimate_dateEdit = QDateEdit(self.centralwidget)
        self.ultimate_dateEdit.setObjectName(u"ultimate_dateEdit")
        self.ultimate_dateEdit.setMinimumSize(QSize(120, 25))
        self.ultimate_dateEdit.setMaximumSize(QSize(120, 25))
        self.ultimate_dateEdit.setFont(font)
        self.ultimate_dateEdit.setTabletTracking(False)
        self.ultimate_dateEdit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ultimate_dateEdit.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.ultimate_dateEdit.setMinimumDate(QDate(2023, 1, 1))
        self.ultimate_dateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.ultimate_dateEdit)

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_initial_3 = QLabel(self.centralwidget)
        self.label_initial_3.setObjectName(u"label_initial_3")
        sizePolicy.setHeightForWidth(self.label_initial_3.sizePolicy().hasHeightForWidth())
        self.label_initial_3.setSizePolicy(sizePolicy)
        self.label_initial_3.setMinimumSize(QSize(100, 25))
        self.label_initial_3.setMaximumSize(QSize(100, 25))
        self.label_initial_3.setFont(font)
        self.label_initial_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_initial_3)

        self.comboBox_workers = QComboBox(self.centralwidget)
        self.comboBox_workers.setObjectName(u"comboBox_workers")
        self.comboBox_workers.setMinimumSize(QSize(170, 25))
        self.comboBox_workers.setMaximumSize(QSize(170, 25))
        self.comboBox_workers.setStyleSheet(u"background-color: rgb(248, 248, 248);")

        self.horizontalLayout.addWidget(self.comboBox_workers)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_initial_4 = QLabel(self.centralwidget)
        self.label_initial_4.setObjectName(u"label_initial_4")
        sizePolicy.setHeightForWidth(self.label_initial_4.sizePolicy().hasHeightForWidth())
        self.label_initial_4.setSizePolicy(sizePolicy)
        self.label_initial_4.setMinimumSize(QSize(150, 25))
        self.label_initial_4.setMaximumSize(QSize(150, 25))
        self.label_initial_4.setFont(font)
        self.label_initial_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_initial_4)

        self.comboBox_station = QComboBox(self.centralwidget)
        self.comboBox_station.setObjectName(u"comboBox_station")
        self.comboBox_station.setMinimumSize(QSize(230, 25))
        self.comboBox_station.setMaximumSize(QSize(230, 25))
        self.comboBox_station.setStyleSheet(u"background-color: rgb(248, 248, 248);")

        self.horizontalLayout.addWidget(self.comboBox_station)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 10)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: rgb(247, 247, 247);")

        self.gridLayout.addWidget(self.tableView, 7, 0, 4, 10)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 4, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 8, 0, 1, 1)

        self.label_titul = QLabel(self.centralwidget)
        self.label_titul.setObjectName(u"label_titul")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.label_titul.setFont(font1)
        self.label_titul.setStyleSheet(u"color: rgb(0, 0, 235);")
        self.label_titul.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_titul, 1, 6, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        PlanWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PlanWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menubar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 219, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.menu_service = QMenu(self.menubar)
        self.menu_service.setObjectName(u"menu_service")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        PlanWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PlanWindow)
        self.statusbar.setObjectName(u"statusbar")
        PlanWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_service.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_service.addAction(self.action_admin)
        self.menu_service.addAction(self.action_user)
        self.menu_service.addSeparator()
        self.menu_service.addAction(self.action_return)
        self.menu_edit.addAction(self.action_workers)
        self.menu_edit.addAction(self.action_stations)
        self.menu_edit.addAction(self.action_plan_edit)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_admin_edit)
        self.menu_help.addAction(self.action_moduls)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(PlanWindow)

        QMetaObject.connectSlotsByName(PlanWindow)
    # setupUi

    def retranslateUi(self, PlanWindow):
        PlanWindow.setWindowTitle(QCoreApplication.translate("PlanWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a", None))
        self.action_admin.setText(QCoreApplication.translate("PlanWindow", u"\u0420\u0435\u0436\u0438\u043c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_user.setText(QCoreApplication.translate("PlanWindow", u"\u0420\u0435\u0436\u0438\u043c &\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.action_workers.setText(QCoreApplication.translate("PlanWindow", u"&\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.action_stations.setText(QCoreApplication.translate("PlanWindow", u"\u0421\u0442\u0430\u043d\u0446\u0438\u0438 \u0438 &\u043f\u0435\u0440\u0435\u0433\u043e\u043d\u044b", None))
        self.action_admin_edit.setText(QCoreApplication.translate("PlanWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_moduls.setText(QCoreApplication.translate("PlanWindow", u"&\u041c\u043e\u0434\u0443\u043b\u0438", None))
        self.action_about.setText(QCoreApplication.translate("PlanWindow", u"&\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_return.setText(QCoreApplication.translate("PlanWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.action_plan_edit.setText(QCoreApplication.translate("PlanWindow", u"&\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442", None))
        self.checkBox.setText(QCoreApplication.translate("PlanWindow", u"    \u0412\u044b\u0431\u043e\u0440 \u043f\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0443", None))
        self.pushButton_add.setText(QCoreApplication.translate("PlanWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
        self.pushButton_return.setText(QCoreApplication.translate("PlanWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_delete.setText(QCoreApplication.translate("PlanWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0438", None))
        self.label_initial.setText(QCoreApplication.translate("PlanWindow", u"\u0441", None))
        self.label_initial_2.setText(QCoreApplication.translate("PlanWindow", u"\u043f\u043e", None))
        self.label_initial_3.setText(QCoreApplication.translate("PlanWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a:", None))
        self.label_initial_4.setText(QCoreApplication.translate("PlanWindow", u"\u0421\u0442\u0430\u043d\u0446\u0438\u044f (\u043f\u0435\u0440\u0435\u0433\u043e\u043d):", None))
        self.label_titul.setText(QCoreApplication.translate("PlanWindow", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442", None))
        self.menu_service.setTitle(QCoreApplication.translate("PlanWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        self.menu_edit.setTitle(QCoreApplication.translate("PlanWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u044b", None))
        self.menu_help.setTitle(QCoreApplication.translate("PlanWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

