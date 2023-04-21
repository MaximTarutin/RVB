# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otgulwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_OtgulWindow(object):
    def setupUi(self, OtgulWindow):
        if not OtgulWindow.objectName():
            OtgulWindow.setObjectName(u"OtgulWindow")
        OtgulWindow.setWindowModality(Qt.ApplicationModal)
        OtgulWindow.resize(600, 650)
        OtgulWindow.setMinimumSize(QSize(600, 650))
        OtgulWindow.setMaximumSize(QSize(600, 650))
        OtgulWindow.setStyleSheet(u"background-color: rgb(231, 255, 252);")
        self.gridLayout_2 = QGridLayout(OtgulWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(OtgulWindow)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(450, 40))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tableView = QTableView(OtgulWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(450, 480))
        self.tableView.setMaximumSize(QSize(450, 480))
        self.tableView.setStyleSheet(u"background-color: rgb(234, 234, 234);")

        self.verticalLayout.addWidget(self.tableView)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(458, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(OtgulWindow)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(80, 25))
        self.pushButton.setMaximumSize(QSize(80, 25))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(222, 222, 222);")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(OtgulWindow)

        QMetaObject.connectSlotsByName(OtgulWindow)
    # setupUi

    def retranslateUi(self, OtgulWindow):
        OtgulWindow.setWindowTitle(QCoreApplication.translate("OtgulWindow", u"\u041e\u0442\u0433\u0443\u043b\u044b", None))
        self.label.setText(QCoreApplication.translate("OtgulWindow", u"\u041e \u0422 \u0413 \u0423 \u041b \u042b", None))
        self.pushButton.setText(QCoreApplication.translate("OtgulWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

