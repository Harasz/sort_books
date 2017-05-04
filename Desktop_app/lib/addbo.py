# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_bo.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from error import app_error, check_con


class Ui_Form(object):

    def setupUi(self, Form, Config, Sec):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 331, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(26, 162, 221, 61))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(264, 162, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.Config = Config
        self.Sec = Sec

        self.pushButton.clicked.connect(self.add_book)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Autor: "))
        self.label_2.setText(_translate("Form", "Tytuł: "))
        self.label_4.setText(_translate("Form", "Ilość: "))
        self.pushButton.setText(_translate("Form", "Dodaj"))

    def show_(self):
        return self.Form.show()

    def add_book(self):
        author = self.lineEdit.text()
        title = self.lineEdit_2.text()
        count = self.lineEdit_3.text()

        if author is '' or title is '' or count is '':
            return app_error("Uzupełnij wszystkie dane.")

        try:
            resp = requests.post(self.Config.get_server()+'/api/addbook',
                                 data={'arg1': self.Sec.encrypt_(title),
                                       'arg2': self.Sec.encrypt_(author),
                                       'book_id': self.Sec.encrypt_(count),
                                       'key': open('.cache', 'r').read()})
            check_con(resp)
        except:
            return app_error("Wystąpił błąd przy dodawaniu.")

        if 507 == resp.status_code:
            self.clear_line()
            self.label_3.setStyleSheet("color: green;")
            return self.label_3.setText("Dodano "+str(count)+" książek.")
        elif 201 == resp.status_code:
            self.clear_line()
            self.label_3.setStyleSheet("color: green;")
            return self.label_3.setText("Książka dodana do bazy.")
        else:
            self.label_3.setStyleSheet("color: red;")
            return self.label_3.setText("Nieznany błąd.")

    def clear_line(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
