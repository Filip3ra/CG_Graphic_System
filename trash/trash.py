
from cProfile import label
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt
import sys


def demo():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 300, 300)
    win.setWindowTitle("Demo App")
    lablee = QtWidgets.QLabel(win)
    lablee.setText("Rock koder")
    lablee.move(100, 100)

    win.show()
    sys.exit(app.exec_())
