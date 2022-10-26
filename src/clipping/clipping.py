from PyQt5.QtWidgets import QDialog, QGraphicsScene

from clipping.poligonos import clipping_poligono

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

'''


PONTO:
#TODO

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