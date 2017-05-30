# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'librarians.ui'
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
    na = None

    def setupUi(self, Form, Config, Sec):
        self.Form = Form
        self.Config = Config
        self.Sec = Sec
        Form.setObjectName("Form")
        Form.resize(649, 390)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.treeView = QtWidgets.QTreeView(Form)
        self.treeView.setObjectName("treeView")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.treeView)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setContentsMargins(20, -1, 20, -1)
        self.formLayout_2.setSpacing(5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 100))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setMinimumSize(QtCore.QSize(200, 0))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.button(self.buttonBox.Discard).setText("Odrzuć")
        self.buttonBox.button(self.buttonBox.Save).setText("Zapisz")
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.widget)
        self.horizontalLayout.addLayout(self.formLayout)

        self.itemModel = QtGui.QStandardItemModel(0, 5)
        self.treeView.setModel(self.itemModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setColumnWidth(0, 200)
        self.itemModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Imie i nazwisko')
        self.treeView.setColumnWidth(1, 200)
        self.itemModel.setHeaderData(1, QtCore.Qt.Horizontal, 'E-mail')
        self.treeView.setColumnWidth(2, 100)
        self.itemModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Zarządzanie')
        self.treeView.setColumnWidth(3, 60)
        self.itemModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Edytuj')
        self.treeView.setColumnWidth(4, 60)
        self.itemModel.setHeaderData(4, QtCore.Qt.Horizontal, 'Usuń')


        self.buttonBox.button(self.buttonBox.Save).clicked.connect(self.doEdit)
        self.buttonBox.button(self.buttonBox.Discard).clicked.connect(self.delEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_(self):
        self.widget.hide()
        self.get_list()
        return self.Form.show()


    def get_list(self):
        self.clear_row()

        try:
            resp = requests.post(self.Config.get_server()+'/api/getlibrarians',
                                 data={'key': open('.cache', 'r').read()})
            if check_con(resp):
                return False
        except Exception as e:
            return app_error("Wystąpił błąd podczas pobierania informacji.", e)

        if resp.text:
            self.data = self.Sec.encode_data(json.loads(resp.text))
        button = []
        i = 0
        for key, value in self.data.items():
            button.append([])
            button[i].append(QtWidgets.QPushButton("Edytuj"))
            button[i].append(QtWidgets.QPushButton("Usuń"))
            button[i][0].clicked.connect(partial(self.edRead, na=value[0]))
            button[i][1].clicked.connect(partial(self.delLibr, na=value[0]))

            self.itemModel.setItem(i, 0, QtGui.QStandardItem(value[1]+' '+value[2]))
            self.itemModel.setItem(i, 1, QtGui.QStandardItem(value[3]))
            if value[5] == 'True':
                self.itemModel.setItem(i, 2, QtGui.QStandardItem("Tak"))
            else:
                self.itemModel.setItem(i, 2, QtGui.QStandardItem("Nie"))
            self.treeView.setIndexWidget(self.itemModel.index(i, 3), button[i][0])
            self.treeView.setIndexWidget(self.itemModel.index(i, 4), button[i][1])
            i += 1


    def edRead(self, na):
        self.na = na
        index = [y for x, y in self.data.items() if y[0] == na][0]
        if index[5] == 'True':
            self.checkBox.setCheckState(True)
        self.lineEdit.setText(index[1])
        self.lineEdit_2.setText(index[2])
        self.lineEdit_3.setText(index[3])
        return self.widget.show()


    def doEdit(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        master = self.checkBox.isChecked()

        if name is '' or surname is '' or email is '':
            return app_error("Uzupełnij wszystkie dane.")

        try:
            resp = requests.post(self.Config.get_server()+'/api/librariansedit',
                                 data={'key': open('.cache', 'r').read(),
                                       'arg1': self.Sec.encrypt_(name),
                                       'arg2': self.Sec.encrypt_(surname),
                                       'login': self.Sec.encrypt_(email),
                                       'arg3': self.Sec.encrypt_(str(master)),
                                       'name_id': self.Sec.encrypt_(self.na)})
            check_con(resp)
        except Exception as e:
            return app_error("Wystąpił błąd przy edytowaniu.", e)

        if 200 == resp.status_code:
            self.widget.hide()
            self.get_list()
            self.na = None
            return self.editInfo(name, surname, email)
        else:
            return app_error("Wystąpił błąd przy edytowaniu danych.")


    def delEdit(self):
        return self.widget.hide()

    def delLibr(self, na):
        sure = QtWidgets.QMessageBox.question(self.Form, "Usuwanie użytkownika",
                                              "Czy na pewno chcesz usunąć tego użytkownika?",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if sure == QtWidgets.QMessageBox.No:
            return False

        try:
            resp = requests.post(self.Config.get_server()+'/api/dellibrarian',
                                 data={'key': open('.cache', 'r').read(),
                                       'arg1': self.Sec.encrypt_(na)})
            check_con(resp)
        except Exception as e:
            return app_error("Wystąpił błąd przy usuwaniu.", e)

        if resp.status_code == 200:
            self.get_list()
        else:
            return app_error("Wystąpił błąd przy usuwaniu.")


    def editInfo(self, name, surname, emial):
        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setText("Dane zostały pomyslnie zmienione, sprawdź jeszcze raz ich poprawność\n"
                     "Imię i naziwsko: "+name+" "+surname+"\n"
                     "Email: "+emial)
        info.setWindowTitle("Dane biblitekarza!")
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return info.exec_()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sort Books - edycja kont"))
        self.label.setText(_translate("Form", "Zarządzanie kontami"))
        self.label_2.setText(_translate("Form", "Imię: "))
        self.label_3.setText(_translate("Form", "Nazwisko: "))
        self.label_4.setText(_translate("Form", "Emial: "))
        self.label_5.setText(_translate("Form", "Zarządzanie: "))


    def clear_row(self):
        for i in range(self.itemModel.rowCount()):
            self.itemModel.removeRow(i)
