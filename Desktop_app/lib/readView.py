# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readView.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from error import check_con, app_error
import requests
import json



class Ui_Form(object):

    data = None
    button = []

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
        self.treeView.setGeometry(QtCore.QRect(30, 50, 400, 170))
        self.treeView.setObjectName("treeView")
        self.treeView.setSortingEnabled(True)
        self.itemModel = QtGui.QStandardItemModel(0, 3)
        self.treeView.setModel(self.itemModel)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setColumnWidth(0, 160)
        self.itemModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Imie i nazwisko')
        self.treeView.setColumnWidth(1, 175)
        self.itemModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Adres')
        self.treeView.setColumnWidth(2, 40)
        self.itemModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Edytuj')

        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 230, 341, 140))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.formLayoutWidget_2.hide()

        self.Config = Config
        self.Sec = Sec

        self.lineEdit.textChanged['QString'].connect(self.search)
        self.pushButton.clicked.connect(self.get_list)
        self.pushButton_2.clicked.connect(self.doEdit)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("Form", "Szukaj: "))
        self.pushButton.setText(_translate("Form", "Odśwież"))
        self.label_3.setText(_translate("Form", "Imię:"))
        self.label_4.setText(_translate("Form", "Nazwisko:"))
        self.label_5.setText(_translate("Form", "Miasto"))
        self.label_6.setText(_translate("Form", "Ulica:"))
        self.pushButton_2.setText(_translate("Form", "Zmień"))

    def show_(self):
        self.get_list()
        self.formLayoutWidget_2.hide()
        return self.Form.show()

    def get_list(self):
        self.clear_row()

        try:
            resp = requests.post(self.Config.get_server()+'/api/getreader',
                                 data={'key': open('.cache', 'r').read()})
            if check_con(resp):
                return False
        except Exception as e:
            return app_error("Wystąpił błąd podczas pobierania informacji.", e)

        if resp.text:
            self.data = self.Sec.encode_data(json.loads(resp.text))
        i = 0
        self.button = []
        for key, value in self.data.items():
            self.button.append(QtWidgets.QPushButton("Edytuj"))
            self.button[i].clicked.connect(partial(self.edRead, na=value[0]))
            self.itemModel.setItem(int(key)-1, 0, QtGui.QStandardItem(value[1]))
            self.itemModel.setItem(int(key)-1, 1, QtGui.QStandardItem(value[2]))
            self.treeView.setIndexWidget(self.itemModel.index(int(key)-1, 2), self.button[i])
            i += 1

    def edRead(self, na):
        self.na = na

        index = [y for x, y in self.data.items() if y[0] == na][0]

        name = index[1].split(' ')
        address = index[2].split(', ')

        self.lineEdit_2.setText(name[0])
        self.lineEdit_3.setText(name[1])
        self.lineEdit_4.setText(address[0])
        self.lineEdit_5.setText(address[1])
        return self.formLayoutWidget_2.show()

    def doEdit(self):
        name = self.lineEdit_2.text()
        surname = self.lineEdit_3.text()
        address = self.lineEdit_4.text()
        address_2 = self.lineEdit_5.text()

        if name is '' or surname is '' or address is '' or address_2 is '':
            return app_error("Uzupełnij wszystkie dane.")

        name = name+' '+surname
        address = address+', '+address_2

        try:
            resp = requests.post(self.Config.get_server()+'/api/useredit',
                                 data={'key': open('.cache', 'r').read(),
                                       'arg1': self.Sec.encrypt_(name),
                                       'arg2': self.Sec.encrypt_(address),
                                       'name_id': self.Sec.encrypt_(self.na)})
            check_con(resp)
        except Exception as e:
            return app_error("Wystąpił błąd przy edytowaniu.", e)

        if 200 == resp.status_code:
            self.formLayoutWidget_2.hide()
            return self.editInfo(name, address)
        else:
            return app_error("Wystąpił błąd przy edytowaniu danych.")

    def editInfo(self, name, address):
        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setText("Dane zostały pomyslnie zmienione, sprawdź jeszcze raz ich poprawność\n"
                     "Imię i naziwsko: "+name+"\n"
                     "Adres: "+address)
        info.setWindowTitle("Dane czytelnika!")
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return info.exec_()

    def search(self):
        cache = self.lineEdit.text().upper()
        self.clear_row()
        i = 0
        for key, value in self.data.items():
            if not value[2].upper().find(cache) or not value[1].upper().find(cache):
                self.itemModel.setItem(int(key) - 1, 0, QtGui.QStandardItem(value[1]))
                self.itemModel.setItem(int(key) - 1, 1, QtGui.QStandardItem(value[2]))
                self.treeView.setIndexWidget(self.itemModel.index(int(key) - 1, 2), self.button[i])
                i += 1

    def clear_row(self):
        for i in range(self.itemModel.rowCount()):
            self.itemModel.removeRow(i)
