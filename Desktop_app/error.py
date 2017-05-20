from PyQt5 import QtWidgets


def check_con(resp):
    if resp.status_code == 401:
        app_error("Błąd autoryzacji.", "Aby ponownie uzyskać autoryzację ze strony serwera zrestartuj aplikację.\n"
                              "W razie dalszych problemów skontaktuj się z administratorem.")
        return True
    if resp.status_code == 500:
        app_error("Błąd przy połączeniu z serwerem. Spróbuj ponownie za chwilę.")
        return True
    return False


def app_error(text, e=''):
    error = QtWidgets.QMessageBox()
    error.setIcon(QtWidgets.QMessageBox.Warning)
    error.setText(text)
    error.setWindowTitle("Uwaga błąd! - Sort Books")
    error.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if e:
        error.setDetailedText(str(e))

    return error.exec_()
