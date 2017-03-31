# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readView.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json

class Ui_Form(object):

    data = None

    def setupUi(self, Form):
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
        self.itemModel = QtGui.QStandardItemModel(0, 2)
        self.treeView.setModel(self.itemModel)
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeView.setColumnWidth(0, 200)
        self.itemModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Tytuł')
        self.treeView.setColumnWidth(2, 200)
        self.itemModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Autor')

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
            resp = requests.post('http://192.168.0.107:5000/api/getbook')
        except:
            error = QtWidgets.QMessageBox()
            error.setIcon(QtWidgets.QMessageBox.Warning)
            error.setText("Połączenie z serwerem nie zostało nawiązane.")
            error.setWindowTitle("Błąd!")
            return error.exec_()

        self.data = json.loads(resp.text)
        for key, value in self.data.items():
            self.itemModel.setItem(int(key), 0, QtGui.QStandardItem(value[1]))
            self.itemModel.setItem(int(key), 1, QtGui.QStandardItem(value[2]))

    def search(self):
        cache = self.lineEdit.text()
        self.clear_row()
        i = 0
        for key, value in self.data.items():
            if cache.upper() in value[1].upper() or cache.upper() in value[2].upper() or cache.upper() in '':
                self.itemModel.setItem(i, 0, QtGui.QStandardItem(value[1]))
                self.itemModel.setItem(i, 1, QtGui.QStandardItem(value[2]))
                i += 1

    def clear_row(self):
        for i in range(self.itemModel.rowCount()):
            self.itemModel.removeRow(i)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

