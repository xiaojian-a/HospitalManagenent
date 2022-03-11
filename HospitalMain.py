# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledMain1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import random
import sqlite3
import time

from PyQt5.QtCore import QStringListModel

from scr.error import Win
from scr.mkdir import file
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication, QMainWindow
import sys


class Ui_MainWindow(object):
    def __init__(self):
        self.str6 = None
        self.str5 = None
        self.list5 = ["内科", "外科", "脑科", "儿科", "骨科", "口鼻科", "中医科", "妇产科", "男科", "泌尿科", "美容科"]
        self.list4 = []
        self.str_yp = None
        self.value = None
        self.list3 = ["阿莫西林", "心得安", "消心痛", "心痛定", "胃舒平", "消炎痛", "病毒矬", "去痛片", "健胃消食片", "慢心率", "大伦丁", "西地兰"]
        self.dict3 = {"阿莫西林": 30, "心得安": 68, "消心痛": 78, "心痛定": 56, "胃舒平": 99, "消炎痛": 16, "病毒矬": 56, "去痛片": 35,
                      "健胃消食片": 36, "慢心率": 89, "大伦丁": 35, "西地兰": 87}
        self.list2 = []
        self.pathFile = os.path.expanduser("~")
        self.list1 = []
        self.dict1 = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 151, 381))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 260, 125, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 50, 125, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 125, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 190, 125, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 330, 125, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 80, 551, 451))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listView = QtWidgets.QListView(self.page)
        self.listView.setGeometry(QtCore.QRect(20, 50, 160, 351))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.page)
        self.listView_2.setGeometry(QtCore.QRect(200, 50, 130, 350))
        self.listView_2.setObjectName("listView_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(370, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setGeometry(QtCore.QRect(380, 50, 130, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(470, 430, 72, 15))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(390, 310, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 360, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.listView_3 = QtWidgets.QListView(self.page_2)
        self.listView_3.setGeometry(QtCore.QRect(20, 50, 180, 350))
        self.listView_3.setObjectName("listView_3")
        self.slm = QStringListModel()

        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(230, 5, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(220, 50, 290, 350))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(330, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.listView_4 = QtWidgets.QListView(self.page_3)
        self.listView_4.setGeometry(QtCore.QRect(310, 60, 191, 281))
        self.listView_4.setObjectName("listView_4")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.listView_5 = QtWidgets.QListView(self.page_3)
        self.listView_5.setGeometry(QtCore.QRect(80, 60, 181, 181))
        self.listView_5.setObjectName("listView_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_3.setGeometry(QtCore.QRect(86, 280, 151, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_21 = QtWidgets.QLabel(self.page_3)
        self.label_21.setGeometry(QtCore.QRect(10, 280, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(80, 330, 151, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_22 = QtWidgets.QLabel(self.page_3)
        self.label_22.setGeometry(QtCore.QRect(10, 340, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_20 = QtWidgets.QLabel(self.page_3)
        self.label_20.setGeometry(QtCore.QRect(10, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_7.setGeometry(QtCore.QRect(110, 10, 151, 41))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 387, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(40, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 70, 280, 301))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_5.setGeometry(QtCore.QRect(340, 70, 180, 211))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(370, 25, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(180, 410, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_6.setGeometry(QtCore.QRect(330, 300, 201, 141))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.lineEdit = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 100, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 200, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.page_5)
        self.comboBox.setGeometry(QtCore.QRect(370, 40, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.page_5)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 72, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_5)
        self.label_14.setGeometry(QtCore.QRect(10, 120, 72, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setGeometry(QtCore.QRect(300, 40, 72, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_5)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 190, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_16 = QtWidgets.QLabel(self.page_5)
        self.label_16.setGeometry(QtCore.QRect(10, 190, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_5)
        self.label_17.setGeometry(QtCore.QRect(10, 260, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 260, 100, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_18 = QtWidgets.QLabel(self.page_5)
        self.label_18.setGeometry(QtCore.QRect(10, 330, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 330, 200, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 380, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_19 = QtWidgets.QLabel(self.page_5)
        self.label_19.setGeometry(QtCore.QRect(310, 260, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(390, 260, 100, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_1.clicked.connect(lambda: self.pub_ff5())
        self.pushButton_2.clicked.connect(lambda: self.pub_ff2())

        self.pushButton_3.clicked.connect(lambda: self.pub_ff3())
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_7.clicked.connect(lambda: self.pub_ff1())
        self.listView_3.clicked.connect(self.delaFile1)
        self.listView_5.clicked.connect(self.delaFile2)
        self.listView.clicked.connect(self.delaFile3)
        self.listView_2.clicked.connect(self.delaFile4)
        self.pushButton_8.clicked.connect(lambda: self.pub_ff4())
        self.pushButton.clicked.connect(lambda: self.pub_ff6())


        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pub_ff1(self):
        strUserId = "XJ-" + str(random.randint(1000, 9999)) + "-ID-" + str(random.randint(10000, 99999))
        name = self.lineEdit.text()
        sex = self.comboBox.currentText()
        id = self.lineEdit_2.text()
        zw = self.comboBox_2.currentText()
        wage = self.lineEdit_3.text()
        wl = self.lineEdit_5.text()
        onef = self.lineEdit_4.text()
        if name and sex and id and wage and wl and onef:
            conn = sqlite3.connect(rf"{self.pathFile}\Jian\doctorFile.db")
            c = conn.cursor()
            sql = '''INSERT INTO JIAN (ID, NAME, SEX, USERID, KS, WAGE, XL, DH) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')''' % (
                strUserId, name, sex, id, zw, wage, wl, onef)
            c.execute(sql)
            conn.commit()
            conn.close()
            Win(0).show_message("提示", f"工号为：{strUserId}\n名字为：{name}\n添加成功")
        else:
            Win(0).show_message("提示", "请正确输入")

        time.sleep(5)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()

    def pub_ff2(self):
        self.stackedWidget.setCurrentIndex(1)
        self.list1.clear()
        self.dict1.clear()
        conn = sqlite3.connect(rf"{self.pathFile}\Jian\hospitaFileWc.db")
        c = conn.cursor()
        hospitaList = c.execute('''select ID, NAME,AGE,SEX, USERID, KESI, BINLI, YP from JIAN''')
        for i in hospitaList:
            self.list1.append(i[0] + " " + i[1])
            hospitaFile = f"""病历号：{i[0]}\n姓名：{i[1]}\n年龄：{i[2]}, 性别：{i[3]}\n身份证：{i[4]}\n就诊科室：{i[5]}\n\n医嘱：{i[6]}\n\n药品：{i[7]} """
            self.dict1[i[0] + " " + i[1]] = hospitaFile
        self.slm.setStringList(self.list1)
        self.listView_3.setModel(self.slm)
        conn.commit()
        conn.close()

    def ypFile(self):
        self.list2.clear()
        conn = sqlite3.connect(rf"{self.pathFile}\Jian\drug.db")
        c = conn.cursor()
        drug = c.execute("""select NAME, NUM from JIAN""")
        for i in drug:
            self.list2.append(i[0] + "  " + i[1])
        c.close()
        self.slm = QStringListModel()
        self.slm.setStringList(self.list2)
        self.listView_4.setModel(self.slm)

    def pub_ff3(self):
        self.stackedWidget.setCurrentIndex(2)
        self.ypFile()
        self.slm = QStringListModel()
        self.slm.setStringList(self.list3)
        self.listView_5.setModel(self.slm)

    def pub_ff4(self):
        num = int(self.comboBox_3.currentText())
        moyne = str(num * self.value)
        self.textBrowser_3.append(moyne)
        if Win(moyne).closeEvent("提示"):
            conn = sqlite3.connect(rf"{self.pathFile}\Jian\drug.db")
            c = conn.cursor()
            sun = c.execute("select  NAME, NUM from JIAN ")
            for i in sun:
                if self.str_yp == i[0]:
                    add = int(i[1]) + num
                    sql = """UPDATE JIAN set NUM = '%s' where  NAME = '%s'""" % (add, self.str_yp)
                    c.execute(sql)
                    conn.commit()
                    c.close()
                    self.ypFile()
                    return
            else:
                conn = sqlite3.connect(rf"{self.pathFile}\Jian\drug.db")
                c = conn.cursor()
                sql = '''INSERT INTO JIAN (NAME, NUM ) VALUES ('%s', '%s')''' % (self.str_yp, num)
                c.execute(sql)
                conn.commit()
                c.close()
                self.ypFile()
                return
        else:
            Win(0).show_message("提示", "已取消购买")

    def pub_ff5(self):
        self.stackedWidget.setCurrentIndex(0)
        self.list4.clear()
        conn = sqlite3.connect(rf"{self.pathFile}\Jian\doctorFile.db")
        c = conn.cursor()
        drug = c.execute("""select ID, NAME, KS from JIAN""")
        for i in drug:
            self.list4.append(i[0] + "-" + i[1] + "-" + i[2])
        c.close()
        self.slm = QStringListModel()
        self.slm.setStringList(self.list4)
        self.listView.setModel(self.slm)
        
        self.slm = QStringListModel()
        self.slm.setStringList(self.list5)
        self.listView_2.setModel(self.slm)

    def pub_ff6(self):
        conn = sqlite3.connect(rf"{self.pathFile}\Jian\doctorFile.db")
        c = conn.cursor()
        sql = """UPDATE JIAN set KS = '%s' where  ID = '%s'""" % (self.str6, self.str5[0:16])
        c.execute(sql)
        conn.commit()
        c.close()
        self.textBrowser.clear()
        self.textBrowser.append(self.str5[0:20] + self.str6)

    def delaFile1(self, qModelIndex):
        str1 = self.list1[qModelIndex.row()]
        self.textBrowser_2.clear()
        value = self.dict1.get(str1)
        self.textBrowser_2.append(value)

    def delaFile2(self, qModelIndex):
        self.str_yp = self.list3[qModelIndex.row()]
        self.textBrowser_3.clear()
        self.value = self.dict3.get(self.str_yp)
    
    def delaFile3(self, qModelIndex):
        self.str5 = self.list4[qModelIndex.row()]

    def delaFile4(self, qModelIndex):
        self.str6 = self.list5[qModelIndex.row()]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "功能"))
        self.pushButton_4.setText(_translate("MainWindow", "财务管理"))
        self.pushButton_1.setText(_translate("MainWindow", "医生调动"))
        self.pushButton_2.setText(_translate("MainWindow", "病人管理"))
        self.pushButton_3.setText(_translate("MainWindow", "药品管理"))
        self.pushButton_6.setText(_translate("MainWindow", "医生入职"))
        self.label.setText(_translate("MainWindow", "医院终端管理系统"))
        self.label_2.setText(_translate("MainWindow", "医生："))
        self.label_3.setText(_translate("MainWindow", "选择科室："))
        self.label_4.setText(_translate("MainWindow", "结果："))
        self.label_5.setText(_translate("MainWindow", "医生调动"))
        self.pushButton.setText(_translate("MainWindow", "确定调动"))
        self.pushButton_5.setText(_translate("MainWindow", "删除"))
        self.label_6.setText(_translate("MainWindow", "病人名单："))
        self.label_7.setText(_translate("MainWindow", "详细信息显示："))
        self.label_8.setText(_translate("MainWindow", "药品剩余："))
        self.label_9.setText(_translate("MainWindow", "剩余资产："))
        self.label_21.setText(_translate("MainWindow", "数量："))
        self.label_22.setText(_translate("MainWindow", "价格："))
        self.label_20.setText(_translate("MainWindow", "购买："))
        self.pushButton_8.setText(_translate("MainWindow", "确定购买"))
        self.label_10.setText(_translate("MainWindow", "药品使用明细："))
        self.label_11.setText(_translate("MainWindow", "其他收入明细："))
        self.label_12.setText(_translate("MainWindow", "总入账金额："))
        self.comboBox.setItemText(0, _translate("MainWindow", "男"))
        self.comboBox.setItemText(1, _translate("MainWindow", "女"))
        self.label_13.setText(_translate("MainWindow", "姓名："))
        self.label_14.setText(_translate("MainWindow", "身份证："))
        self.label_15.setText(_translate("MainWindow", "性别："))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "内科"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "外科"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "脑科"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "儿科"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "骨科"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "口鼻科"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "中医科"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "妇产科"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "男科"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "泌尿科"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "美容科"))

        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "8"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "12"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "20"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "30"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "50"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "80"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "200"))
        self.label_16.setText(_translate("MainWindow", "医生职位："))
        self.label_17.setText(_translate("MainWindow", "工资："))
        self.label_18.setText(_translate("MainWindow", "电话："))
        self.pushButton_7.setText(_translate("MainWindow", "确定"))
        self.label_19.setText(_translate("MainWindow", "学历："))


if __name__ == '__main__':
    file()
    app = QApplication(sys.argv)
    m = QMainWindow()
    # 设置窗口尺寸
    Ui_MainWindow().setupUi(m)
    # 加载控件
    m.show()
    sys.exit(app.exec_())
