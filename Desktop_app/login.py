# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Login_form(object):


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 306)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #EEEEEE;\n"
"    border: 1px solid #515151;\n"
"    color: #515151;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background-color: #00B4FF;\n"
"    color: #FFF;\n"
"}\n"
"QLineEdit\n"
"{\n"
"    background-color: #EEEEEE;\n"
"    border: 1px solid #515151;\n"
"    color: #515151;\n"
"}")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.welcomeLabel = QtWidgets.QLabel(Form)
        self.welcomeLabel.setGeometry(QtCore.QRect(0, 0, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.welcomeLabel.setAutoFillBackground(True)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setWordWrap(True)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 120, 201, 31))
        self.lineEdit.setObjectName("loginInput")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 170, 201, 31))
        self.lineEdit_2.setObjectName("passInput")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.closeBtn = QtWidgets.QPushButton(Form)
        self.closeBtn.setGeometry(QtCore.QRect(360, 0, 40, 40))
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.setText("X")
        self.closeBtn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: red;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    color: #FFF;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background-color: black;\n"
"    color: #FFF;\n"
"}\n")
        self.loginBtn = QtWidgets.QPushButton(Form)
        self.loginBtn.setGeometry(QtCore.QRect(140, 230, 101, 41))
        self.loginBtn.setObjectName("loginBtn")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.loginBtn.pressed.connect(lambda: self.loginAction())
        self.closeBtn.pressed.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sort Books - logowanie"))
        self.welcomeLabel.setText(_translate("Form", "Sort_Books;"))
        self.label.setText(_translate("Form", "Email: "))
        self.label_2.setText(_translate("Form", "Hasło:"))
        self.loginBtn.setText(_translate("Form", "Zaloguj"))
        self.loginBtn.clicked.connect(self.loginAction)