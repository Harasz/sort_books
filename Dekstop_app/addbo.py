# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_bo.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_Form(object):
    def setupUi(self, Form):
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
        self.label.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
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
        self.label_2.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
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
        self.pushButton.setStyleSheet("border: none;\n"
"border-bottom: 3px solid rgb(0, 85, 255);\n"
"background-color: grey;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.add_book)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Autor: "))
        self.label_2.setText(_translate("Form", "Tytuł: "))
        self.pushButton.setText(_translate("Form", "Dodaj"))

    def add_book(self):
        author = self.lineEdit.text()
        title = self.lineEdit_2.text()

        if author is '' or title is '':
            error = QtWidgets.QMessageBox()
            error.setIcon(QtWidgets.QMessageBox.Warning)
            error.setText("Uzupełnij wszystkie dane!")
            error.setWindowTitle("Błąd!")
            return error.exec_()

        try:
            resp = requests.post('http://192.168.0.107:5000/api/addbook', data={'arg1': title, 'arg2': author})
        except:
            self.label_3.setStyleSheet("color: red;")
            return self.label_3.setText("Błąd połączenia z serwerem")

        if 507 == resp.status_code:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label_3.setStyleSheet("color: orange;")
            return self.label_3.setText("Książka istnieje w bazie.")
        elif 201 == resp.status_code:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label_3.setStyleSheet("color: green;")
            return self.label_3.setText("Książka dodana do bazy.")
        else:
            self.label_3.setStyleSheet("color: red;")
            return self.label_3.setText("Nieznany błąd.")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

