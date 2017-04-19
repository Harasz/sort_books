from PyQt5 import QtWidgets


def check_con(resp):
    if resp.status_code == 401:
        app_error("Błąd autoryzacji.", True)
        return True
    if resp.status_code == 500:
        app_error("Błąd przy połączeniu z serwerem. Spróbuj ponownie za chwilę.")
        return True
    return False


def app_error(text, conn=False):
    error = QtWidgets.QMessageBox()
    error.setIcon(QtWidgets.QMessageBox.Warning)
    error.setText(text)
    error.setWindowTitle("Błąd!")
    error.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if conn:
        error.setDetailedText("Aby ponownie uzyskać autoryzację ze strony serwera zrestartuj aplikację.\nW razie dalszych problemów skontaktuj się z administratorem.")
    return error.exec_()