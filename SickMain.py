# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sqlite3
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication, QMainWindow
import sys
import random
from PyQt5.QtCore import QStringListModel
import scr.mab_rc
from scr.mkdir import file
from scr.error import Win


class Ui_MainWindow(object):
    def __init__(self):
        self.app = Win(0)
        self.num = 0
        self.listFile = []
        self.pathFile = os.path.expanduser("~")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 190, 211, 481))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 70, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 150, 198, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_01 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setObjectName("pushButton_01")
        self.verticalLayout.addWidget(self.pushButton_01)
        self.pushButton_02 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setObjectName("pushButton_02")
        self.verticalLayout.addWidget(self.pushButton_02)
        self.pushButton_03 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setObjectName("pushButton_03")
        self.verticalLayout.addWidget(self.pushButton_03)
        self.pushButton_04 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_04.setFont(font)
        self.pushButton_04.setObjectName("pushButton_04")
        self.verticalLayout.addWidget(self.pushButton_04)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(260, 160, 621, 511))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_23 = QtWidgets.QLabel(self.page_4)
        self.label_23.setGeometry(QtCore.QRect(30, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(self.page_4)
        self.label_22.setGeometry(QtCore.QRect(30, 70, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_9.setGeometry(QtCore.QRect(502, 107, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_11.setGeometry(QtCore.QRect(55, 201, 521, 291))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textEdit_12 = QtWidgets.QTextEdit(self.page_4)
        self.textEdit_12.setGeometry(QtCore.QRect(200, 120, 250, 30))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_7 = QtWidgets.QTextEdit(self.page_4)
        self.textEdit_7.setGeometry(QtCore.QRect(200, 70, 250, 30))
        self.textEdit_7.setObjectName("textEdit_7")
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.label_21 = QtWidgets.QLabel(self.page_3)
        self.label_21.setGeometry(QtCore.QRect(380, 90, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_20 = QtWidgets.QLabel(self.page_3)
        self.label_20.setGeometry(QtCore.QRect(40, 90, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")

        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(350, 200, 250, 250))
        self.label_3.setStyleSheet("image: url(:/icon/vx);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 250, 250))
        self.label_4.setStyleSheet("image: url(:/icon/zfb);")
        self.label_4.setObjectName("label_4")


        self.stackedWidget.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 430, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_3.setGeometry(QtCore.QRect(140, 280, 230, 30))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_5.setGeometry(QtCore.QRect(520, 340, 80, 30))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(10, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.comboBox_4 = QtWidgets.QComboBox(self.page)
        self.comboBox_4.setGeometry(QtCore.QRect(140, 220, 230, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_4.setGeometry(QtCore.QRect(140, 340, 230, 30))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(10, 150, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 430, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(230, 80, 202, 29))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(10, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(427, 90, 202, 29))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(210, 20, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(390, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.textEdit_6 = QtWidgets.QTextEdit(self.page)
        self.textEdit_6.setGeometry(QtCore.QRect(140, 150, 300, 30))
        self.textEdit_6.setObjectName("textEdit_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.page)
        self.comboBox_3.setGeometry(QtCore.QRect(510, 80, 91, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(10, 270, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.textEdit_5 = QtWidgets.QTextEdit(self.page)
        self.textEdit_5.setGeometry(QtCore.QRect(310, 80, 80, 30))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_8 = QtWidgets.QTextEdit(self.page)
        self.textEdit_8.setGeometry(QtCore.QRect(120, 80, 80, 30))
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_24 = QtWidgets.QLabel(self.page)
        self.label_24.setGeometry(QtCore.QRect(10, 80, 201, 29))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_24.raise_()
        self.label_13.raise_()
        self.textEdit_5.raise_()
        self.pushButton_5.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_5.raise_()
        self.label_16.raise_()
        self.comboBox_4.raise_()
        self.textBrowser_4.raise_()
        self.label_12.raise_()
        self.pushButton_6.raise_()
        self.label_18.raise_()
        self.label_14.raise_()
        self.label_11.raise_()
        self.label_19.raise_()
        self.textEdit_6.raise_()
        self.comboBox_3.raise_()
        self.label_17.raise_()
        self.textEdit_8.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_6.setGeometry(QtCore.QRect(310, 10, 300, 490))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.listView = QtWidgets.QListView(self.page_2)
        self.listView.setGeometry(QtCore.QRect(70, 10, 191, 490))
        self.listView.setObjectName("listView")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.slm = QStringListModel()
        for i in os.listdir(rf"{self.pathFile}\Jian\text"):
            self.listFile.append(i[:-4])

        self.slm.setStringList(self.listFile)
        self.listView.setModel(self.slm)
        self.pushButton_01.clicked.connect(lambda: self.btn1_fun())
        self.pushButton_02.clicked.connect(lambda: self.btn2_fun())
        self.pushButton_03.clicked.connect(lambda: self.btn3_fun())
        self.pushButton_04.clicked.connect(lambda: self.btn4_fun())
        self.pushButton_5.clicked.connect(lambda: self.btn5_fun())
        self.pushButton_6.clicked.connect(lambda: self.btn6_fun())
        self.pushButton_9.clicked.connect(lambda: self.btn7_fun())
        self.listView.clicked.connect(self.delaFile)

        self.retranslateUi(MainWindow)
        # self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btn1_fun(self):
        self.stackedWidget.setCurrentIndex(2)

    def btn2_fun(self):
        self.stackedWidget.setCurrentIndex(3)

    def btn3_fun(self):
        self.stackedWidget.setCurrentIndex(1)

    def btn4_fun(self):
        self.stackedWidget.setCurrentIndex(0)

    def btn5_fun(self):

        self.textBrowser_3.clear()

        name = self.textEdit_8.toPlainText()
        age = self.textEdit_5.toPlainText()
        user = self.textEdit_6.toPlainText()
        sex = self.comboBox_3.currentText()
        admin = self.comboBox_4.currentText()

        if name and age and user and len(user) == 18:
            strUserId = "XJ" + str(random.randint(10000, 99999)) + "-ID" + str(random.randint(1000, 9999))
            self.textBrowser_3.append(strUserId)  # ????????????????????????????????????
            self.cursor = self.textBrowser_3.textCursor()
            self.textBrowser_3.moveCursor(self.cursor.End)  # ???????????????????????????????????????????????????
            QtWidgets.QApplication.processEvents()  # ??????????????????????????????????????????

            conn = sqlite3.connect(rf"{self.pathFile}\Jian\{admin}hospitaFile.db")
            c = conn.cursor()
            sql = '''INSERT INTO JIAN (ID, NAME,AGE, SEX, USERID, KESI, BINLI) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')''' % (
            strUserId, name, age, sex, user, admin, " ")
            c.execute(sql)
            conn.commit()
            conn.close()
            self.num += 1

            # ???????????????????????????
            conn0 = sqlite3.connect(rf"{self.pathFile}\Jian\hospitaNum.db")
            c0 = conn0.cursor()
            c0.execute("SELECT max(rowid) from JIAN")
            n = c0.fetchone()[0]
            conn0.commit()

            sql = '''INSERT INTO JIAN (ID, NUM) VALUES ('%s', '%s')''' % (strUserId, n)
            c0.execute(sql)
            conn0.commit()
            conn0.close()

            self.textBrowser_4.append(str(self.num))  # ????????????????????????????????????
            self.cursor = self.textBrowser_4.textCursor()
            self.textBrowser_4.moveCursor(self.cursor.End)  # ???????????????????????????????????????????????????
            if n is None:
                n = 0
            self.textBrowser_5.append(str(n))  # ????????????????????????????????????
            self.cursor = self.textBrowser_5.textCursor()
            self.textBrowser_5.moveCursor(self.cursor.End)  # ???????????????????????????????????????????????????
            QtWidgets.QApplication.processEvents()  # ??????????????????????????????????????????
            self.app.show_message("??????", "????????????????????????????????????")
            time.sleep(5)
            self.textEdit_8.clear()
            self.textEdit_5.clear()
            self.textEdit_6.clear()
            self.textBrowser_3.clear()
            self.textBrowser_4.clear()
            self.textBrowser_5.clear()
        else:
            self.app.show_message("??????", "???????????????")

    def btn6_fun(self):
        self.textBrowser_3.clear()
        self.textEdit_8.clear()
        self.textEdit_5.clear()
        self.textEdit_6.clear()

    def btn7_fun(self):
        id = self.textEdit_7.toPlainText()
        name = self.textEdit_12.toPlainText()
        if id and name:
            conn1 = sqlite3.connect(rf"{self.pathFile}\Jian\hospitaFileWc.db")
            c1 = conn1.cursor()
            sun = c1.execute(
                "select ID, NAME,AGE, SEX, USERID, KESI, BINLI, YP from JIAN ")
            for i in sun:
                if id == i[0] and name == i[1]:
                    self.textBrowser_11.clear()
                    self.textBrowser_11.append("?????????" + i[6] + "\n?????????" + i[7])
                    self.textEdit_7.clear()
                    self.textEdit_12.clear()
                    c1.close()
                    break
            else:
                Win(0).show_message("??????", "?????????????????????")
                self.textEdit_7.clear()
                self.textEdit_12.clear()
                c1.close()


    def delaFile(self, qModelIndex):
        str1 = self.listFile[qModelIndex.row()]
        self.textBrowser_6.clear()
        with open(rf"{self.pathFile}\Jian\text/" + str(str1) + ".txt", "r") as f:
            st = f.read()
            self.textBrowser_6.append(st)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????"))
        self.groupBox.setTitle(_translate("MainWindow", "??????"))
        self.label.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton_01.setText(_translate("MainWindow", "??????"))
        self.pushButton_02.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton_03.setText(_translate("MainWindow", "??????"))
        self.pushButton_04.setText(_translate("MainWindow", "????????????"))
        self.label_23.setText(_translate("MainWindow", "?????????"))
        self.label_22.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton_9.setText(_translate("MainWindow", "??????"))
        self.label_21.setText(_translate("MainWindow", "???????????????"))
        self.label_20.setText(_translate("MainWindow", "????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "??????"))
        self.label_16.setText(_translate("MainWindow", "???????????????"))
        self.label_12.setText(_translate("MainWindow", "???????????????"))
        self.pushButton_6.setText(_translate("MainWindow", "??????"))
        self.label_13.setText(_translate("MainWindow", "?????????"))
        self.label_18.setText(_translate("MainWindow", "?????????"))
        self.label_14.setText(_translate("MainWindow", "?????????"))
        self.label_11.setText(_translate("MainWindow", "?????????????????????"))
        self.label_19.setText(_translate("MainWindow", "???????????????"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "???"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "???"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "??????"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "??????"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "??????"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "??????"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "??????"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "?????????"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "?????????"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "?????????"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "??????"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "?????????"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "?????????"))
        self.label_17.setText(_translate("MainWindow", "????????????"))
        self.label_24.setText(_translate("MainWindow", "?????????"))


if __name__ == '__main__':
    file()
    app = QApplication(sys.argv)
    m = QMainWindow()
    # ??????????????????
    Ui_MainWindow().setupUi(m)
    # ????????????
    m.show()
    sys.exit(app.exec_())
