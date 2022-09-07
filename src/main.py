import os
import sys
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QPolygonF, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QDialog, QFileDialog, QListWidgetItem, QGraphicsScene
from modelos.ponto import Ponto
from modelos.reta import Reta
from modelos.poligono import Poligono
from leitor_xml import LeitorEntradaXml
from escritor_xml import gera_arquivo_saida
from transformacao import Transformacao
import matplotlib.colors as mcolors


def browseFiles():
    '''
    Função que carrega o arquivo xml e já realiza a transformação dos pontos do objeto geométrico.

    '''
    try:
        # Configurando o botão Open File para abrir uma janela no diretório raiz
        arquivo_xml = QFileDialog.getOpenFileName(QDialog(), "Open File", "\\")

        # Realizando parse de xml para uma lista de palavras
        dados_entrada.append(LeitorEntradaXml(
            arquivo_xml[0]).getDadosEntradaCompletos())

        # Por facilidade criei uma lista para colocar o dicionário,
        # assim eu preciso pegar a posição 0 da lista que é o próprio dicionário
        dados_entrada_dict = dados_entrada[0]

        # Configurando a cena com o tamanho da viewport passada
        scene.setSceneRect(
            0, 0, dados_entrada_dict["viewport"].xvmax, dados_entrada_dict["viewport"].yvmax)

        # Realiza a transformação em cima dos dados lidos
        transformacao = Transformacao(
            dados_entrada_dict['window'], dados_entrada_dict['viewport'])

        for w_ponto in dados_entrada_dict['pontos']:
            v_ponto = transformacao.transformada_ponto(w_ponto)
            dados_saida.append(v_ponto)

        for w_reta in dados_entrada_dict['retas']:
            v_reta = transformacao.transformada_reta(w_reta)
            dados_saida.append(v_reta)

        for w_poligono in dados_entrada_dict['poligonos']:
            v_poligono = transformacao.transformada_poligono(w_poligono)
            dados_saida.append(v_poligono)

        # Adiciona cada objeto na lista
        for objeto in dados_saida:
            ui.list_objects.addItem(objeto.__str__())

        atualiza_objeto()

        # Salvando o arquivo
        nome_arquivo_saida = '..\saida.csv'
        gera_arquivo_saida(dados_saida, nome_arquivo_saida)
    except:
        pass


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
    # Dicionário de cores para os objetos geométricos
    dict_colors = mcolors.TABLEAU_COLORS
    list_colors_iter = iter(dict_colors)

    # Limpa a tela
    scene.clear()

    # Adicionando retângulo conforme o viewport passado
    scene.addRect(0, 0, dados_entrada[0]["viewport"].xvmax,
                  dados_entrada[0]["viewport"].yvmax, QPen(QColor("black")))

    for index in range(ui.list_objects.count()):
        # Adicionando uma cor para cada objeto
        color = next(list_colors_iter)
        brush = QBrush(QColor(dict_colors[color]))

        if ui.list_objects.item(index).checkState() == QtCore.Qt.Checked:
            pen = QPen(brush, 3)

            if isinstance(dados_saida[index], Ponto):
                scene.addEllipse(
                    dados_saida[index].x, dados_saida[index].y, 1, 1, pen)
            elif isinstance(dados_saida[index], Reta):
                scene.addLine(dados_saida[index].p1.x, dados_saida[index].p1.y,
                              dados_saida[index].p2.x, dados_saida[index].p2.y, pen)
            elif isinstance(dados_saida[index], Poligono):
                polygon = QPolygonF()
                for ponto in dados_saida[index].lista_pontos:
                    polygon.append(QPointF(ponto.x, ponto.y))

                scene.addPolygon(polygon, pen)

            ui.graphics_view_viewport.setScene(scene)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    scene = QGraphicsScene()
    dados_entrada = []

    ui = uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "sistema-grafico.ui"))
    ui.show()

    # Tamanho da janela padrão
    scene.addRect(10, 10, 630, 470, QPen(QColor("black")))
    ui.graphics_view_viewport.setScene(scene)

    # Procurando arquivo no diretorio
    dados_saida = []

    # Ao butão button_open for clicado, chama a função browseFiles
    ui.button_open.clicked.connect(browseFiles)

    # Ao pressionar na lista de objetos os objetos serão atualizados
    ui.list_objects.pressed.connect(exibe_na_viewport)

    # Fechando janela
    ui.button_close.clicked.connect(QtCore.QCoreApplication.instance().quit)
    sys.exit(app.exec_())
