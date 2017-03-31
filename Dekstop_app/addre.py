# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_re.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 117, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: none;\n"
"border-left: 1px solid grey;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 20, 271, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)

        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)

        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(264, 160, 111, 41))
        self.pushButton.setStyleSheet("border: none;\n"
"border-bottom: 3px solid rgb(0, 85, 255);\n"
"background-color: grey;")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(16, 162, 151, 31))
        self.label_4.setStyleSheet("color: green;")
        self.label_4.setObjectName("label_4")

        self.pushButton.clicked.connect(self.add_re)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Imię:"))
        self.label_2.setText(_translate("Form", "Nazwisko:"))
        self.label_3.setText(_translate("Form", "Miasto:"))
        self.label_5.setText(_translate("Form", "Ulica i nr domu:"))
        self.pushButton.setText(_translate("Form", "Dodaj czytelnika"))
        self.label_4.setText(_translate("Form", "."))

    def add_re(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        address = self.lineEdit_3.text()
        address_2 = self.lineEdit_4.text()

        if name is '' or surname is '' or address is '' or address_2 is '':
            error = QtWidgets.QMessageBox()
            error.setIcon(QtWidgets.QMessageBox.Warning)
            error.setText("Uzupełnij wszystkie dane!")
            error.setWindowTitle("Błąd!")
            return error.exec_()

        name = name+' '+surname
        address = address+', '+address_2

        try:
            resp = requests.post('http://192.168.0.107:5000/api/addre', data={'arg1': name, 'arg2': address})
        except:
            self.label_4.setStyleSheet("color: red;")
            return self.label_4.setText("Błąd połączenia z serwerem.")

        if 507 == resp.status_code:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.label_4.setStyleSheet("color: orange;")
            return self.label_4.setText("Czytelnik istnieje w bazie.")
        elif 201 == resp.status_code:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.label_4.setStyleSheet("color: green;")
            return self.label_4.setText("Czytelnik dodany do bazy.")
        else:
            self.label_4.setStyleSheet("color: red;")
            return self.label_4.setText("Nieznany błąd.")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

