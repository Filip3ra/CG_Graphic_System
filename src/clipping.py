from PyQt5.QtWidgets import QDialog, QGraphicsScene

def clipping_poligono(ui: QDialog,
                      dados_entrada: list,
                      dados_saida: list):
    '''
    Algoritmo de clipping de Weiler-Atherton.
    '''
    ## 1 - Calcula pontos de interseção entre janela e polígono

    ## 2 - Cria lista dos polígonos

    ## 2.1 - Cria lista da janela

    ## 3 - Verifica pontos de entrada e saida

    ## 4 - Inicia pela lista do polígono, encontra o 1° ponto de entrada

    ## 5 - Se encontrar ponto de saída, procura ele na lista da janela

    ## 6 - Se encontrar ponto de janela, procura ele na lista de polígono

def verifica_clipping(ui: QDialog, 
                      scene: QGraphicsScene, 
                      dados_entrada: list,
                      dados_saida: list):

    if ui.checkBox_ponto.isChecked():
        ## TODO Fazer clipping ponto
        pass
    elif ui.checkBox_ponto.isChecked():
        if ui.radioButton_liang.isChecked():
            ## TODO Fazer clipping reta por Liang-Barsky
            pass
        elif ui.radioButton_cohen.isChecked():
            ## TODO Fazer clipping reta por Cohen -Sutherland
            pass
    elif ui.checkBox_poligono.isChecked():
        ## TODO Fazer clipping poligono
        clipping_poligono(ui= ui,
                          dados_entrada= dados_entrada,
                          dados_saida= dados_saida)

