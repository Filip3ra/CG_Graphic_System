
# Arquivo teste para verificar se o QT(pyside6) está funcionando corretamente

from cProfile import label
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt
from qdarktheme import load_stylesheet
import sys


class Window(QMainWindow):
    def __init__(self):     # dunder init?
        super().__init__()  # 

        base = QWidget()
        layout = QGridLayout()
        font = QFont()

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

        self.setCentralWidget(base)
        menu = self.menuBar()
        arquivo_menu = menu.addMenu('Arquivo')
        action = QAction('Print!')
        arquivo_menu.addAction(action)


app = QApplication()
app.setStyleSheet(load_stylesheet())
window = Window()
window.show()

app.exec()
