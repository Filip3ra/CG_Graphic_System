
# Arquivo teste para verificar se o QT(pyside6) está funcionando corretamente

from cProfile import label
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt
from qdarktheme import load_stylesheet
import sys

def callback():
    print('Cliquei no botão!!!')

    
def callback2():
    print('Callback 2')

class Window(QMainWindow):
    def __init__(self):     # dunder init?
        super().__init__()  # 

        base = QWidget()
        layout = QGridLayout()
        font = QFont()

        font.setPixelSize(90)
        base.setFont(font)

        self.lablel_ = QLabel('ola!')
        #self.lablel_.setFont(font)
        self.lablel_.setAlignment(Qt.AlignCenter)

        botao = QPushButton('Botao!')
        #botao.setFont(font)
        #botao.clicked.connect(callback)
        botao.clicked.connect(self.muda_label)

        layout.addWidget(self.lablel_)
        layout.addWidget(botao)

        base.setLayout(layout)

        self.setCentralWidget(base)
        menu = self.menuBar()
        arquivo_menu = menu.addMenu('Arquivo')
        action = QAction('Print!')
        action.triggered.connect(callback2)
        arquivo_menu.addAction(action)

    def muda_label(self):
        self.lablel_.setText('Clicado!')


app = QApplication()
app.setStyleSheet(load_stylesheet())
window = Window()
window.show()

app.exec()
