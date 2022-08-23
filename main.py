
# Arquivo teste para verificar se o QT(pyside6) está funcionando corretamente

from cProfile import label
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sys

def test():
    app = QApplication()
    base = QWidget()
    font = QFont()
    layout = QGridLayout()

    font.setPixelSize(90)

    lablel_ = QLabel('ola!')
    lablel_.setFont(font)
    lablel_.setAlignment(Qt.AlignCenter)

    botao = QPushButton('Botao!')
    botao2 = QPushButton('Botao2')
    botao3 = QPushButton('Botao3')
    botao4 = QPushButton('Botao4')
    botao.setFont(font)


    layout.addWidget(lablel_)
    layout.addWidget(botao)
    layout.addWidget(botao2)
    layout.addWidget(botao3)
    layout.addWidget(botao4)
    base.setLayout(layout)
    base.show()
    app.exec()


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

test()
