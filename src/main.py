'''
Equipe: André Vinícius e Filipi Maciel
Disciplina: Computação Gráfica 2/2022
'''

import os
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QGraphicsScene

from aplicacao import aplicacao

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    scene = QGraphicsScene()

    ui = uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "sistema-grafico.ui"))

    # Tamanho da janela padrão
    scene.addRect(10, 10, 630, 470, QPen(QColor("black")))
    ui.graphics_view_viewport.setScene(scene)

    ui.show()
    aplicacao(ui = ui, scene = scene)


    sys.exit(app.exec_())