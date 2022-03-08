# @IDEL      : PyCharm 
# @FileName  : error.py
# @Time      : 2022/3/1 0:31
# @Author    : 简词海
from PyQt5.QtWidgets import QWidget, QMessageBox


class Win(QWidget):
    def show_message(self, hint, content):
        QMessageBox.warning(self, f"{hint}", f"{content}", QMessageBox.Cancel)


