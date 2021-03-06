# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updata.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sqlite3
import sys
import time
import scr.bj_rc
import scr.mkdir as file
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from scr import DoctorMain


class Ui_MainWindow(object):
    def __init__(self):
        self.pathFile = os.path.expanduser("~")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 170, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -80, 681, 541))
        self.label.setStyleSheet("image: url(:/icon/pr.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 220, 171, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 165, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 215, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 300, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 300, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-color: rgb(255, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(lambda: self.pubt_1())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????"))
        self.label_3.setText(_translate("MainWindow", "??????"))
        self.label_4.setText(_translate("MainWindow", "??????"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????"))
        self.label_5.setText(_translate("MainWindow", "??????"))

    def pubt_1(self):
        if self.lineEdit.text() and self.lineEdit_3.text():
            conn = sqlite3.connect(rf"{self.pathFile}\Jian\doctorFile.db")
            c = conn.cursor()
            drug = c.execute("""select ID, USERID, KS from JIAN""")
            for i in drug:
                if self.lineEdit.text() == i[0] and self.lineEdit_3.text() == i[1][12:]:
                    time.sleep(1)
                    DoctorMain.Ui_MainWindow(f"{i[2]}hospitaFile.db").setupUi(m)
                    m.show()
            c.close()

# XJ-6115-ID-14538


if __name__ == '__main__':
    file.file()
    app = QApplication(sys.argv)
    m = QMainWindow()
    # ??????????????????
    Ui_MainWindow().setupUi(m)
    # ????????????
    m.show()
    sys.exit(app.exec_())
