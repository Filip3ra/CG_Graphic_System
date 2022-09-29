from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPolygonF, QPen, QColor, QBrush
from PyQt5.QtWidgets import QDialog, QFileDialog, QListWidgetItem, QGraphicsScene, QLineEdit, QLabel
import matplotlib.colors as mcolors
from PyQt5 import QtCore

from leitor_xml import LeitorEntradaXml
from modelos.ponto import Ponto
from modelos.reta import Reta
from modelos.poligono import Poligono
from mapeadores.window_to_viewport import TransformadaViewport

def realiza_transformacao_dados(dados_entrada_dict: dict,
                                dados_saida: list):
    '''
    Realiza a transformação em cima dos dados de entrada lidos.
    '''

    dados_saida.clear()
    
    transformacao = TransformadaViewport(
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


def atualiza_lista_objetos(ui: QDialog,
                           dados_saida: list):
    '''
    Função que limpa e atualiza a lista de objetos conforme os objetos presentes na lista dados_saida
    '''
    ui.list_objects.clear()
    for objeto in dados_saida:
        ui.list_objects.addItem(objeto.__str__())


def browseFiles(ui: QDialog,
                dados_entrada: list,
                dados_saida: list,
                scene: QGraphicsScene):
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
            0, 0, 
            dados_entrada_dict["viewport"].ponto_max.x, 
            dados_entrada_dict["viewport"].ponto_max.y
        )

        realiza_transformacao_dados(dados_entrada_dict= dados_entrada_dict, 
                                    dados_saida= dados_saida)

        # Adiciona cada objeto na lista
        atualiza_lista_objetos(ui = ui, 
                            dados_saida=dados_saida)

        exibe_na_viewport(ui= ui,
                        scene=scene,
                        dados_entrada=dados_entrada,
                        dados_saida=dados_saida)
    except:
        pass


def atualiza_objeto(ui: QDialog):
    '''
    Atualizando objeto para ficar com o checkbox False
    '''
    item = QListWidgetItem()
    for index in range(ui.list_objects.count()):
        item = ui.list_objects.item(index)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        item.setCheckState(QtCore.Qt.Unchecked)
        ui.list_objects.addItem(item)


def exibe_na_viewport(ui: QDialog,
                      scene: QGraphicsScene,
                      dados_entrada: list,
                      dados_saida: list):
    ''' 
    Verifica quais itens estão selecionados, os que estiverem selecionados serão exibidos na viewport.
    '''
    atualiza_objeto(ui= ui)

    # Dicionário de cores para os objetos geométricos
    dict_colors = mcolors.TABLEAU_COLORS
    list_colors_iter = iter(dict_colors)

    # Limpa a tela
    scene.clear()

    # Adicionando retângulo conforme o viewport passado
    scene.addRect(0, 0, 
                  dados_entrada[0]["viewport"].ponto_max.x,
                  dados_entrada[0]["viewport"].ponto_max.y,
                  QPen(QColor("black")))

    for index in range(ui.list_objects.count()):
        # Adicionando uma cor para cada objeto
        color = next(list_colors_iter)
        brush = QBrush(QColor(dict_colors[color]))

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


# link referencia --> https://pythonpyqt.com/pyqt-label/
# TODO como configurar 'self' nessa função? igual o exemplo do link...
def adiciona_objeto():
    label_x1 = QLabel('&label_ponto_1_x')
    x1_LineEdit = QLineEdit()
    label_x1.setBuddy(x1_LineEdit)

    print(x1_LineEdit)


def att_opcao_selecionada(ui: QDialog):
    # Verifica o tipo do objeto
    if ui.radioButton_ponto.isChecked():
        ui.label_ponto_1_x.setDisabled(False)
        ui.text_x_1.setDisabled(False)
        ui.label_ponto_1_y.setDisabled(False)
        ui.text_y_1.setDisabled(False)

        ui.label_ponto_2_x.setDisabled(True)
        ui.text_x_2.setDisabled(True)
        ui.label_ponto_2_y.setDisabled(True)
        ui.text_y_2.setDisabled(True)

        ui.label_ponto_3_x.setDisabled(True)
        ui.text_x_3.setDisabled(True)
        ui.label_ponto_3_y.setDisabled(True)
        ui.text_y_3.setDisabled(True)

    elif ui.radioButton_reta.isChecked():
        # Se for a reta precisa permitir os campos de texto 2
        ui.label_ponto_1_x.setDisabled(False)
        ui.text_x_1.setDisabled(False)
        ui.label_ponto_1_y.setDisabled(False)
        ui.text_y_1.setDisabled(False)

        ui.label_ponto_2_x.setDisabled(False)
        ui.text_x_2.setDisabled(False)
        ui.label_ponto_2_y.setDisabled(False)
        ui.text_y_2.setDisabled(False)

        ui.label_ponto_3_x.setDisabled(True)
        ui.text_x_3.setDisabled(True)
        ui.label_ponto_3_y.setDisabled(True)
        ui.text_y_3.setDisabled(True)

    elif ui.radioButton_poligono.isChecked():
        # Se for um poligono reta precisa permitir os campos de texto 2 e 3,
        # e o botão de adicionar mais pontos
        ui.label_ponto_1_x.setDisabled(False)
        ui.text_x_1.setDisabled(False)
        ui.label_ponto_1_y.setDisabled(False)
        ui.text_y_1.setDisabled(False)

        ui.label_ponto_2_x.setDisabled(False)
        ui.text_x_2.setDisabled(False)
        ui.label_ponto_2_y.setDisabled(False)
        ui.text_y_2.setDisabled(False)

        ui.label_ponto_3_x.setDisabled(False)
        ui.text_x_3.setDisabled(False)
        ui.label_ponto_3_y.setDisabled(False)
        ui.text_y_3.setDisabled(False)
        ui.button_add_ponto.setDisabled(False)

