# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from login import Login_form
from window import Sort_books
from error import app_error

class MainApplication(QtWidgets.QWidget, Login_form, Sort_books):


    def __init__(self, dialog, window):
        super(MainApplication, self).__init__()
        self.setupUi(dialog)
        self.dialog = dialog
        self.window = window

        self.dialog.show()


    def loginAction(self):
        login = self.lineEdit.text()
        pass_ = self.lineEdit_2.text()

        if login is '' or pass_ is '':
            return app_error("Uzupełnij wszystkie dane.")

        try:
            resp = requests.post('http://192.168.0.107:5000/api/logaction', data={'login': login, 'pass_': pass_})
        except:
            return app_error("Nie można nawiązać połączenia z serwerem.")

        if resp.status_code == 200:
            self.data = json.loads(resp.text)
            open('.cache', "w").write(self.data['auth'])
            ctypes.windll.kernel32.SetFileAttributesW('.cache' ,0x02)
            self.dialog.close()
            return self.st_ap()
        else:
            return app_error("Dane użyte do logowania są niepoprawne")


    def st_ap(self):
        self.setupUi_2(self.window)
        self.retranslateUi_2(self.window)
        return self.window.show()


if '__main__' == __name__:
    import sys, json, requests, os, ctypes
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    MainWindow = QtWidgets.QMainWindow()
    MainApplication(Form, MainWindow)
    app.exec_()
    sys.exit(os.remove('.cache'))