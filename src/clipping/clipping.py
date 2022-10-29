from PyQt5.QtWidgets import QDialog, QGraphicsScene

from clipping.poligonos import clipping_poligono
from graficos import atualiza_lista_objetos, exibe_na_viewport
from modelos.reta import Reta

def verifica_clipping(ui: QDialog, 
                      scene: QGraphicsScene, 
                      dados_entrada: list,
                      dados_saida: list):

    if ui.checkBox_ponto.isChecked():
        ## TODO Fazer clipping ponto
        pass
    elif ui.checkBox_reta.isChecked():
        if ui.radioButton_liang.isChecked():
            for index in range(len(dados_saida)):
                if isinstance(dados_saida[index], Reta):
                    dados_saida[index].clipping_liang_barsky(dados_entrada= dados_entrada[0])
        elif ui.radioButton_cohen.isChecked():
            ## TODO Fazer clipping reta por Cohen -Sutherland
            pass
    elif ui.checkBox_poligono.isChecked():
        ## TODO Fazer clipping poligono
        clipping_poligono(ui= ui,
                          dados_entrada= dados_entrada,
                          dados_saida= dados_saida)

    atualiza_lista_objetos(ui= ui,
                           dados_saida= dados_saida)
    exibe_na_viewport(ui= ui,
                      scene= scene,
                      dados_entrada=dados_entrada,
                      dados_saida= dados_saida)

