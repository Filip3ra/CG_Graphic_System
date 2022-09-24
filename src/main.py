'''
Equipe: André Vinícius e Filipi Maciel
Disciplina: Computação Gráfica 2/2022
'''

import os
import sys
from this import d
import numpy as np
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QPolygonF, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QDialog, QFileDialog, QListWidgetItem, QGraphicsScene, QLineEdit, QLabel
import matplotlib.colors as mcolors

from modelos.ponto import Ponto
from modelos.reta import Reta
from modelos.poligono import Poligono
from leitor_xml import LeitorEntradaXml
from escritor_xml import gera_arquivo_saida
from modelos.viewport import Viewport
from modelos.window import Window
from transformacao import Transformacao
from transformacoes_geometricas import TransformacaoGeometrica


def atualiza_lista_objetos():
    '''
    Função que limpa e atualiza a lista de objetos conforme os objetos presentes na lista dados_saida
    '''
    ui.list_objects.clear()
    for objeto in dados_saida:
        ui.list_objects.addItem(objeto.__str__())


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

        dados_saida.append(dados_entrada_dict['window'])
        dados_saida.append(dados_entrada_dict['viewport'])

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
        atualiza_lista_objetos()

        exibe_na_viewport()

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
    atualiza_objeto()

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


def att_opcao_selecionada():
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


def controle_diminuir():
    tag = 'Diminuir'
    ui.list_transformacoes.addItem(tag)


def controle_ampliar():
    tag = 'Ampliar'
    ui.list_transformacoes.addItem(tag)


def controle_girar_negativamente():
    tag = 'Girar Negativo'
    ui.list_transformacoes.addItem(tag)


def controle_girar_positivamente():
    tag = 'Girar Positivo'
    ui.list_transformacoes.addItem(tag)


def controle_cima():
    tag = 'Cima'
    ui.list_transformacoes.addItem(tag)


def controle_baixo():
    tag = 'Baixo'
    ui.list_transformacoes.addItem(tag)


def controle_esquerda():
    tag = 'Esquerda'
    ui.list_transformacoes.addItem(tag)


def controle_direita():
    tag = 'Direita'
    ui.list_transformacoes.addItem(tag)


def adiciona_lista_transformacoes():
    '''
    De acordo com a descrição na lista de transformações, 
    é adicionado na matriz de transformações a transformações da descrição passada.
    '''
    for index in range(ui.list_transformacoes.count()):
        # Verifica qual objeto está marcado na lista de objetos
        item_lista_transformacoes = ui.list_transformacoes.item(index).text()
        if item_lista_transformacoes == 'Ampliar':
            transformacoes.escala(1.1, 1.1)
        elif item_lista_transformacoes == 'Diminuir':
            transformacoes.escala(0.9, 0.9)
        elif item_lista_transformacoes == 'Girar Negativo':
            # Rotacionando -10° = -0.1745 rad
            transformacoes.rotacao(-0.1745)
        elif item_lista_transformacoes == 'Girar Positivo':
            # Rotacionando 10° = 0.1745 rad
            transformacoes.rotacao(-0.1745)
        elif item_lista_transformacoes == 'Cima':
            # Transladando 10 unidades para cima em Y
            transformacoes.translacao(0, 10)
        elif item_lista_transformacoes == 'Baixo':
            # Transladando 10 unidades para baixo em X
            transformacoes.translacao(0, -10)
        elif item_lista_transformacoes == 'Esquerda':
            # Transladando 10 unidades para esquerda em X
            transformacoes.translacao(-10, 0)
        elif item_lista_transformacoes == 'Direita':
            # Transladando 10 unidades para direita em X
            transformacoes.translacao(10, 0)


def aplica_transformacoes_objetos(index: int):
    '''
    Verifica qual objeto geometrico e aplica a transformação.
    '''
    if isinstance(dados_saida[index], Ponto):
        dados_saida[index] = transformacoes.aplica_transformacoes_ponto(
            dados_saida[index])
    elif isinstance(dados_saida[index], Reta):
        dados_saida[index] = transformacoes.aplica_transformacoes_reta(
            dados_saida[index])
    elif isinstance(dados_saida[index], Poligono):
        dados_saida[index] = transformacoes.aplica_transformacoes_poligono(
            dados_saida[index])
    else:
        raise TypeError("Tipo de objeto não encontrado!")


