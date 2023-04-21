# -*- coding: utf-8 -*-
"""
################################################################################
## Form generated from reading UI file 'passwordform.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
"""

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(644, 271)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(644, 271))
        Form.setMaximumSize(QSize(644, 271))
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 255, 255, 160), stop:1 rgba(255, 255, 255, 255));")
        self.passw_label = QLabel(Form)
        self.passw_label.setObjectName(u"passw_label")
        self.passw_label.setGeometry(QRect(20, 80, 261, 21))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.passw_label.setFont(font)
        self.passw_label_2 = QLabel(Form)
        self.passw_label_2.setObjectName(u"passw_label_2")
        self.passw_label_2.setGeometry(QRect(20, 140, 211, 21))
        self.passw_label_2.setFont(font)
        self.passw_label_3 = QLabel(Form)
        self.passw_label_3.setObjectName(u"passw_label_3")
        self.passw_label_3.setGeometry(QRect(20, 190, 231, 21))
        self.passw_label_3.setFont(font)
        self.button_Ok = QPushButton(Form)
        self.button_Ok.setObjectName(u"button_Ok")
        self.button_Ok.setGeometry(QRect(540, 230, 80, 25))
        self.button_Cancel = QPushButton(Form)
        self.button_Cancel.setObjectName(u"button_Cancel")
        self.button_Cancel.setGeometry(QRect(420, 230, 80, 25))
        self.passw_lineEdit = QLineEdit(Form)
        self.passw_lineEdit.setObjectName(u"passw_lineEdit")
        self.passw_lineEdit.setGeometry(QRect(290, 80, 331, 25))
        self.passw_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.new_passw_lineEdit = QLineEdit(Form)
        self.new_passw_lineEdit.setObjectName(u"new_passw_lineEdit")
        self.new_passw_lineEdit.setGeometry(QRect(290, 140, 331, 25))
        self.new_passw_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.new_passw_lineEdit_1 = QLineEdit(Form)
        self.new_passw_lineEdit_1.setObjectName(u"new_passw_lineEdit_1")
        self.new_passw_lineEdit_1.setGeometry(QRect(290, 190, 331, 25))
        self.new_passw_lineEdit_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 481, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 0, 127);")
        self.label.setFrameShape(QFrame.Box)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.passw_label.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430:", None))
        self.passw_label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.passw_label_3.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c \u0435\u0449\u0435 \u0440\u0430\u0437:", None))
        self.button_Ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.button_Cancel.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
    # retranslateUi

