# @IDEL      : PyCharm 
# @FileName  : mkdir.py
# @Time      : 2022/3/1 17:11
# @Author    : 简词海
import os
import sqlite3

pathFile = os.path.expanduser("~")


def file():
    if not os.path.exists(fr"{pathFile}\Jian"):
        os.mkdir(fr"{pathFile}\Jian")
        os.mkdir(fr"{pathFile}\Jian\text")
        conn = sqlite3.connect(rf"{pathFile}\Jian\hospitaNum.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE JIAN
                                                    (ID TEXT PRIMARY KEY   NOT NULL,
                                                     NUM             TEXT  NOT NULL);''')
        conn.commit()
        conn.close()

        conn = sqlite3.connect(rf"{pathFile}\Jian\hospitaFileWc.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE JIAN
                                                (ID TEXT PRIMARY KEY   NOT NULL,
                                                 NAME           TEXT  NOT NULL,
                                                 AGE            TEXT  NOT NULL,
                                                 SEX            TEXT   NOT NULL,
                                                 USERID         TEXT  NOT NULL,
                                                 KESI           TEXT  NOT NULL,
                                                 BINLI           TEXT  NOT NULL,
                                                 YP             TEXT  NOT NULL);''')
        conn.commit()
        conn.close()


        conn = sqlite3.connect(rf"{pathFile}\Jian\drug.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE JIAN
                                                (NAME TEXT PRIMARY KEY   NOT NULL,
                                                 NUM             TEXT  NOT NULL);''')
        conn.commit()
        conn.close()

        # conn = sqlite3.connect(rf"{pathFile}\Jian\hospitaFileWc.db")
        # c = conn.cursor()
        # c.execute('''CREATE TABLE JIAN
        #                                                 (ID TEXT PRIMARY KEY   NOT NULL,
        #                                                  NAME           TEXT  NOT NULL,
        #                                                  AGE            TEXT  NOT NULL,
        #                                                  SEX            TEXT   NOT NULL,
        #                                                  USERID         TEXT  NOT NULL,
        #                                                  KESI           TEXT  NOT NULL,
        #                                                  BINLI           TEXT  NOT NULL,
        #                                                  YP             TEXT  NOT NULL);''')
        # conn.commit()
        # conn.close()

        conn = sqlite3.connect(rf"{pathFile}\Jian\doctorFile.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE JIAN
                                                        (ID TEXT PRIMARY KEY   NOT NULL,
                                                         NAME           TEXT  NOT NULL,
                                                         SEX            TEXT  NOT NULL,
                                                         USERID         TEXT   NOT NULL,
                                                         KS             TEXT  NOT NULL,
                                                         WAGE           TEXT  NOT NULL,
                                                         XL             TEXT  NOT NULL,
                                                         DH             TEXT  NOT NULL);''')
        conn.commit()
        conn.close()


        list1 = ["内科", "外科", "脑科", "儿科", "骨科", "口鼻科", "中医科", "妇产科", "男科", "泌尿科", "美容科"]
        for i in list1:
            conn = sqlite3.connect(rf"{pathFile}\Jian\{i}hospitaFile.db")
            c = conn.cursor()
            c.execute('''CREATE TABLE JIAN
                                                                                (ID TEXT PRIMARY KEY   NOT NULL,
                                                                                 NAME           TEXT  NOT NULL,
                                                                                 AGE            TEXT  NOT NULL,
                                                                                 SEX            TEXT   NOT NULL,
                                                                                 USERID         TEXT  NOT NULL,
                                                                                 KESI           TEXT  NOT NULL,
                                                                                 BINLI           TEXT  NOT NULL);''')
            conn.commit()
            conn.close()