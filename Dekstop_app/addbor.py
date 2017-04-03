# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_borrow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json
from error import app_error, check_con

class Ui_Form(object):

    list_1 = {}
    list_2 = {}

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 298)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(29, 29, 331, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.completer = QtWidgets.QCompleter()
        self.model = QtCore.QStringListModel()
        self.completer.setModel(self.model)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setCompleter(self.completer)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.completer_2 = QtWidgets.QCompleter()
        self.model_2 = QtCore.QStringListModel()
        self.completer_2.setModel(self.model_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setCompleter(self.completer_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.line = QtWidgets.QFrame(self.formLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 90, 331, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.dateEdit_2.setWrapping(False)
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime().addDays(30))
        self.dateEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEdit_2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 231, 31))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(274, 172, 91, 41))
        self.pushButton.setStyleSheet("border: none;\n"
"border-bottom: 3px solid rgb(0, 85, 255);\n"
"background-color: grey;")
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.add_borrow)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Czytelnik: "))
        self.label_2.setText(_translate("Form", "Książka: "))
        self.label_3.setText(_translate("Form", "Wypozyczono: "))
        self.label_4.setText(_translate("Form", "Do zwrotu: "))
        self.pushButton.setText(_translate("Form", "Wypożycz"))

    def get_list_reader(self):
        try:
            resp = requests.post('http://192.168.0.107:5000/api/getreader', data={'key': open('.cache', 'r').read()})
            check_con(resp)
        except:
            return app_error("Wystapił problem przy dodawaniu.")

        data = json.loads(resp.text)
        self.list_1 = {}
        list = []
        for key, value in data.items():
            list.append(value[1]+', '+value[2])
            self.list_1.update({value[1]+', '+value[2]: value[0]})
        self.model.setStringList(list)

    def get_list_book(self):
        try:
            resp = requests.post('http://192.168.0.107:5000/api/getbook', data={'key': open('.cache', 'r').read()})
            check_con(resp)
        except:
            return app_error("Wystąpił błąd przy pobieraniu danych")

        data = json.loads(resp.text)
        self.list_2 = {}
        list = []
        for key, value in data.items():
            list.append(value[1]+', Autora: '+value[2])
            self.list_2.update({value[1]+', Autora: '+value[2]: value[0]})
        self.model_2.setStringList(list)

    def get_list(self):
        self.get_list_book()
        self.get_list_reader()

    def add_borrow(self):
        reader = self.lineEdit.text()
        book = self.lineEdit_2.text()

        if reader is '' or book is '':
            return app_error("Uzupełnij wszystkie dane")

        date_1 = self.dateEdit.date().toPyDate()
        date_2 = self.dateEdit_2.date().toPyDate()
        if date_1 > date_2:
            return app_error("Dats wypożyczenia nie może być większa niż data zwrotu")

        try:
            resp = requests.post('http://192.168.0.107:5000/api/borrow', data={'key': open('.cache', 'r').read(), 'arg1': date_2, 'arg2': date_1, 'name_id': self.list_1[reader], 'book_id': self.list_2[book]})
            check_con(resp)
        except:
            return app_error("Wystąpił błąd przy dodawaniu")

        if 507 == resp.status_code:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label_5.setStyleSheet("color: orange;")
            return self.label_5.setText("Ten czytelnik wypożyczył już tą książkę.")
        elif 201 == resp.status_code:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label_5.setStyleSheet("color: green;")
            return self.label_5.setText("Książka została wypożyczona.")
        else:
            self.label_5.setStyleSheet("color: red;")
            return self.label_5.setText("Nieznany błąd.")