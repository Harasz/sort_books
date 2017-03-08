# coding=utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_Form

class MainApplication(QtWidgets.QWidget, Ui_Form):
    def __init__(self, dialog):
        super(MainApplication, self).__init__()
        while True:
            login = QtWidgets.QInputDialog.getText(self, "Logowanie do bazy", "Login: ")
            pass_ = QtWidgets.QInputDialog.getText(self, "Logowanie do bazy", "Haslo: ")
            if not login or not pass_:
                login = None
                pass_ = None
                QtWidgets.QMessageBox.warning(self, 'Błąd', 'Pusty login lub hasło!', QtWidgets.QMessageBox.Ok)
            else:
              self.setupUi(dialog)
              break

    def loginAction(self):
        login = self.loginInput.text()
        pass_ = self.passInput.text()

        if login is None or pass_ is None:
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Uzupełnij wszystkie dane!")
            error.setWindowTitle("Błąd! Brak danych.")
            return error.exec_()

        print(login)
        print(pass_)



if '__main__' == __name__:
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    MainApplication(Form)

    Form.show()
    sys.exit(app.exec_())