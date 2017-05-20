# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readView.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import requests
import json
from error import check_con, app_error


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
        self.treeView.setGeometry(QtCore.QRect(30, 70, 421, 135))
        self.treeView.setObjectName("treeView")
        self.treeView.setSortingEnabled(True)
        self.itemModel = QtGui.QStandardItemModel(0, 4)
        self.treeView.setModel(self.itemModel)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setColumnWidth(0, 150)
        self.itemModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Tytuł')
        self.treeView.setColumnWidth(1, 130)
        self.itemModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Autor')
        self.treeView.setColumnWidth(2, 80)
        self.itemModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Dostępnych')
        self.treeView.setColumnWidth(3, 40)
        self.itemModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Edytuj')

        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 220, 341, 140))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.formLayoutWidget_2.hide()

        self.Config = Config
        self.Sec = Sec

        self.lineEdit.textChanged['QString'].connect(self.search)
        self.pushButton.clicked.connect(self.get_list)
        self.pushButton_2.clicked.connect(self.doEdit)
        self.pushButton_3.clicked.connect(self.get_cover)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("Form", "Szukaj: "))
        self.pushButton.setText(_translate("Form", "Odśwież"))
        self.label_3.setText(_translate("Form", "Tytuł:"))
        self.label_4.setText(_translate("Form", "Autor:"))
        self.label_5.setText(_translate("Form", "Dostępnych: "))
        self.pushButton_2.setText(_translate("Form", "Zmień"))
        self.pushButton_3.setText(_translate("Form", "Zmień okładkę"))


    def show_(self):
        self.get_list()
        self.formLayoutWidget_2.hide()
        self.cover = None
        return self.Form.show()


    def get_list(self):
        self.clear_row()

        try:
            resp = requests.post(self.Config.get_server()+'/api/getbook',
                                 data={'key': open('.cache', 'r').read()})
            if check_con(resp):
                 return False
        except Exception as e:
            return app_error("Wystąpił błąd przy pobieraniu danych.", e)

        self.data = self.Sec.encode_data(json.loads(resp.text))
        self.button = []
        i = 0
        for key, value in self.data.items():
            self.button.append(QtWidgets.QPushButton("Edytuj"))
            self.button[i].clicked.connect(partial(self.edRead, na=value[0]))
            self.itemModel.setItem(int(key)-1, 0, QtGui.QStandardItem(value[1]))
            self.itemModel.setItem(int(key)-1, 1, QtGui.QStandardItem(value[2]))
            self.itemModel.setItem(int(key)-1, 2, QtGui.QStandardItem(str(value[3])))
            self.treeView.setIndexWidget(self.itemModel.index(int(key)-1, 3), self.button[i])
            i += 1


    def edRead(self, na):
        self.na = na

        index = [y for x, y in self.data.items() if y[0] == na][0]
        self.lineEdit_2.setText(index[1])
        self.lineEdit_3.setText(index[2])
        self.lineEdit_4.setText(index[3])
        return self.formLayoutWidget_2.show()


    def doEdit(self):
        title = self.lineEdit_2.text()
        autor = self.lineEdit_3.text()
        count = self.lineEdit_4.text()

        if title is '' or autor is '' or count is '':
            return app_error("Uzupełnij wszystkie dane.")

        try:

            if self.cover is not None:
                files = {'cover': self.cover}
            else:
                files = {}

            resp = requests.post(self.Config.get_server()+'/api/bookedit',
                                 data={'key': open('.cache', 'r').read(),
                                       'arg1': self.Sec.encrypt_(title),
                                       'arg2': self.Sec.encrypt_(autor),
                                       'arg3': self.Sec.encrypt_(count),
                                       'book_id': self.Sec.encrypt_(self.na)},
                                 files=files)
            check_con(resp)
        except Exception as e:
            return app_error("Wystąpił błąd przy edytowaniu.", e)

        self.cover = None

        if 200 == resp.status_code:
            self.formLayoutWidget_2.hide()
            return self.editInfo(title, autor, count)
        else:
            return app_error("Wystąpił błąd przy edytowaniu danych.")


    def editInfo(self, title, autor, count):
        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setText("Dane zostały pomyslnie zmienione, sprawdź jeszcze raz ich poprawność\n"
                     "Tytuł: "+title+"\n"
                     "Autor: "+autor+"\n"
                     "Dostępna ilość w biblitece: "+count)
        info.setWindowTitle("Dane książki!")
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return info.exec_()


    def get_cover(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.Form, "Wybierz okładkę dla ksiązki",
                                                            "",
                                                            "Pliki graficzne (*.png *.jpg *.jpeg *.gif)"
                                                            )
        if fileName:
            self.cover = open(fileName, 'rb')


    def search(self):
        cache = self.lineEdit.text().upper()
        self.clear_row()
        i = 0
        for key, value in self.data.items():
            if not value[1].upper().find(cache) or not value[2].upper().find(cache):
                self.itemModel.setItem(i, 0, QtGui.QStandardItem(value[1]))
                self.itemModel.setItem(i, 1, QtGui.QStandardItem(value[2]))
                self.itemModel.setItem(i, 2, QtGui.QStandardItem(str(value[3])))
                self.treeView.setIndexWidget(self.itemModel.index(int(key) - 1, 3), self.button[i])
                i += 1

    def clear_row(self):
        for i in range(self.itemModel.rowCount()):
            self.itemModel.removeRow(i)
