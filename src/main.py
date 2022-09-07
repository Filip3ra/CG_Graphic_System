import os
import sys
from PyQt5 import uic,QtCore, QtWidgets
from PyQt5.QtGui import QPolygonF,QPen,QBrush, QColor
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QDialog,QFileDialog,QListWidgetItem, QGraphicsScene
from modelos.ponto2d import Ponto2D_int
from modelos.reta import Reta
from modelos.poligono import Poligono
from leitor_xml import LeitorEntradaXml
from transformacao import Transformacao

def browseFiles():
    arquivo_xml = QFileDialog.getOpenFileName(QDialog(), "Open File","\\")
    print(f'Carregou {arquivo_xml}')

    ## Realizando parse de xml para uma lista de palavras
    dados_entrada.append(LeitorEntradaXml(arquivo_xml[0]).getDadosEntradaCompletos())
    dados_entrada_dict = dados_entrada[0]

    scene.setSceneRect(0, 0, dados_entrada_dict["viewport"].xvmax,dados_entrada_dict["viewport"].yvmax)
    
    # executo transformação em cima dos dados lidos
    transformacao = Transformacao(dados_entrada_dict['window'], dados_entrada_dict['viewport'])

    dados_saida = {
        'pontos': [],
        'retas': [],
        'poligonos': []
    }

    for w_ponto in dados_entrada_dict['pontos']:
        v_ponto = transformacao.transformada_ponto(w_ponto)
        dados_saida_.append(v_ponto)

    for w_reta in dados_entrada_dict['retas']:
        v_reta = transformacao.transformada_reta(w_reta)
        dados_saida_.append(v_reta)

    for w_poligono in dados_entrada_dict['poligonos']:
        v_poligono = transformacao.transformada_poligono(w_poligono)
        dados_saida['poligonos'].append(v_poligono)
        dados_saida_.append(v_poligono)            

    ## Adiciona cada objeto na lista
    '''
    for objeto in dados_saida:
        for dados_objeto in dados_saida[objeto]:
            print(dados_objeto)
            ui.list_objects.addItem(dados_objeto.__str__())
    '''
    for objeto in dados_saida_:
        ui.list_objects.addItem(objeto.__str__())

    atualiza_objeto()

    return dados_saida_

def atualiza_objeto():
    '''
    Atualizando objeto para ficar com o checkbox False
    '''
    item = QListWidgetItem()
    for index in range(ui.list_objects.count()):
        item = ui.list_objects.item(index)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        item.setCheckState(QtCore.Qt.Unchecked)
        ui.list_objects.addItem(item)

def exibe_na_viewport():
    ''' 
    Verifica quais itens estão selecionados, os que estiverem selecionados serão exibidos na viewport.
    '''
    ## Limpa a tela
    scene.clear()
    scene.addRect(0, 0, dados_entrada[0]["viewport"].xvmax,dados_entrada[0]["viewport"].yvmax,QPen(QColor("black")))
    for index in range(ui.list_objects.count()):
        if ui.list_objects.item(index).checkState() == QtCore.Qt.Checked:

            if isinstance(dados_saida_[index], Ponto2D_int):
                scene.addEllipse(dados_saida_[index].x, dados_saida_[index].y, 1, 1)
            elif isinstance(dados_saida_[index], Reta):
                scene.addLine(dados_saida_[index].p1.x, dados_saida_[index].p1.y, 
                              dados_saida_[index].p2.x, dados_saida_[index].p2.y)
            elif isinstance(dados_saida_[index], Poligono):
                ## Precisa desenhar poligono
                pen = QPen(Qt.red)
                greenBurh = QBrush(Qt.green)
                polygon = QPolygonF()
                for ponto in dados_saida_[index].lista_pontos:
                    polygon.append(QPoint(ponto.x, ponto.y))

                scene.addPolygon(polygon)

            ui.graphics_view_viewport.setScene(scene)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    scene = QGraphicsScene()
    dados_entrada = []

    ui = uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "sistema-grafico.ui"))
    ui.show()

    ## Tamanho da janela padrão
    scene.addRect(10, 10, 630, 470, QPen(QColor("black")))
    ui.graphics_view_viewport.setScene(scene)

    # Procurando arquivo no diretorio
    dados_saida_ = []
    ui.button_open.clicked.connect(browseFiles)

    # Ao pressionar na lista de objetos os objetos serão atualizados
    ui.list_objects.pressed.connect(exibe_na_viewport)

    ## Fechando janela
    ui.button_close.clicked.connect(Dialog.close)
    sys.exit(app.exec_())