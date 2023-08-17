# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_File_View(object):
    def setupUi(self, File_View):
        if not File_View.objectName():
            File_View.setObjectName(u"File_View")
        File_View.setWindowModality(Qt.ApplicationModal)
        File_View.resize(1276, 681)
        self.gridLayout = QGridLayout(File_View)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_7 = QSpacerItem(20, 569, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 2, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 3, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 3, 1, 1)

        self.label_foto = QLabel(File_View)
        self.label_foto.setObjectName(u"label_foto")

        self.gridLayout.addWidget(self.label_foto, 1, 1, 3, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_save = QPushButton(File_View)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.horizontalSpacer_2 = QSpacerItem(458, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_del = QPushButton(File_View)
        self.pushButton_del.setObjectName(u"pushButton_del")

        self.horizontalLayout.addWidget(self.pushButton_del)

        self.horizontalSpacer_3 = QSpacerItem(458, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_close = QPushButton(File_View)
        self.pushButton_close.setObjectName(u"pushButton_close")

        self.horizontalLayout.addWidget(self.pushButton_close)

        self.horizontalSpacer_4 = QSpacerItem(28, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 5)


        self.retranslateUi(File_View)

        QMetaObject.connectSlotsByName(File_View)
    # setupUi

    def retranslateUi(self, File_View):
        File_View.setWindowTitle(QCoreApplication.translate("File_View", u"File_View", None))
        self.label_foto.setText("")
        self.pushButton_save.setText(QCoreApplication.translate("File_View", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_del.setText(QCoreApplication.translate("File_View", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_close.setText(QCoreApplication.translate("File_View", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

