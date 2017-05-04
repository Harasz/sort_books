# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editReader.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from error import check_con, app_error
import requests
import json


class Ui_Dialog(object):

    na = None

    def setupUi(self, Dialog, Sec, Config):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Dialog = Dialog
        self.Sec = Sec
        self.Config = Config
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.doEdit)
        self.buttonBox.rejected.connect(self.doEdit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Imię: "))
        self.label_2.setText(_translate("Dialog", "Nazwisko: "))
        self.label_3.setText(_translate("Dialog", "Miasto: "))
        self.label_4.setText(_translate("Dialog", "Ulica i nr. domu"))


    def getData(self, na):

        self.na = na

        try:
            resp = requests.post(self.Config.get_server()+'/api/userinfo',
                                 data={'key': open('.cache', 'r').read(),
                                       'arg1': self.Sec.encrypt_(str(na))})
            if check_con(resp):
                return False
        except:
            return app_error("Wystąpił błąd podczas pobierania informacji.")

        data = self.Sec.encode_data(json.loads(resp.text))
        data['data'][1] = data['data'][1].split(' ')
        data['data'][2] = data['data'][2].split(', ')

        self.lineEdit.setText(data['data'][1][0])
        self.lineEdit_2.setText(data['data'][1][1])
        self.lineEdit_3.setText(data['data'][2][0])
        self.lineEdit_4.setText(data['data'][2][1])
        return self.Dialog.show()


    def doEdit(self):
        pass
