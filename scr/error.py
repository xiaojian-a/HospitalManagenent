# @IDEL      : PyCharm 
# @FileName  : error.py
# @Time      : 2022/3/1 0:31
# @Author    : 简词海
from PyQt5.QtWidgets import QWidget, QMessageBox
from pyqt5_plugins.examplebuttonplugin import QtGui


class Win(QWidget):
    def __init__(self, monye):
        super().__init__()
        self.monye = monye

    def show_message(self, hint, content):
        QMessageBox.warning(self, f"{hint}", f"{content}", QMessageBox.Cancel)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', f'将花费：{self.monye}元\n确定购买吗?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False


