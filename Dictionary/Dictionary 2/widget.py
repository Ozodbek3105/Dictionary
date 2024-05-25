# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QListWidget,
                               QPushButton, QTextEdit,
                               QVBoxLayout)

from searchwidget import SearchWidget as QLineEdit


class Ui_Dictionary2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(589, 604)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"pushButton_3")
        self.add_btn.setStyleSheet(u"\n"
                                   "font: 12pt \"MS Shell Dlg 2\";\n"
                                   "padding:8px 50px")

        self.gridLayout.addWidget(self.add_btn, 2, 2, 1, 1)

        self.edit_btn = QPushButton(Form)
        self.edit_btn.setObjectName(u"pushButton_4")
        self.edit_btn.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
                                    "padding:8px 50px\n"
                                    "")

        self.gridLayout.addWidget(self.edit_btn, 2, 1, 1, 1)

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 5)

        self.kalonka_btn = QPushButton("audio")
        self.kalonka_btn.setObjectName(u"pushButton_2")
        self.kalonka_btn.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
                                      "padding:8px 50px")

        self.gridLayout.addWidget(self.kalonka_btn, 2, 3, 1, 1)
        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"pushButton_2")
        self.delete_btn.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
                                      "padding:8px 50px")

        self.gridLayout.addWidget(self.delete_btn, 2, 0, 1, 1)

        self.search_btn = QPushButton(Form)
        self.search_btn.setObjectName(u"pushButton")
        self.search_btn.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";"
                                      u"padding:8px 50px")

        self.gridLayout.addWidget(self.search_btn, 0, 3, 1, 2)

        self.mikrafon_btn = QPushButton("gapiring")
        self.mikrafon_btn.setObjectName(u"pushButton_2")
        self.mikrafon_btn.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
                                      "padding:8px 50px")
        self.gridLayout.addWidget(self.mikrafon_btn, 0, 2, 1, 1)
        self.search_lineEdit = QLineEdit(Form)
        self.search_lineEdit.setObjectName(u"lineEdit")
        self.search_lineEdit.setStyleSheet(u"padding:8px ")

        self.gridLayout.addWidget(self.search_lineEdit, 0, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"padding:10px")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")


        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"add", None))
        self.edit_btn.setText(QCoreApplication.translate("Form", u"edit", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"delete", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"search", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"add item", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"add value", None))
    # retranslateUi
