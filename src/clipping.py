from PyQt5.QtWidgets import QDialog, QGraphicsScene

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
    elif ui.checkBox_ponto.isChecked():
        ## TODO Fazer clipping poligono
        pass

