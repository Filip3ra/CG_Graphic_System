from PyQt5.QtWidgets import QDialog
from modelos.poligono import Poligono
from modelos.ponto import Ponto

from modelos.reta import Reta
from modelos.window import Window


# REGION CODES
RC_INSIDE = 0  # 0000
RC_LEFT = 1    # 0001
RC_RIGHT = 2   # 0010
RC_BOTTOM = 4  # 0100
RC_TOP = 8     # 1000

# A ideia é fazer um OU lógico pra saber quais equações vou usar no cálculo
# O operador '|=' realiza um OU lógico


def getRegionCode():

    # TODO - preciso acessar esses valores
    ponto = 0  # vai acessar o valor de x e y
    # vai acessar os valos min e max de x e y na window
    window_min_ponto, window_max_ponto = 0

    region_code = RC_INSIDE

    # verifica se x ta fora ou dentro da window
    if (ponto.x < window_min_ponto.x):
        region_code |= RC_LEFT
    elif (ponto.x > window_max_ponto.x):
        region_code |= RC_RIGHT

    # verifica se y ta fora ou dentro da window
    if (ponto.y < window_max_ponto.y):
        region_code |= RC_BOTTOM
    elif (ponto.y > window_max_ponto.y):
        region_code |= RC_TOP

    return region_code

# TODO verifica se os pontos da reta estão:
# - completamente dentro da window
# - completametne fora
# - parcialmente dentro/fora, deve ser clipado


def clipping_cohen_sutherland(ui: QDialog,
                              dados_entrada: list,
                              dados_saida: list):
    print("teste")

    # preciso tratar o region code primeiro, pra saber os quadrantes que a reta cruza
