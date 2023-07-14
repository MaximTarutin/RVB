# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_CommentsView(object):
    def setupUi(self, CommentsView):
        if not CommentsView.objectName():
            CommentsView.setObjectName(u"CommentsView")
        CommentsView.setWindowModality(Qt.ApplicationModal)
        CommentsView.resize(1240, 731)
        self.action_Admin = QAction(CommentsView)
        self.action_Admin.setObjectName(u"action_Admin")
        self.action_User = QAction(CommentsView)
        self.action_User.setObjectName(u"action_User")
        self.action_Excel = QAction(CommentsView)
        self.action_Excel.setObjectName(u"action_Excel")
        self.action_Return = QAction(CommentsView)
        self.action_Return.setObjectName(u"action_Return")
        self.action_Worker = QAction(CommentsView)
        self.action_Worker.setObjectName(u"action_Worker")
        self.action_Station = QAction(CommentsView)
        self.action_Station.setObjectName(u"action_Station")
        self.action_Password = QAction(CommentsView)
        self.action_Password.setObjectName(u"action_Password")
        self.action_Moduls = QAction(CommentsView)
        self.action_Moduls.setObjectName(u"action_Moduls")
        self.action_About = QAction(CommentsView)
        self.action_About.setObjectName(u"action_About")
        self.centralwidget = QWidget(CommentsView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.label_head = QLabel(self.centralwidget)
        self.label_head.setObjectName(u"label_head")

        self.horizontalLayout.addWidget(self.label_head)

        self.horizontalSpacer_8 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_commis = QLabel(self.centralwidget)
        self.label_commis.setObjectName(u"label_commis")
        self.label_commis.setMinimumSize(QSize(170, 30))
        self.label_commis.setMaximumSize(QSize(170, 30))

        self.gridLayout.addWidget(self.label_commis, 0, 1, 1, 1)

        self.label_station = QLabel(self.centralwidget)
        self.label_station.setObjectName(u"label_station")
        self.label_station.setMinimumSize(QSize(180, 30))
        self.label_station.setMaximumSize(QSize(180, 30))

        self.gridLayout.addWidget(self.label_station, 0, 3, 1, 1)

        self.label_auditor = QLabel(self.centralwidget)
        self.label_auditor.setObjectName(u"label_auditor")
        self.label_auditor.setMinimumSize(QSize(120, 30))
        self.label_auditor.setMaximumSize(QSize(120, 30))

        self.gridLayout.addWidget(self.label_auditor, 0, 5, 1, 1)

        self.label_worker = QLabel(self.centralwidget)
        self.label_worker.setObjectName(u"label_worker")
        self.label_worker.setMinimumSize(QSize(150, 30))
        self.label_worker.setMaximumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.label_worker, 0, 7, 1, 1)

        self.label_performance = QLabel(self.centralwidget)
        self.label_performance.setObjectName(u"label_performance")
        self.label_performance.setMinimumSize(QSize(120, 30))
        self.label_performance.setMaximumSize(QSize(120, 30))

        self.gridLayout.addWidget(self.label_performance, 0, 9, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.commis_Box = QComboBox(self.centralwidget)
        self.commis_Box.addItem("")
        self.commis_Box.addItem("")
        self.commis_Box.addItem("")
        self.commis_Box.addItem("")
        self.commis_Box.addItem("")
        self.commis_Box.addItem("")
        self.commis_Box.addItem("")
        self.commis_Box.setObjectName(u"commis_Box")
        self.commis_Box.setMinimumSize(QSize(170, 30))
        self.commis_Box.setMaximumSize(QSize(170, 30))

        self.gridLayout.addWidget(self.commis_Box, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.station_Box = QComboBox(self.centralwidget)
        self.station_Box.setObjectName(u"station_Box")
        self.station_Box.setMinimumSize(QSize(210, 30))
        self.station_Box.setMaximumSize(QSize(210, 30))

        self.gridLayout.addWidget(self.station_Box, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 6, 1, 1)

        self.worker_Box = QComboBox(self.centralwidget)
        self.worker_Box.setObjectName(u"worker_Box")
        self.worker_Box.setMinimumSize(QSize(150, 30))
        self.worker_Box.setMaximumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.worker_Box, 1, 7, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 8, 1, 1)

        self.performance_Box = QComboBox(self.centralwidget)
        self.performance_Box.addItem("")
        self.performance_Box.addItem("")
        self.performance_Box.addItem("")
        self.performance_Box.setObjectName(u"performance_Box")
        self.performance_Box.setMinimumSize(QSize(150, 30))
        self.performance_Box.setMaximumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.performance_Box, 1, 9, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 10, 1, 1)

        self.auditor_Box = QComboBox(self.centralwidget)
        self.auditor_Box.setObjectName(u"auditor_Box")
        self.auditor_Box.setMinimumSize(QSize(210, 30))
        self.auditor_Box.setMaximumSize(QSize(210, 30))

        self.gridLayout.addWidget(self.auditor_Box, 1, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.edit_checkBox = QCheckBox(self.centralwidget)
        self.edit_checkBox.setObjectName(u"edit_checkBox")

        self.horizontalLayout_3.addWidget(self.edit_checkBox)

        self.horizontalSpacer_12 = QSpacerItem(78, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)

        self.day_dateEdit = QDateEdit(self.centralwidget)
        self.day_dateEdit.setObjectName(u"day_dateEdit")
        self.day_dateEdit.setWrapping(False)
        self.day_dateEdit.setProperty("showGroupSeparator", False)
        self.day_dateEdit.setMinimumDateTime(QDateTime(QDate(1752, 9, 17), QTime(0, 0, 0)))
        self.day_dateEdit.setCalendarPopup(True)
        self.day_dateEdit.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_3.addWidget(self.day_dateEdit)

        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_18)

        self.edit_checkBox_data = QCheckBox(self.centralwidget)
        self.edit_checkBox_data.setObjectName(u"edit_checkBox_data")

        self.horizontalLayout_3.addWidget(self.edit_checkBox_data)

        self.horizontalSpacer_13 = QSpacerItem(578, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_2.addWidget(self.tableView)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.del_Button = QPushButton(self.centralwidget)
        self.del_Button.setObjectName(u"del_Button")
        self.del_Button.setMinimumSize(QSize(250, 40))
        self.del_Button.setMaximumSize(QSize(250, 40))

        self.horizontalLayout_4.addWidget(self.del_Button)

        self.horizontalSpacer_15 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.excel_Button = QPushButton(self.centralwidget)
        self.excel_Button.setObjectName(u"excel_Button")
        self.excel_Button.setMinimumSize(QSize(250, 40))
        self.excel_Button.setMaximumSize(QSize(250, 40))

        self.horizontalLayout_4.addWidget(self.excel_Button)

        self.horizontalSpacer_17 = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_17)

        self.return_pushButton = QPushButton(self.centralwidget)
        self.return_pushButton.setObjectName(u"return_pushButton")

        self.horizontalLayout_4.addWidget(self.return_pushButton)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        CommentsView.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CommentsView)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1240, 22))
        self.menu_Service = QMenu(self.menubar)
        self.menu_Service.setObjectName(u"menu_Service")
        self.menu_Editor = QMenu(self.menubar)
        self.menu_Editor.setObjectName(u"menu_Editor")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        CommentsView.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CommentsView)
        self.statusbar.setObjectName(u"statusbar")
        CommentsView.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_Service.menuAction())
        self.menubar.addAction(self.menu_Editor.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_Service.addAction(self.action_Admin)
        self.menu_Service.addAction(self.action_User)
        self.menu_Service.addSeparator()
        self.menu_Service.addAction(self.action_Excel)
        self.menu_Service.addSeparator()
        self.menu_Service.addAction(self.action_Return)
        self.menu_Editor.addAction(self.action_Worker)
        self.menu_Editor.addAction(self.action_Station)
        self.menu_Editor.addSeparator()
        self.menu_Editor.addAction(self.action_Password)
        self.menu_Help.addAction(self.action_Moduls)
        self.menu_Help.addAction(self.action_About)

        self.retranslateUi(CommentsView)

        QMetaObject.connectSlotsByName(CommentsView)
    # setupUi

    def retranslateUi(self, CommentsView):
        CommentsView.setWindowTitle(QCoreApplication.translate("CommentsView", u"CommentsView", None))
        self.action_Admin.setText(QCoreApplication.translate("CommentsView", u"\u0420\u0435\u0436\u0438\u043c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_User.setText(QCoreApplication.translate("CommentsView", u"\u0420\u0435\u0436\u0438\u043c &\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.action_Excel.setText(QCoreApplication.translate("CommentsView", u"&\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 Excel", None))
        self.action_Return.setText(QCoreApplication.translate("CommentsView", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.action_Worker.setText(QCoreApplication.translate("CommentsView", u"&\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.action_Station.setText(QCoreApplication.translate("CommentsView", u"\u0421\u0442\u0430\u043d\u0446\u0438\u0438 \u0438 &\u043f\u0435\u0440\u0435\u0433\u043e\u043d\u044b", None))
        self.action_Password.setText(QCoreApplication.translate("CommentsView", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_Moduls.setText(QCoreApplication.translate("CommentsView", u"&\u041c\u043e\u0434\u0443\u043b\u0438", None))
        self.action_About.setText(QCoreApplication.translate("CommentsView", u"&\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_head.setText(QCoreApplication.translate("CommentsView", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#f4018a;\">\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0438 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0439</span></p></body></html>", None))
        self.label_commis.setText(QCoreApplication.translate("CommentsView", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f:", None))
        self.label_station.setText(QCoreApplication.translate("CommentsView", u"\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u0438\u043b\u0438 \u043f\u0435\u0440\u0435\u0433\u043e\u043d:", None))
        self.label_auditor.setText(QCoreApplication.translate("CommentsView", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u044e\u0449\u0438\u0439:", None))
        self.label_worker.setText(QCoreApplication.translate("CommentsView", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c:", None))
        self.label_performance.setText(QCoreApplication.translate("CommentsView", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435:", None))
        self.commis_Box.setItemText(0, "")
        self.commis_Box.setItemText(1, QCoreApplication.translate("CommentsView", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a \u0434\u043e\u0440\u043e\u0433\u0438", None))
        self.commis_Box.setItemText(2, QCoreApplication.translate("CommentsView", u"\u0417\u0430\u043c. \u043f\u043e \u0440\u0435\u0433\u0438\u043e\u043d\u0443", None))
        self.commis_Box.setItemText(3, QCoreApplication.translate("CommentsView", u"\u0420\u0435\u0432\u0438\u0437\u043e\u0440\u0441\u043a\u0438\u0439 \u0430\u043f\u043f\u0430\u0440\u0430\u0442", None))
        self.commis_Box.setItemText(4, QCoreApplication.translate("CommentsView", u"\u0414\u043d\u0438 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438", None))
        self.commis_Box.setItemText(5, QCoreApplication.translate("CommentsView", u"\u041e\u0445\u0440\u0430\u043d\u0430 \u0442\u0440\u0443\u0434\u0430", None))
        self.commis_Box.setItemText(6, QCoreApplication.translate("CommentsView", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043c\u0435\u0445\u0430\u043d\u0438\u043a", None))

        self.performance_Box.setItemText(0, "")
        self.performance_Box.setItemText(1, QCoreApplication.translate("CommentsView", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.performance_Box.setItemText(2, QCoreApplication.translate("CommentsView", u"\u041d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))

        self.edit_checkBox.setText(QCoreApplication.translate("CommentsView", u"\u0420\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.edit_checkBox_data.setText(QCoreApplication.translate("CommentsView", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440 \u043f\u043e \u0434\u0430\u0442\u0435 \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f", None))
        self.del_Button.setText(QCoreApplication.translate("CommentsView", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0441\u0442\u0440\u043e\u043a\u0438", None))
        self.excel_Button.setText(QCoreApplication.translate("CommentsView", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 Excel", None))
        self.return_pushButton.setText(QCoreApplication.translate("CommentsView", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.menu_Service.setTitle(QCoreApplication.translate("CommentsView", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        self.menu_Editor.setTitle(QCoreApplication.translate("CommentsView", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u044b", None))
        self.menu_Help.setTitle(QCoreApplication.translate("CommentsView", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

