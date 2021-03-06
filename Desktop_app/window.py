# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from error import check_con, app_error
import requests
import json


class Sort_books(object):

    cover = None

    def setupUi_2(self, MainWindow, Config, Sec, data, date):
        self.Config = Config
        self.Sec = Sec
        self.Window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(719, 398)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 211, 160))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 150, 211, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 250, 211, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(5, 0, 5, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, -20, 20, 391))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(229, -1, 481, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(9, 19, 461, 331))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 21))
        self.menubar.setObjectName("menubar")
        self.menuWebsite = QtWidgets.QMenu(self.menubar)
        self.menuWebsite.setObjectName("menuWebsite")
        self.menuLibrarians = QtWidgets.QMenu(self.menubar)
        self.menuLibrarians.setObjectName("menuLibrarians")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionComm = QtWidgets.QAction(MainWindow)
        self.actionComm.setObjectName("actionComm")
        self.actionLibrarians = QtWidgets.QAction(MainWindow)
        self.actionLibrarians.setObjectName("actionLibrarians")
        self.passLibrarians = QtWidgets.QAction(MainWindow)
        self.passLibrarians.setObjectName("passLibrarians")
        self.menuLibrarians.addAction(self.passLibrarians)
        self.infoLibrarians = QtWidgets.QAction(MainWindow)
        self.infoLibrarians.setObjectName("infoLibrarians")
        self.menuLibrarians.addAction(self.infoLibrarians)
        self.aboutLibrarians = QtWidgets.QAction(MainWindow)
        self.aboutLibrarians.setObjectName("aboutLibrarians")
        self.menuAbout.addAction(self.aboutLibrarians)
        self.addLibrarians = QtWidgets.QAction(MainWindow)
        self.addLibrarians.setObjectName("addLibrarians")
        if data.decode() == 'True':
            self.menuLibrarians.addAction(self.actionLibrarians)
            self.menuLibrarians.addAction(self.addLibrarians)
        self.menuWebsite.addAction(self.actionComm)
        self.menuWebsite.addSeparator()
        self.menubar.addAction(self.menuWebsite.menuAction())
        self.menubar.addAction(self.menuLibrarians.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.add_widget()

        self.retranslateUi_2(MainWindow)
        self.pushButton_2.clicked.connect(lambda: self.update_(self.Widgets['borrowView']['Ui']))
        self.pushButton_3.clicked.connect(lambda: self.update_(self.Widgets['readView']['Ui']))
        self.pushButton.clicked.connect(lambda: self.update_(self.Widgets['bookView']['Ui']))
        self.pushButton_4.clicked.connect(lambda: self.update_(self.Widgets['addbor']['Ui']))
        self.pushButton_5.clicked.connect(lambda: self.update_(self.Widgets['return_']['Ui']))
        self.pushButton_6.clicked.connect(lambda: self.update_(self.Widgets['addbo']['Ui']))
        self.pushButton_7.clicked.connect(lambda: self.update_(self.Widgets['addre']['Ui']))
        self.actionComm.triggered.connect(lambda: self.update_(self.Widgets['comments']['Ui']))
        self.actionLibrarians.triggered.connect(lambda: self.update_(self.Widgets['librarians']['Ui']))
        self.passLibrarians.triggered.connect(lambda: self.update_(self.Widgets['pass']['Ui']))
        self.addLibrarians.triggered.connect(lambda: self.update_(self.Widgets['addLib']['Ui']))
        self.aboutLibrarians.triggered.connect(lambda: self.update_(self.Widgets['about']['Ui']))
        self.infoLibrarians.triggered.connect(self.userInfo)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)

        if date.decode() == '1':
            self.needPass()


    def retranslateUi_2(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sort Books"))
        self.pushButton_2.setText(_translate("MainWindow", "Lista wypożyczeń"))
        self.pushButton_3.setText(_translate("MainWindow", "Lista czytelników"))
        self.pushButton.setText(_translate("MainWindow", "Lista książek"))
        self.pushButton_4.setText(_translate("MainWindow", "Wypożycz książkę"))
        self.pushButton_5.setText(_translate("MainWindow", "Zwróc książkę"))
        self.pushButton_6.setText(_translate("MainWindow", "Dodaj książkę"))
        self.pushButton_7.setText(_translate("MainWindow", "Dodaj czytelnika"))
        self.groupBox.setTitle(_translate("MainWindow", "Sort Books"))
        self.menuWebsite.setTitle(_translate("MainWindow", "Strona"))
        self.menuLibrarians.setTitle(_translate("MainWindow", "Biblioteka"))
        self.actionComm.setText(_translate("MainWindow", "Komentarze"))
        self.actionLibrarians.setText(_translate("MainWindow", "Konta"))
        self.passLibrarians.setText(_translate("MainWindow", "Zmień hasło"))
        self.infoLibrarians.setText(_translate("MainWindow", "Moje konto"))
        self.addLibrarians.setText(_translate("MainWindow", "Dodaj konto"))
        self.menuAbout.setTitle(_translate("MainWindow", "Projekt"))
        self.aboutLibrarians.setText(_translate("MainWindow", "O projekcie"))


    def update_(self, to_update):
        self.clearWidget()
        to_update.show_()


    def add_widget(self):

        self.Widgets = {}

        modules_name = ('addre', 'addbo', 'addbor', 'readView', 'bookView', 'borrowView',
                        'return_', 'comments', 'addLib', 'librarians', 'pass', 'about')
        modules = []

        for modul in modules_name:
            modules.append(__import__('lib.'+modul, None, None, [None], 0))

        for widget in range(len(modules)):
            self.Widgets[modules_name[widget]] = {}
            if widget < 9:
                self.Widgets[modules_name[widget]]['Widget'] = QtWidgets.QWidget(self.Window)
                self.gridLayout.addWidget(self.Widgets[modules_name[widget]]['Widget'], 0, 0, 0, 0)
            else:
                self.Widgets[modules_name[widget]]['Widget'] = QtWidgets.QDialog(self.Window)
            self.Widgets[modules_name[widget]]['Ui'] = modules[widget].Ui_Form()
            self.Widgets[modules_name[widget]]['Ui'].setupUi(self.Widgets[modules_name[widget]]['Widget'],
                                                             self.Config, self.Sec)
            self.Widgets[modules_name[widget]]['Widget'].hide()


    def clearWidget(self):
        for i in range(self.gridLayout.count() - 1, -1, -1):
            widget = self.gridLayout.itemAt(i).widget()
            if widget.objectName() != 'groupBox':
                widget.hide()


    def userInfo(self):

        try:
            resp = requests.post(self.Config.get_server()+'/api/librariansinfo',
                                 data={'key': open('.cache', 'r').read()})
            if check_con(resp):
                return False
        except Exception as e:
            return app_error("Wystąpił błąd podczas pobierania informacji.", e)

        data = self.Sec.encode_data(json.loads(resp.text))['data']

        master = ""
        if data[3] == 'True':
            master = "Jesteś zarządcą\n"

        text = "Informacje o twoim koncie:\n\nImię: "+data[0]+"\nNazwisko: "+data[1]+"\nE-mial: "+data[2]+"\n"+master
        return self.infoBox(text, "Informacje o koncie - Sort Books")


    def needPass(self):
        self.infoBox("Od ostatniej zmiany hasła minął ponad miesiąc. Ze względów bezpieczeństwa zalecamy je zmienić.",
                     "Zmien hasło - Sort Books")
        return self.update_(self.Widgets['pass']['Ui'])

    def infoBox(self, text, title):
        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setText(text)
        info.setWindowTitle(title)
        info.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return info.exec_()
