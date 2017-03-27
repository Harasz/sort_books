# coding=utf-8
from PyQt5 import QtWidgets
from login import Login_form
from window import Sort_books

class MainApplication(QtWidgets.QWidget, Login_form, Sort_books):
    def __init__(self, dialog, window):
        super(MainApplication, self).__init__()
        self.setupUi(dialog)
        self.dialog = dialog
        self.window = window

        self.dialog.show()

    def loginAction(self):
        self.dialog.close()
        self.st_ap()
        #login = self.lineEdit.text()
        #pass_ = self.lineEdit_2.text()

        #if login is '' or pass_ is '':
         #   error = QtWidgets.QMessageBox()
          #  error.setIcon(QtWidgets.QMessageBox.Warning)
          #  error.setText("Uzupełnij wszystkie dane!")
          #  error.setWindowTitle("Błąd! Brak danych")
          #  return error.exec_()

        #resp = requests.post('http://192.168.0.107:5000/api/logaction', data={'login': login, 'pass_': pass_})
        #if resp.status_code == requests.codes.ok:
        #    self.data = json.loads(resp.text)
        #    self.dialog.close()
        #    return self.st_ap()
        #else:
        #    error = QtWidgets.QMessageBox()
        #    error.setIcon(QtWidgets.QMessageBox.Warning)
        #    error.setText("Dane użyte do logowania są niepoprawne.")
        #    error.setWindowTitle("Błąd logowania")
        #    return error.exec_()

    def st_ap(self):
        self.setupUi_2(self.window)
        self.retranslateUi_2(self.window)
        return self.window.show()

if '__main__' == __name__:
    import sys, json, requests
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    MainWindow = QtWidgets.QMainWindow()
    MainApplication(Form, MainWindow)
    app.exec_()