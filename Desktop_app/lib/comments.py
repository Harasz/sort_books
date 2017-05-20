# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comments.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from error import check_con, app_error
from functools import partial
import requests
import json


class Ui_Form(object):

    def setupUi(self, Form, Config, Sec):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(444, 373)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 600, 380))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.treeView = QtWidgets.QTreeView(self.formLayoutWidget)
        self.treeView.setMinimumSize(QtCore.QSize(435, 275))
        self.treeView.setObjectName("treeView")
        self.itemModel = QtGui.QStandardItemModel(0, 4)
        self.treeView.setModel(self.itemModel)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setColumnWidth(0, 150)
        self.itemModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Czytelnik')
        self.treeView.setColumnWidth(1, 160)
        self.itemModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Komentarz')
        self.treeView.setColumnWidth(2, 60)
        self.itemModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Akceptuj')
        self.treeView.setColumnWidth(3, 60)
        self.itemModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Odrzuć')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.treeView)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)

        self.Config = Config
        self.Sec = Sec

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Komentarze do zaakceptowania"))


    def show_(self):
        self.get_list()
        return self.Form.show()


    def get_list(self):
        self.clear_row()

        try:
            resp = requests.post(self.Config.get_server()+'/api/getcomm', data={'key': open('.cache', 'r').read()})
            if check_con(resp):
                 return False
        except Exception as e:
            return app_error("Wystąpił błąd przy pobieraniu danych.", e)

        if resp.status_code == 204:
            self.label_2.setStyleSheet("color: green;")
            self.label_2.setText("Brak komentarzy.")
            return False


        data = self.Sec.encode_data(json.loads(resp.text))
        button = []
        for key, value in data.items():
            button.append([])
            button[int(key)].append(QtWidgets.QPushButton("Akceptuj"))
            button[int(key)].append(QtWidgets.QPushButton("Odrzuć"))
            button[int(key)][0].clicked.connect(partial(self.acceptCom, na=value[0], ac="True"))
            button[int(key)][1].clicked.connect(partial(self.acceptCom, na=value[0], ac="False"))

            self.itemModel.setItem(int(key), 0, QtGui.QStandardItem(value[2]))
            self.itemModel.setItem(int(key), 1, QtGui.QStandardItem(value[1]))
            self.treeView.setIndexWidget(self.itemModel.index(int(key), 2), button[int(key)][0])
            self.treeView.setIndexWidget(self.itemModel.index(int(key), 3), button[int(key)][1])


    def acceptCom(self, na, ac):
        if ac == "False":
            sure = QtWidgets.QMessageBox.question(self.Form, "Usuwanie komentarza",
                                                  "Czy na pewno chcesz usunąć ten komentarz?",
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if sure == QtWidgets.QMessageBox.No:
                return False

        try:
            resp = requests.post(self.Config.get_server()+'/api/acceptcom',
                                 data={'arg1': self.Sec.encrypt_(na),
                                       'arg2': self.Sec.encrypt_(ac),
                                       'key': open('.cache', 'r').read()})
            check_con(resp)
        except Exception as e:
            self.label_2.setStyleSheet("color: red;")
            self.label_2.setText("Wystąpił błąd.")
            return self.get_list()

        if resp.status_code == 201:
            self.label_2.setStyleSheet("color: green;")
            self.label_2.setText("Zaakceptowano.")
        else:
            self.label_2.setStyleSheet("color: red;")
            self.label_2.setText("Wystąpił błąd.")

        return self.get_list()


    def clear_row(self):
        for i in range(self.itemModel.rowCount()):
            self.itemModel.removeRow(i)
