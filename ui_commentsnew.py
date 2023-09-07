# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
##  Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_CommentsNew(object):
    def setupUi(self, CommentsNew):
        if not CommentsNew.objectName():
            CommentsNew.setObjectName(u"CommentsNew")
        CommentsNew.setWindowModality(Qt.ApplicationModal)
        CommentsNew.resize(1114, 706)
        self.action_admin = QAction(CommentsNew)
        self.action_admin.setObjectName(u"action_admin")
        self.action_user = QAction(CommentsNew)
        self.action_user.setObjectName(u"action_user")
        self.action_return = QAction(CommentsNew)
        self.action_return.setObjectName(u"action_return")
        self.action_workers = QAction(CommentsNew)
        self.action_workers.setObjectName(u"action_workers")
        self.action_stations = QAction(CommentsNew)
        self.action_stations.setObjectName(u"action_stations")
        self.action_password = QAction(CommentsNew)
        self.action_password.setObjectName(u"action_password")
        self.action_moduls = QAction(CommentsNew)
        self.action_moduls.setObjectName(u"action_moduls")
        self.action_about = QAction(CommentsNew)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(CommentsNew)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_header = QLabel(self.centralwidget)
        self.label_header.setObjectName(u"label_header")

        self.horizontalLayout.addWidget(self.label_header)

        self.horizontalSpacer_2 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_auditor = QLabel(self.centralwidget)
        self.label_auditor.setObjectName(u"label_auditor")
        self.label_auditor.setMinimumSize(QSize(0, 20))
        self.label_auditor.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_auditor, 0, 7, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.label_date = QLabel(self.centralwidget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMinimumSize(QSize(0, 20))
        self.label_date.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_date, 0, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 9, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.date_dateEdit = QDateEdit(self.centralwidget)
        self.date_dateEdit.setObjectName(u"date_dateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.date_dateEdit.sizePolicy().hasHeightForWidth())
        self.date_dateEdit.setSizePolicy(sizePolicy)
        self.date_dateEdit.setMinimumSize(QSize(100, 30))
        self.date_dateEdit.setMaximumSize(QSize(100, 30))
        self.date_dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_dateEdit, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 4, 1, 1)

        self.Komiss_Box = QComboBox(self.centralwidget)
        self.Komiss_Box.addItem("")
        self.Komiss_Box.addItem("")
        self.Komiss_Box.addItem("")
        self.Komiss_Box.addItem("")
        self.Komiss_Box.addItem("")
        self.Komiss_Box.addItem("")
        self.Komiss_Box.addItem("")
        self.Komiss_Box.addItem("")
        self.Komiss_Box.addItem("")
        self.Komiss_Box.setObjectName(u"Komiss_Box")
        self.Komiss_Box.setMinimumSize(QSize(220, 30))
        self.Komiss_Box.setMaximumSize(QSize(220, 30))

        self.gridLayout.addWidget(self.Komiss_Box, 1, 5, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 6, 1, 1)

        self.auditor_lineedit = QLineEdit(self.centralwidget)
        self.auditor_lineedit.setObjectName(u"auditor_lineedit")
        self.auditor_lineedit.setMinimumSize(QSize(160, 30))
        self.auditor_lineedit.setMaximumSize(QSize(160, 30))

        self.gridLayout.addWidget(self.auditor_lineedit, 1, 7, 1, 1)

        self.label_comission = QLabel(self.centralwidget)
        self.label_comission.setObjectName(u"label_comission")
        self.label_comission.setMinimumSize(QSize(0, 20))
        self.label_comission.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_comission, 0, 5, 1, 1)

        self.label_act = QLabel(self.centralwidget)
        self.label_act.setObjectName(u"label_act")
        self.label_act.setMinimumSize(QSize(0, 20))
        self.label_act.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_act, 0, 1, 1, 1)

        self.act_lineEdit = QLineEdit(self.centralwidget)
        self.act_lineEdit.setObjectName(u"act_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(80)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.act_lineEdit.sizePolicy().hasHeightForWidth())
        self.act_lineEdit.setSizePolicy(sizePolicy1)
        self.act_lineEdit.setMinimumSize(QSize(80, 30))
        self.act_lineEdit.setMaximumSize(QSize(80, 30))

        self.gridLayout.addWidget(self.act_lineEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_stations = QLabel(self.centralwidget)
        self.label_stations.setObjectName(u"label_stations")
        self.label_stations.setMinimumSize(QSize(0, 20))
        self.label_stations.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_stations, 0, 1, 1, 1)

        self.label_executor = QLabel(self.centralwidget)
        self.label_executor.setObjectName(u"label_executor")
        self.label_executor.setMinimumSize(QSize(0, 20))
        self.label_executor.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_executor, 0, 3, 1, 1)

        self.label_term = QLabel(self.centralwidget)
        self.label_term.setObjectName(u"label_term")
        self.label_term.setMinimumSize(QSize(0, 20))
        self.label_term.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_term, 0, 5, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(37, 17, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.Stations_Box = QComboBox(self.centralwidget)
        self.Stations_Box.setObjectName(u"Stations_Box")
        self.Stations_Box.setMinimumSize(QSize(250, 30))
        self.Stations_Box.setMaximumSize(QSize(250, 30))

        self.gridLayout_2.addWidget(self.Stations_Box, 1, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 17, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 1, 2, 1, 1)

        self.Executor_Box = QComboBox(self.centralwidget)
        self.Executor_Box.setObjectName(u"Executor_Box")
        self.Executor_Box.setMinimumSize(QSize(220, 30))

        self.gridLayout_2.addWidget(self.Executor_Box, 1, 3, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(37, 17, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 1, 4, 1, 1)

        self.term_dateEdit = QDateEdit(self.centralwidget)
        self.term_dateEdit.setObjectName(u"term_dateEdit")
        self.term_dateEdit.setMinimumSize(QSize(100, 30))
        self.term_dateEdit.setMaximumSize(QSize(100, 30))
        self.term_dateEdit.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.term_dateEdit, 1, 5, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(108, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 1, 6, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_16 = QSpacerItem(40, 17, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 1, 2, 1, 1)

        self.label_text = QLabel(self.centralwidget)
        self.label_text.setObjectName(u"label_text")

        self.gridLayout_3.addWidget(self.label_text, 0, 1, 1, 1)

        self.text_textEdit = QTextEdit(self.centralwidget)
        self.text_textEdit.setObjectName(u"text_textEdit")
        self.text_textEdit.setMinimumSize(QSize(1000, 0))
        self.text_textEdit.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_3.addWidget(self.text_textEdit, 1, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 17, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.verticalSpacer_4 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.Add_pushButton = QPushButton(self.centralwidget)
        self.Add_pushButton.setObjectName(u"Add_pushButton")
        self.Add_pushButton.setMinimumSize(QSize(140, 40))
        self.Add_pushButton.setMaximumSize(QSize(140, 40))

        self.horizontalLayout_2.addWidget(self.Add_pushButton)

        self.horizontalSpacer_13 = QSpacerItem(388, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.Return_pushButton = QPushButton(self.centralwidget)
        self.Return_pushButton.setObjectName(u"Return_pushButton")
        self.Return_pushButton.setMinimumSize(QSize(140, 40))
        self.Return_pushButton.setMaximumSize(QSize(140, 40))

        self.horizontalLayout_2.addWidget(self.Return_pushButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        CommentsNew.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CommentsNew)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1114, 22))
        self.menu_service = QMenu(self.menubar)
        self.menu_service.setObjectName(u"menu_service")
        self.menu_editors = QMenu(self.menubar)
        self.menu_editors.setObjectName(u"menu_editors")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        CommentsNew.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CommentsNew)
        self.statusbar.setObjectName(u"statusbar")
        CommentsNew.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_service.menuAction())
        self.menubar.addAction(self.menu_editors.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_service.addAction(self.action_admin)
        self.menu_service.addAction(self.action_user)
        self.menu_service.addSeparator()
        self.menu_service.addAction(self.action_return)
        self.menu_editors.addAction(self.action_workers)
        self.menu_editors.addAction(self.action_stations)
        self.menu_editors.addSeparator()
        self.menu_editors.addAction(self.action_password)
        self.menu_help.addAction(self.action_moduls)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(CommentsNew)

        QMetaObject.connectSlotsByName(CommentsNew)
    # setupUi

    def retranslateUi(self, CommentsNew):
        CommentsNew.setWindowTitle(QCoreApplication.translate("CommentsNew", u"CommentsNew", None))
        self.action_admin.setText(QCoreApplication.translate("CommentsNew", u"\u0420\u0435\u0436\u0438\u043c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_user.setText(QCoreApplication.translate("CommentsNew", u"\u0420\u0435\u0436\u0438\u043c &\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.action_return.setText(QCoreApplication.translate("CommentsNew", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.action_workers.setText(QCoreApplication.translate("CommentsNew", u"&\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.action_stations.setText(QCoreApplication.translate("CommentsNew", u"\u0421\u0442\u0430\u043d\u0446\u0438\u0438 \u0438 &\u043f\u0435\u0440\u0435\u0433\u043e\u043d\u044b", None))
        self.action_password.setText(QCoreApplication.translate("CommentsNew", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c &\u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.action_moduls.setText(QCoreApplication.translate("CommentsNew", u"&\u041c\u043e\u0434\u0443\u043b\u0438", None))
        self.action_about.setText(QCoreApplication.translate("CommentsNew", u"&\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_header.setText(QCoreApplication.translate("CommentsNew", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#ff0000;\">\u0424\u043e\u0440\u043c\u0430 \u0432\u0432\u043e\u0434\u0430 \u043d\u043e\u0432\u044b\u0445 \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0439</span></p></body></html>", None))
        self.label_auditor.setText(QCoreApplication.translate("CommentsNew", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u044e\u0449\u0438\u0439:", None))
        self.label_date.setText(QCoreApplication.translate("CommentsNew", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438", None))
        self.Komiss_Box.setItemText(0, "")
        self.Komiss_Box.setItemText(1, QCoreApplication.translate("CommentsNew", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a \u0434\u043e\u0440\u043e\u0433\u0438", None))
        self.Komiss_Box.setItemText(2, QCoreApplication.translate("CommentsNew", u"\u0417\u0430\u043c. \u043f\u043e \u0440\u0435\u0433\u0438\u043e\u043d\u0443", None))
        self.Komiss_Box.setItemText(3, QCoreApplication.translate("CommentsNew", u"\u0420\u0435\u0432\u0438\u0437\u043e\u0440\u0441\u043a\u0438\u0439 \u0430\u043f\u043f\u0430\u0440\u0430\u0442", None))
        self.Komiss_Box.setItemText(4, QCoreApplication.translate("CommentsNew", u"\u0414\u043d\u0438 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438", None))
        self.Komiss_Box.setItemText(5, QCoreApplication.translate("CommentsNew", u"\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0438\u043d\u0441\u043f\u0435\u043a\u0442\u043e\u0440", None))
        self.Komiss_Box.setItemText(6, QCoreApplication.translate("CommentsNew", u"\u041e\u0445\u0440\u0430\u043d\u0430 \u0442\u0440\u0443\u0434\u0430", None))
        self.Komiss_Box.setItemText(7, QCoreApplication.translate("CommentsNew", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0439 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043c\u0435\u0445\u0430\u043d\u0438\u043a", None))
        self.Komiss_Box.setItemText(8, QCoreApplication.translate("CommentsNew", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))

        self.label_comission.setText(QCoreApplication.translate("CommentsNew", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f:", None))
        self.label_act.setText(QCoreApplication.translate("CommentsNew", u"\u2116 \u043f\u043e \u0430\u043a\u0442\u0443", None))
        self.label_stations.setText(QCoreApplication.translate("CommentsNew", u"\u0421\u0442\u0430\u043d\u0446\u0438\u044f, \u043f\u0435\u0440\u0435\u0433\u043e\u043d", None))
        self.label_executor.setText(QCoreApplication.translate("CommentsNew", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c:", None))
        self.label_term.setText(QCoreApplication.translate("CommentsNew", u"\u0421\u0440\u043e\u043a \u0443\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.label_text.setText(QCoreApplication.translate("CommentsNew", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u044f:", None))
        self.Add_pushButton.setText(QCoreApplication.translate("CommentsNew", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \n"
" \u0437\u0430\u043c\u0435\u0447\u0430\u043d\u0438\u0435 \u0432 \u0431\u0430\u0437\u0443", None))
        self.Return_pushButton.setText(QCoreApplication.translate("CommentsNew", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f\n"
" \u043d\u0430\u0437\u0430\u0434", None))
        self.menu_service.setTitle(QCoreApplication.translate("CommentsNew", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        self.menu_editors.setTitle(QCoreApplication.translate("CommentsNew", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u044b", None))
        self.menu_help.setTitle(QCoreApplication.translate("CommentsNew", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

