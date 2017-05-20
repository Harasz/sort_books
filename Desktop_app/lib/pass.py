# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pass.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from error import check_con, app_error
import requests

class Ui_Form(object):
    def setupUi(self, Form, Config, Sec):
        self.Form = Form
        self.Config = Config
        self.Sec = Sec
        Form.setObjectName("Form")
        Form.resize(400, 223)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(self.buttonBox.Cancel).setText("Anuluj")
        self.buttonBox.button(self.buttonBox.Save).setText("Zmień")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Form)

        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.buttonBox.button(self.buttonBox.Save).clicked.connect(self.doEdit)
        self.buttonBox.button(self.buttonBox.Cancel).clicked.connect(self.delEdit)

        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Zmiana hasła - Sort Books"))
        self.label.setText(_translate("Form", "Zmiana hasła dostępu do konta"))
        self.label_2.setText(_translate("Form", "Stare hasło: "))
        self.label_3.setText(_translate("Form", "Nowe hasło:"))
        self.label_4.setText(_translate("Form", "Powtórz nowe hasło:"))


    def show_(self):
        return self.Form.show()


    def delEdit(self):
        return self.Form.hide()

    def doEdit(self):
        old_pass = self.lineEdit_3.text()
        new_pass = self.lineEdit_2.text()
        new_pass_2 = self.lineEdit.text()

        if old_pass == '' or new_pass == '' or new_pass_2 == '':
            return app_error("Uzupełnij wszystkie dane.")

        if not new_pass == new_pass_2:
            app_error("Nowe hasła nie są identyczne!")
            return self.clearLine()

        try:
            resp = requests.post(self.Config.get_server()+'/api/changepass',
                                 data={'key': open('.cache', 'r').read(),
                                       'arg1': self.Sec.encrypt_(old_pass),
                                       'pass_': self.Sec.encrypt_(new_pass)})
            if check_con(resp):
                return False
        except Exception as e:
            return app_error("Wystąpił błąd podczas pobierania informacji.", e)

        if resp.status_code == 200:
            self.editInfo()
            return self.delEdit()
        elif resp.status_code == 409:
            self.clearLine()
            return app_error("Stare hasło nie jest poprawne.")
        else:
            return app_error("Wystąpił błąd przy zmianie hasła.")


    def editInfo(self):
        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setText("Hasło zostało pomyślnie zmienione.\n"
                     "Pamiętaj, aby je sobie zapisać.")
        info.setWindowTitle("Zmiana hasła - Sort Books")
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return info.exec_()


    def clearLine(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        return self.lineEdit_3.clear()
