from PyQt5.QtWidgets import QDialog
from modelos.poligono import Poligono
from modelos.ponto import Ponto

from modelos.reta import Reta
from modelos.window import Window


def clipping_cohen_sutherland(lista_pontos_inter: list,
                              lista_janela: list,
                              reta: Reta):

    for ponto_inter in lista_pontos_inter:
        if (reta.p1.x <= ponto_inter.x) & \
            (ponto_inter.x <= reta.p2.x) & \
            (reta.p1.y <= ponto_inter.y) & \
                (ponto_inter.y <= reta.p2.y):
