# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readView.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from error import check_con, app_error
import requests
import json


class Ui_Form(object):

    data = None
    resp = None
    resp_2 = None

    def setupUi(self, Form, Config, Sec):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 260, 141, 31))
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
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.treeView = QtWidgets.QTreeView(Form)
        self.treeView.setGeometry(QtCore.QRect(30, 60, 415, 192))
        self.treeView.setObjectName("treeView")
        self.treeView.setSortingEnabled(True)
        self.itemModel = QtGui.QStandardItemModel(0, 4)
        self.treeView.setModel(self.itemModel)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setColumnWidth(0, 150)
        self.itemModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Czytelnik')
        self.treeView.setColumnWidth(1, 100)
        self.itemModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Książka')
        self.treeView.setColumnWidth(2, 100)
        self.itemModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Data wypożyczenia')
        self.treeView.setColumnWidth(3, 25)
        self.itemModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Zwrócono')

        self.Config = Config
        self.Sec = Sec

        self.lineEdit.textChanged['QString'].connect(self.search)
        self.pushButton.clicked.connect(self.get_list)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Szukaj: "))
        self.pushButton.setText(_translate("Form", "Odśwież"))

    def show_(self):
        self.get_list()
        return self.Form.show()

    def get_list(self):
        self.clear_row()

        try:
            resp = requests.post(self.Config.get_server()+'/api/getborrow',
                                 data={'key': open('.cache', 'r').read()})
            if check_con(resp):
                 return False
        except Exception as e:
            return app_error("Wystąpił błąd przy pobieraniu danych.", e)

        if resp.text:
            self.data = self.Sec.encode_data(json.loads(resp.text))

        for key, value in self.data.items():
            self.itemModel.setItem(int(key), 0, QtGui.QStandardItem(value[1]))
            self.itemModel.setItem(int(key), 1, QtGui.QStandardItem(value[2]))
            self.itemModel.setItem(int(key), 2, QtGui.QStandardItem(value[0]))
            if value[3] == 'True':
                self.itemModel.setItem(int(key), 3, QtGui.QStandardItem("Tak"))
            else:
                self.itemModel.setItem(int(key), 3, QtGui.QStandardItem("Nie"))

    def search(self):
        cache = self.lineEdit.text().upper()
        self.clear_row()
        i = 0
        for key, value in self.data.items():
            if not value[1].upper().find(cache) == -1 \
               or not value[2].upper().find(cache) == -1 \
               or not value[0].upper().find(cache) == -1:
                self.itemModel.setItem(i, 0, QtGui.QStandardItem(value[1]))
                self.itemModel.setItem(i, 1, QtGui.QStandardItem(value[2]))
                self.itemModel.setItem(i, 2, QtGui.QStandardItem(value[0]))
                if value[3] == 'True':
                    self.itemModel.setItem(i, 3, QtGui.QStandardItem("Tak"))
                else:
                    self.itemModel.setItem(i, 3, QtGui.QStandardItem("Nie"))
                i += 1

    def clear_row(self):
        for i in range(self.itemModel.rowCount()):
            self.itemModel.removeRow(i)
