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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QTextEdit,
    QWidget)

class Ui_planEditor(object):
    def setupUi(self, planEditor):
        if not planEditor.objectName():
            planEditor.setObjectName(u"planEditor")
        planEditor.setWindowModality(Qt.ApplicationModal)
        planEditor.resize(1200, 700)
        planEditor.setMinimumSize(QSize(1200, 700))
        planEditor.setStyleSheet(u"background-color: rgb(135, 161, 255);")
        self.action_workers = QAction(planEditor)
        self.action_workers.setObjectName(u"action_workers")
        self.action_stations = QAction(planEditor)
        self.action_stations.setObjectName(u"action_stations")
        self.action_return = QAction(planEditor)
        self.action_return.setObjectName(u"action_return")
        self.action_moduls = QAction(planEditor)
        self.action_moduls.setObjectName(u"action_moduls")
        self.action_about = QAction(planEditor)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(planEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_about = QLabel(self.centralwidget)
        self.label_about.setObjectName(u"label_about")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(36)
        font.setBold(True)
        self.label_about.setFont(font)
        self.label_about.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.label_about.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_about, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 7, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_6 = QSpacerItem(17, 17, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.textEdit_plan = QTextEdit(self.centralwidget)
        self.textEdit_plan.setObjectName(u"textEdit_plan")
        self.textEdit_plan.setMinimumSize(QSize(850, 125))
        self.textEdit_plan.setMaximumSize(QSize(850, 125))
        self.textEdit_plan.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.textEdit_plan)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMinimumSize(QSize(100, 25))
        self.pushButton_add.setMaximumSize(QSize(100, 25))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_add.setFont(font2)
        self.pushButton_add.setStyleSheet(u"background-color: rgb(85, 255, 127);")

        self.horizontalLayout_3.addWidget(self.pushButton_add)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(140, 25))
        self.dateEdit.setMaximumSize(QSize(140, 25))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.dateEdit.setFont(font3)
        self.dateEdit.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit)

        self.horizontalSpacer_4 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 25))
        self.comboBox.setMaximumSize(QSize(300, 25))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(14)
        self.comboBox.setFont(font4)
        self.comboBox.setStyleSheet(u"background-color: rgb(238, 238, 238);")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer_5 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(340, 25))
        self.comboBox_2.setMaximumSize(QSize(340, 25))
        self.comboBox_2.setFont(font4)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(238, 238, 238);")

        self.horizontalLayout.addWidget(self.comboBox_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_9 = QSpacerItem(17, 28, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 6, 2, 1)

        self.horizontalSpacer_10 = QSpacerItem(17, 28, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 3, 7, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.pushButton_del = QPushButton(self.centralwidget)
        self.pushButton_del.setObjectName(u"pushButton_del")
        self.pushButton_del.setMinimumSize(QSize(100, 25))
        self.pushButton_del.setMaximumSize(QSize(100, 25))
        self.pushButton_del.setFont(font2)
        self.pushButton_del.setStyleSheet(u"background-color: rgb(255, 170, 255);")

        self.gridLayout.addWidget(self.pushButton_del, 1, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 4, 4, 1, 2)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(870, 250))
        self.tableView.setStyleSheet(u"background-color: rgb(249, 249, 249);")

        self.gridLayout.addWidget(self.tableView, 0, 4, 4, 1)

        self.pushButton_return = QPushButton(self.centralwidget)
        self.pushButton_return.setObjectName(u"pushButton_return")
        self.pushButton_return.setMinimumSize(QSize(100, 25))
        self.pushButton_return.setMaximumSize(QSize(100, 25))
        self.pushButton_return.setFont(font2)
        self.pushButton_return.setStyleSheet(u"background-color: rgb(238, 238, 238);")

        self.gridLayout.addWidget(self.pushButton_return, 3, 6, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_15, 0, 1, 4, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 108, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 3, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 8, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        planEditor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(planEditor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menu_editor = QMenu(self.menubar)
        self.menu_editor.setObjectName(u"menu_editor")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        planEditor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(planEditor)
        self.statusbar.setObjectName(u"statusbar")
        planEditor.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_editor.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_editor.addAction(self.action_workers)
        self.menu_editor.addAction(self.action_stations)
        self.menu_editor.addSeparator()
        self.menu_editor.addAction(self.action_return)
        self.menu_help.addAction(self.action_moduls)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(planEditor)

        QMetaObject.connectSlotsByName(planEditor)
    # setupUi

    def retranslateUi(self, planEditor):
        planEditor.setWindowTitle(QCoreApplication.translate("planEditor", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a\u0430", None))
        self.action_workers.setText(QCoreApplication.translate("planEditor", u"&\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.action_stations.setText(QCoreApplication.translate("planEditor", u"\u0421\u0442\u0430\u043d\u0446\u0438\u0438 \u0438 &\u043f\u0435\u0440\u0435\u0433\u043e\u043d\u044b", None))
        self.action_return.setText(QCoreApplication.translate("planEditor", u"&\u041d\u0430\u0437\u0430\u0434", None))
        self.action_moduls.setText(QCoreApplication.translate("planEditor", u"&\u041c\u043e\u0434\u0443\u043b\u0438", None))
        self.action_about.setText(QCoreApplication.translate("planEditor", u"&\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_about.setText(QCoreApplication.translate("planEditor", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0441\u0443\u0442\u043e\u0447\u043d\u043e\u0433\u043e \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("planEditor", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))
        self.pushButton_add.setText(QCoreApplication.translate("planEditor", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("planEditor", u"\u0414\u0430\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("planEditor", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None))
        self.label_3.setText(QCoreApplication.translate("planEditor", u"\u0421\u0442\u0430\u043d\u0446\u0438\u044f", None))
        self.pushButton_del.setText(QCoreApplication.translate("planEditor", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_return.setText(QCoreApplication.translate("planEditor", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.menu_editor.setTitle(QCoreApplication.translate("planEditor", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u044b", None))
        self.menu_help.setTitle(QCoreApplication.translate("planEditor", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

