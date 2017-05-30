# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from login import Login_form
from window import Sort_books
from error import app_error
from serverConfig import ServerConfig
from secure import Secure


class MainApplication(QtWidgets.QWidget, Login_form, Sort_books):


    def __init__(self, dialog, window):
        super(MainApplication, self).__init__()
        self.setupUi(dialog)
        self.dialog = dialog
        self.window = window

        self.Config = ServerConfig()
        self.Sec = Secure()

        self.get_key()
        self.dialog.show()


    def loginAction(self):
        login = self.lineEdit.text()
        pass_ = self.lineEdit_2.text()

        if login is '' or pass_ is '':
            return app_error("Uzupełnij wszystkie dane.")

        try:
            resp = requests.post(self.Config.get_server()+'/api/logaction',
                                 data={'login': self.Sec.encrypt_(login),
                                       'pass_': self.Sec.encrypt_(pass_),
                                       'publicKey': self.Sec.get_public()})
        except requests.ConnectionError as e:
            return app_error("Nie można nawiązać połączenia z serwerem.", e)

        if resp.status_code == 200:
            data = json.loads(resp.text)
            try:
                open('.cache', "wb").write(data['auth'].encode())
            except PermissionError:
                os.remove('.cache')
                open('.cache', "wb").write(data['auth'].encode())
            ctypes.windll.kernel32.SetFileAttributesW('.cache', 0x02)
            self.dialog.close()
            return self.st_ap(self.Sec.decrypt_(data['master']), self.Sec.decrypt_(data['data']))
        elif resp.status_code == 406:
            return app_error("Dane użyte do logowania są niepoprawne.")
        else:
            return app_error("Wystąpił nieznany błąd podczas przetwarzania danych.")

    def st_ap(self, data, date):
        self.setupUi_2(self.window, self.Config, self.Sec, data, date)
        self.retranslateUi_2(self.window)
        return self.window.show()

    def get_key(self, stop=False):
        try:
            resp = requests.get(self.Config.get_server()+'/api/key')
        except requests.ConnectionError as e:
            app_error("Nie można nawiązać połączenia z serwerem.", e)
            return exit()

        if resp.status_code == 200:
            data = json.loads(resp.text)
            self.Sec.load_other_key(data['publicKey'])
        else:
            if stop:
                return exit()
            else:
                app_error("Wystąpił problem z wczytaniem kluczy")
            return self.get_key(stop=True)


if '__main__' == __name__:
    import sys
    import json
    import requests
    import os
    import ctypes

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    MainWindow = QtWidgets.QMainWindow()
    MainApplication(Form, MainWindow)
    app.exec_()
    sys.exit(os.remove('.cache'))
