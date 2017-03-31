# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import addre, addbo, addbor, readView, bookView, borrowView

class Sort_books(object):
    def setupUi_2(self, MainWindow):
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
        MainWindow.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(0, 170, 255);\n"
"    border: none;\n"
"    border-left: 2px solid grey;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background-color: grey;\n"
"    border: none;\n"
"    border-left: 2px solid rgb(0, 170, 255);\n"
"}")
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
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.update_borrowList)
        self.pushButton_3.clicked.connect(self.update_readList)
        self.pushButton.clicked.connect(self.update_bookList)
        self.pushButton_4.clicked.connect(self.update_borrows)
        self.pushButton_5.clicked.connect(self.update_borrows)
        self.pushButton_6.clicked.connect(self.update_books)
        self.pushButton_7.clicked.connect(self.update_addre)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)

        #Add readers widget
        self.addre = QtWidgets.QWidget()
        self.addre_ui = addre.Ui_Form()
        self.addre_ui.setupUi(self.addre)
        self.addre.hide()

        # Add books widget
        self.books = QtWidgets.QWidget()
        self.books_ui = addbo.Ui_Form()
        self.books_ui.setupUi(self.books)
        self.books.hide()

        # Add borrows widget
        self.borrows = QtWidgets.QWidget()
        self.borrows_ui = addbor.Ui_Form()
        self.borrows_ui.setupUi(self.borrows)
        self.borrows.hide()

        # Read list widget
        self.reList = QtWidgets.QWidget()
        self.reList_ui = readView.Ui_Form()
        self.reList_ui.setupUi(self.reList)
        self.reList.hide()

        # Book list widget
        self.boList = QtWidgets.QWidget()
        self.boList_ui = bookView.Ui_Form()
        self.boList_ui.setupUi(self.boList)
        self.boList.hide()

        # Borrow list widget
        self.borList = QtWidgets.QWidget()
        self.borList_ui = borrowView.Ui_Form()
        self.borList_ui.setupUi(self.borList)
        self.borList.hide()

        self.gridLayout.addWidget(self.addre, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.books, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.borrows, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.reList, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.boList, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.borList, 0, 0, 1, 1)


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

    def update_addre(self):
        self.clearWidget()
        self.addre.show()

    def update_books(self):
        self.clearWidget()
        self.books.show()

    def update_borrows(self):
        self.clearWidget()
        self.borrows_ui.get_list()
        self.borrows.show()

    def update_readList(self):
        self.clearWidget()
        self.reList_ui.get_list()
        self.reList.show()

    def update_bookList(self):
        self.clearWidget()
        self.boList_ui.get_list()
        self.boList.show()

    def update_borrowList(self):
        self.clearWidget()
        self.borList_ui.get_list()
        self.borList.show()

    def clearWidget(self):
        for i in range(self.gridLayout.count() - 1, -1, -1):
            widget = self.gridLayout.itemAt(i).widget()
            if widget.objectName() != 'groupBox':
                widget.hide()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Sort_books()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

