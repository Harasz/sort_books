# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_Lib.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from error import app_error, check_con
import requests
import json
import re


class Ui_Form(object):

    def setupUi(self, Form, Config, Sec):
        self.Form = Form
        self.Config = Config
        self.Sec = Sec
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(343, 281)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 261, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 180, 81, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777212))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 261, 16))
        self.label_5.setObjectName("label_5")

        self.pushButton.clicked.connect(self.addLib)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "Imie: "))
        self.label_2.setText(_translate("Form", "Nazwisko: "))
        self.label_3.setText(_translate("Form", "E-mail: "))
        self.label_4.setText(_translate("Form", "Zarządca"))
        self.pushButton.setText(_translate("Form", "Dodaj"))


    def show_(self):
        self.label_5.setText(" ")
        return self.Form.show()


    def clearLine(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        return self.lineEdit_3.clear()


    def addLib(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        master = self.checkBox.isChecked()

        if name == '' or surname == '' or email == '':
            return app_error("Uzupełnij wszystkie dane")

        if re.match("\w+@\w+(?:\.\w+)", email) == None:
            return app_error("E-mial nie jest poprawny.")

        try:
            resp = requests.post(self.Config.get_server()+'/api/addlibrarian',
                                 data={'key': open('.cache', 'r').read(),
                                       'arg1': self.Sec.encrypt_(name+"/"+surname),
                                       'arg2': self.Sec.encrypt_(email),
                                       'arg3': self.Sec.encrypt_(str(master))})
            check_con(resp)
        except Exception as e:
            return app_error("Wystąpił błąd przy dodawaniu.", e)

        if 507 == resp.status_code:
            self.clearLine()
            self.label_5.setStyleSheet("color: orange;")
            return self.label_5.setText("Bibliotekarz istnieje w bazie.")
        elif 201 == resp.status_code:
            self.clearLine()
            self.label_5.setStyleSheet("color: green;")
            self.userInfo(name, surname, self.Sec.decrypt_(json.loads(resp.text)['data']))
            return self.label_5.setText("Biblitekarz został dodany.")
        else:
            self.label_5.setStyleSheet("color: red;")
            return self.label_5.setText("Nieznany błąd.")


    def userInfo(self, name, surname, password):
        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Warning)
        info.setText(
            "Imie: "+name +
            "\nNazwisko: " + surname +
            "\nHasło: "+password.decode() +
            "\nPamiętaj aby podać hasło bibliotekarzowi.")
        info.setWindowTitle("Dane biblitekarza!")
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return info.exec_()
