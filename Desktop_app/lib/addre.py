# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_re.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from error import app_error, check_con
import requests
import json
import random


class Ui_Form(object):


    def setupUi(self, Form, Config, Sec):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(406, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 117, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 20, 271, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)

        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)

        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(264, 160, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(16, 162, 151, 31))
        self.label_4.setStyleSheet("color: green;")
        self.label_4.setObjectName("label_4")

        self.Config = Config
        self.Sec = Sec

        self.pushButton.clicked.connect(self.add_re)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Imię:"))
        self.label_2.setText(_translate("Form", "Nazwisko:"))
        self.label_3.setText(_translate("Form", "Miasto:"))
        self.label_5.setText(_translate("Form", "Ulica i nr domu:"))
        self.pushButton.setText(_translate("Form", "Dodaj czytelnika"))
        self.label_4.setText(_translate("Form", ""))

    def show_(self):
        return self.Form.show()

    def add_re(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        address = self.lineEdit_3.text()
        address_2 = self.lineEdit_4.text()

        if name is '' or surname is '' or address is '' or address_2 is '':
            return app_error("Uzupełnij wszystkie dane.")

        name = name+' '+surname
        address = address+', '+address_2
        login = name[0:2]+surname[0:3]+''.join(random.sample('1234567890', 2))+address_2[-1]

        try:
            resp = requests.post(self.Config.get_server()+'/api/addre',
                                 data={'key': open('.cache', 'r').read(),
                                       'arg1': self.Sec.encrypt_(name),
                                       'arg2': self.Sec.encrypt_(address),
                                       'login': self.Sec.encrypt_(login)})
            check_con(resp)
        except:
            return app_error("Wystąpił błąd przy dodawaniu.")

        if 507 == resp.status_code:
            self.clear_all()
            self.label_4.setStyleSheet("color: orange;")
            return self.label_4.setText("Czytelnik istnieje w bazie.")
        elif 201 == resp.status_code:
            self.clear_all()
            self.label_4.setStyleSheet("color: green;")
            self.show_userInfo(login, self.Sec.decrypt_(json.loads(resp.text)['haslo']))
            return self.label_4.setText("Czytelnik dodany do bazy.")
        else:
            self.label_4.setStyleSheet("color: red;")
            return self.label_4.setText("Nieznany błąd.")

    def show_userInfo(self, login, pas):
        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Warning)
        info.setText("Login użytkownika: "+login+"\nHasło: "+pas.decode()+"\nMasz obowiązek podać je czytelnikowi!")
        info.setWindowTitle("Dane czytelnika!")
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return info.exec_()

    def clear_all(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()