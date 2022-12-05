# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_password.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from sqlalchemy_test import *

class change_PW(object):
	def setupUi(self, Dialog):
		self.tablename = user
		Dialog.setObjectName("Dialog")
		Dialog.resize(940, 617)
		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(460, 550, 93, 28))
		font = QtGui.QFont()
		font.setFamily("Lucida Handwriting")
		font.setPointSize(10)
		self.pushButton.setFont(font)
		self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(42, 70, 135);\n"
"    color:rgb(255,255,255);\n"
"    border:1px outset rgb(255, 255, 255);\n"
"    border-radius:8px;\n"
"} ")
		self.pushButton.setObjectName("pushButton")
		self.listView = QtWidgets.QListView(Dialog)
		self.listView.setGeometry(QtCore.QRect(-20, 0, 1141, 771))
		self.listView.setStyleSheet("background-image: url(\"C:/Users/KEVIN/Desktop/Login_system/Login_system/login_system\");\n"
"background-color: rgb(255, 255, 255);\n"
"")
		self.listView.setObjectName("listView")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(170, 410, 141, 31))
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
		brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
		self.label.setPalette(palette)
		font = QtGui.QFont()
		font.setFamily("Lucida Calligraphy")
		self.label.setFont(font)
		self.label.setMouseTracking(True)
		self.label.setTabletTracking(False)
		self.label.setFocusPolicy(QtCore.Qt.NoFocus)
		self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
		self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.label.setFrameShadow(QtWidgets.QFrame.Plain)
		self.label.setLineWidth(0)
		self.label.setMidLineWidth(0)
		self.label.setTextFormat(QtCore.Qt.RichText)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(30, 470, 261, 31))
		font = QtGui.QFont()
		font.setFamily("Lucida Handwriting")
		self.label_2.setFont(font)
		self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
		self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.label_2.setLineWidth(0)
		self.label_2.setObjectName("label_2")
		self.lineEdit = QtWidgets.QLineEdit(Dialog)
		self.lineEdit.setGeometry(QtCore.QRect(310, 410, 271, 31))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(12)
		self.lineEdit.setFont(font)
		self.lineEdit.setText("")
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
		self.lineEdit_2.setGeometry(QtCore.QRect(310, 470, 271, 31))
		self.lineEdit_2.setEchoMode(QLineEdit.Password)
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(12)
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setText("")
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.label_4 = QtWidgets.QLabel(Dialog)
		self.label_4.setGeometry(QtCore.QRect(310, 510, 271, 31))
		self.label_4.setStyleSheet('color: red')
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.listView.raise_()
		self.pushButton.raise_()
		self.label.raise_()
		self.label_2.raise_()
		self.lineEdit.raise_()
		self.lineEdit_2.raise_()
		self.label_4.raise_()

		self.pushButton.clicked.connect(self.change_pw)
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.pushButton.setText(_translate("Dialog", "Save"))
		self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Email :</span></p></body></html>"))
		self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Change password :</span></p></body></html>"))
		self.label_4.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
		self.label_4.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:9pt; font-weight:600; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

	def change_pw(self):
		email = self.lineEdit.text()
		password = self.lineEdit_2.text()

		if not email:
			self.label_4.setText('Please enter Email.')
			return
		if not password:
			self.label_4.setText('Please enter Password.')
			return
		Session = sessionmaker(bind=engine)
		session = Session()		

		if not session.query(self.tablename).filter_by(Email=email).first():
			self.label_4.setText('The Email does not exist.')

			session.commit()     #提交會話（事務） 
			session.rollback()     #回滾會話
			session.close()     #關閉會話	
			return
		changePW(self.tablename,email,password)
		self.label_4.setText('The password already change.')
		# Session = sessionmaker(bind=engine)
		# session = Session()		
		# if session.query(self.tablename).filter_by(Email=email).first():
		# 	self.label_4.setText('The Email already exists. Please change another Email.')


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = change_PW()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())