def constroi_matriz_transformacoes(index: int):
    '''
    Constroi a matriz de transformações.
    '''
    # Transladando o centro do objeto para posição (0,0)
    x_centro, y_centro = dados_saida[index].centro_objeto()
    transformacoes.translacao(-x_centro, -y_centro)

    # Aplicando as transformações que estiverem na lista de transformações
    adiciona_lista_transformacoes()

    # Transladando o centro do objeto (0,0) para posição original
    transformacoes.translacao(x_centro, y_centro)


def verifica_transformacoes():
    if (len(dados_entrada) < 1) & (len(dados_saida) < 1):
        # Não possui dados
        print('O arquivo XML inserido está incorreto ou não foi inserido o arquivo de entrada.')
        pass
    else:        
        flag_checked_object = False
        # Verifica se a transformação será realizada com os objetos ou com a viewport

        if ui.radioButton_objetos.isChecked():
            for index in range(ui.list_objects.count()):
                # Verifica qual objeto está marcado na lista de objetos
                # Se tiver objeto marcado chama a função aplica_transformacoes
                # QtCore.Qt.Checked
                if ui.list_objects.item(index).checkState() > 1:
                    if flag_checked_object:
                        # Não precisa construir a matriz de transformações, pois já foi construída.
                        aplica_transformacoes_objetos(index)
                    else:
                        # Se não tiver encontrado nenhum objeto marcado ainda,
                        # precisa construir a matriz de transformações,
                        # depois aplica as transformações nos objetos marcados
                        constroi_matriz_transformacoes(index)
                        aplica_transformacoes_objetos(index)
                        flag_checked_object = True

            if not flag_checked_object:
                print('Objeto Geométrico não selecionado!')
        elif ui.radioButton_window.isChecked():
            ui.button_reset.setDisabled(True)
            # Procura o index da window na lista de dados_saida
            index = None
            for index_aux in range(len(dados_saida)):
                if isinstance(dados_saida[index_aux], Window):
                    index = index_aux
            if index is not None:
                constroi_matriz_transformacoes(index)
                dados_saida[index] = transformacoes.aplica_transformacoes_viewport(
                    viewport = dados_saida[index])
            else:
                print('Não foi encontrado o objeto window! Verifique se foi inserido o arquivo de entrada e se ele está correto.')

        # Limpa lista de objetos e carrega os objetos atualizados
        atualiza_lista_objetos()
        exibe_na_viewport()

        # Limpa matriz de transformações
        transformacoes.limpar()

        # Limpa lista de transformações
        ui.list_transformacoes.clear()


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

    # Ao pressionar o botão de adicionar um objeto, chama a função
    ui.button_atualizar.pressed.connect(att_opcao_selecionada)
    ui.button_adicionar.pressed.connect(adiciona_objeto)

    transformacoes = TransformacaoGeometrica()

    # Ao clicar nos butões das transformações geométricas
    # é chamada a função específica para aquele butão
    ui.button_diminuir.clicked.connect(controle_diminuir)
    ui.button_ampliar.clicked.connect(controle_ampliar)
    ui.button_girar_negativo.clicked.connect(controle_girar_negativamente)
    ui.button_girar_positivo.clicked.connect(controle_girar_positivamente)
    ui.button_cima.clicked.connect(controle_cima)
    ui.button_baixo.clicked.connect(controle_baixo)
    ui.button_esquerda.clicked.connect(controle_esquerda)
    ui.button_direita.clicked.connect(controle_direita)

    # Ao clicar em Aplicar, chama a função verifica_transformacoes
    ui.button_aplicar.clicked.connect(verifica_transformacoes)

    # Fechando janela
    ui.button_close.clicked.connect(QtCore.QCoreApplication.instance().quit)
    sys.exit(app.exec_())
