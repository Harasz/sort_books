# coding=utf-8
from PyQt5 import QtWidgets
from login import Ui_Form

class MainApplication(QtWidgets.QWidget, Ui_Form):
    def __init__(self, dialog):
        super(MainApplication, self).__init__()
        self.setupUi(dialog)
        self.dialog = dialog

    def loginAction(self):
        login = self.lineEdit.text()
        pass_ = self.lineEdit_2.text()

        if login is '' or pass_ is '':
            error = QtWidgets.QMessageBox()
            error.setIcon(QtWidgets.QMessageBox.Warning)
            error.setText("Uzupełnij wszystkie dane!")
            error.setWindowTitle("Błąd! Brak danych")
            return error.exec_()

        resp = requests.post('http://192.168.0.107:5000/api/logaction', data={'login': login, 'pass_': pass_})
        if resp.status_code == requests.codes.ok:
            self.data = json.loads(resp.text)
            self.dialog.close()
        else:
            error = QtWidgets.QMessageBox()
            error.setIcon(QtWidgets.QMessageBox.Warning)
            error.setText("Dane użyte do logowania są niepoprawne.")
            error.setWindowTitle("Błąd logowania")
            return error.exec_()


if '__main__' == __name__:
    import sys, json, requests
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    MainApplication(Form)

    Form.show()
    sys.exit(app.exec_())