from PyQt5.QtWidgets import QDialog, QGraphicsScene

from graficos import atualiza_lista_objetos, exibe_na_viewport
from modelos.poligono import Poligono
from modelos.ponto import Ponto
from modelos.reta import Reta

def verifica_clipping(ui: QDialog, 
                      scene: QGraphicsScene, 
                      dados_entrada: list,
                      dados_saida: list):

    if ui.checkBox_ponto.isChecked():
        ## TODO Fazer clipping ponto
        for index in range(len(dados_saida)):
            if isinstance(dados_saida[index], Ponto):
                dados_saida[index].clipping_ponto(dados_entrada= dados_entrada[0],
                                                  dados_saida= dados_saida)
    elif ui.checkBox_reta.isChecked():
        if ui.radioButton_liang.isChecked():
            for index in range(len(dados_saida)):
                if isinstance(dados_saida[index], Reta):
                    dados_saida[index].clipping_liang_barsky(dados_entrada= dados_entrada[0])
        elif ui.radioButton_cohen.isChecked():
            ## TODO Fazer clipping reta por Cohen -Sutherland
            for index in range(len(dados_saida)):
                if isinstance(dados_saida[index], Reta):
                    dados_saida[index].clipping_cohen_sutherland(dados_entrada= dados_entrada[0])
    elif ui.checkBox_poligono.isChecked():
        ## TODO Fazer clipping poligono
        for index in range(len(dados_saida)):
            if isinstance(dados_saida[index], Poligono):
                dados_saida[index].clipping_poligono(dados_entrada= dados_entrada[0],
                                                     dados_saida= dados_saida)

    atualiza_lista_objetos(ui= ui,
                           dados_saida= dados_saida)
    exibe_na_viewport(ui= ui,
                      scene= scene,
                      dados_entrada=dados_entrada,
                      dados_saida= dados_saida)

'''

RETAS COHEN SUTHERLAND:
Preciso identificar o local que a reta corta minha janela.

Uma reta pode estar cruzando nossa janela em quatro locais, o topo, o fundo, o lado direito e esquerdo. 
Cada um desses locais possuem uma equação específica que o método Cohen Sutherland utiliza.

m = (y2-y1)/(x2-x1)

Esquerda = y = m * (Xe - X1) + y1
Direita = y = m * (Xd - X1) + y1
Topo = x = x1 + 1/m * (yt - y1)
Fundo = x = x1 + 1/m * (yf - y1)

Após calcular o 'm' e as duas equações referentes aos pontos de corte, tenho meu 'x' e 'y' referentes ao 
ponto de interseção. 

RETA LIANG BARSKY:
#TODO

'''
