# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readView.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json
from functools import partial
from error import check_con, app_error

class Ui_Form(object):

    data = None
    resp = None
    resp_2 = None
    button = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 260, 150, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 271, 22))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: nonel;\n"
"border-left: 1px solid grey;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.treeView = QtWidgets.QTreeView(Form)
        self.treeView.setGeometry(QtCore.QRect(30, 60, 400, 192))
        self.treeView.setObjectName("treeView")
        self.itemModel = QtGui.QStandardItemModel(0, 4)
        self.treeView.setModel(self.itemModel)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setColumnWidth(0, 150)
        self.itemModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Czytelnik')
        self.treeView.setColumnWidth(1, 100)
        self.itemModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Książka')
        self.treeView.setColumnWidth(2, 100)
        self.itemModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Data zwrotu')
        self.treeView.setColumnWidth(3, 10)
        self.itemModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Akcja')

        self.lineEdit.textChanged['QString'].connect(self.search)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Szukaj: "))
        self.pushButton.setText(_translate("Form", "Szukaj"))

    def get_list(self):
        self.clear_row()

        try:
            file = open('.cache', 'r').read()
            resp = requests.post('http://192.168.0.107:5000/api/getborrow', data={'key': file})
            resp_2 = requests.post('http://192.168.0.107:5000/api/getreader', data={'key': file})
            resp_3 = requests.post('http://192.168.0.107:5000/api/getbook', data={'key': file})
            if check_con(resp):
                 return False
        except:
            return app_error("Wystąpił błąd podczas pobierania informacji")

        self.data = json.loads(resp.text)
        self.resp = json.loads(resp_2.text)
        self.resp_2 = json.loads(resp_3.text)
        i = 0
        self.button = []
        for key, value in self.data.items():
            if not value[3]:
                self.button.append(QtWidgets.QPushButton("Zwróć"))
                self.button[i].clicked.connect(partial(self.retBook, na=value[4]))
                self.itemModel.setItem(i, 0, QtGui.QStandardItem(self.resp[str(value[1])][1]))
                self.itemModel.setItem(i, 1, QtGui.QStandardItem(self.resp_2[str(value[2])][1]))
                self.itemModel.setItem(i, 2, QtGui.QStandardItem(value[0]))
                self.treeView.setIndexWidget(self.itemModel.index(i, 3), self.button[i])
                i += 1

    def retBook(self, na):
        try:
            resp = requests.post('http://192.168.0.107:5000/api/retbook', data={'arg1': na, 'key': open('.cache', 'r').read()})
            check_con(resp)
        except:
            self.label.setStyleSheet("color: red;")
            self.label.setText("Wystąpił błąd.")
            return self.get_list()

        if resp.status_code == 201:
            self.label.setStyleSheet("color: green;")
            self.label.setText("Książką została pomyślnie oddana")
        else:
            self.label.setStyleSheet("color: red;")
            self.label.setText("Wystąpił błąd.")

        return self.get_list()




    def search(self):
        cache = self.lineEdit.text()
        self.clear_row()
        i = 0
        for key, value in self.data.items():
            if not value[3] and (cache.upper() in self.resp[str(value[1])][1].upper() or cache.upper() in self.resp_2[str(value[2])][1].upper() or cache.upper() in value[0].upper() or cache.upper() in ''):
                self.itemModel.setItem(i, 0, QtGui.QStandardItem(self.resp[str(value[1])][1]))
                self.itemModel.setItem(i, 1, QtGui.QStandardItem(self.resp_2[str(value[2])][1]))
                self.itemModel.setItem(i, 2, QtGui.QStandardItem(value[0]))
                i += 1

    def clear_row(self):
        for i in range(self.itemModel.rowCount()):
            self.itemModel.removeRow(i)