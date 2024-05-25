# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dictionary.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget, QTextEdit)


class Ui_Dictionary(object):
    def setupUi(self, Dictionary):
        if not Dictionary.objectName():
            Dictionary.setObjectName(u"Dictionary")
        Dictionary.resize(720, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dictionary.sizePolicy().hasHeightForWidth())
        Dictionary.setSizePolicy(sizePolicy)
        Dictionary.setMinimumSize(QSize(720, 500))
        Dictionary.setStyleSheet(u"background-color: rgb(199, 199, 199);")
        self.centralwidget = QWidget(Dictionary)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
                                   "padding: 0px 0px  opx 80 px")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setUnderline(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                    "border: 2px solid black;\n"
                                    "")
        self.lineEdit.setLocale(QLocale(QLocale.Uzbek, QLocale.Uzbekistan))
        self.lineEdit.setPlaceholderText(u"search")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);border-radius:10px;\n"
                                      "background-color: rgb(89, 89, 89);\n"
                                      "margin:0px 40px 0px 40px;\n"
                                      "padding:10px\n"
                                      
                                      "")

        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.label = QTextEdit(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
                                 "margin: 30px 30px")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 3)

        self.verticalLayout.addLayout(self.gridLayout)

        Dictionary.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dictionary)

        QMetaObject.connectSlotsByName(Dictionary)

    # setupUi

    def retranslateUi(self, Dictionary):
        Dictionary.setWindowTitle(QCoreApplication.translate("Dictionary", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("Dictionary", u"Enter a word:", None))
        # if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Dictionary",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'Arial Black'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
                                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                              None))
        # endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Dictionary", u"Search", None))
        self.label.setText("")
    # retranslateUi
