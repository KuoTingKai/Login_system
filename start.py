# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from sign_in import *
from Login import *
from change_password import *



class LoginWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.main_ui = login()
        self.main_ui.setupUi(self)


class SignInWindow(QDialog):
    def __init__(self):
        super(SignInWindow,self).__init__()
        self.calendars = signIn()
        self.calendars.setupUi(self)

class ForgotWindow(QDialog):
    def __init__(self):
        super(ForgotWindow,self).__init__()
        self.calendars = change_PW()
        self.calendars.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = LoginWindow()
    SignInchild = SignInWindow()
    Forgorchild = ForgotWindow()

    btn = window.main_ui.pushButton_2
    btn.clicked.connect(SignInchild.show)

    btn = window.main_ui.pushButton_3
    btn.clicked.connect(Forgorchild.show)

    window.show()
    sys.exit(app.exec_())

