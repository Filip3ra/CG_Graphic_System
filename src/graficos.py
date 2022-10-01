from this import d
from PyQt5.QtCore import QPointF
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygonF, QPen, QColor, QBrush
from PyQt5.QtWidgets import QDialog, QFileDialog, QListWidgetItem, QGraphicsScene
import matplotlib.colors as mcolors
from PyQt5 import QtCore

from leitor_xml import LeitorEntradaXml
from modelos.ponto import Ponto
from modelos.reta import Reta
from modelos.poligono import Poligono
from mapeadores.window_to_viewport import TransformadaViewport
from escritor_xml import gera_arquivo_saida, guarda_arquivo_saida


def realiza_transformacao_dados(dados_entrada_dict: dict,
                                dados_saida: list,
                                dados_saida_xml):
    '''
    Realiza a transformação em cima dos dados de entrada lidos.
    '''

    dados_saida.clear()

    transformacao = TransformadaViewport(
        dados_entrada_dict['window'], dados_entrada_dict['viewport'])

    for w_ponto in dados_entrada_dict['pontos']:
        v_ponto = transformacao.transformada_ponto(w_ponto)
        dados_saida_xml['pontos'].append(v_ponto)
        dados_saida.append(v_ponto)

    for w_reta in dados_entrada_dict['retas']:
        v_reta = transformacao.transformada_reta(w_reta)
        dados_saida_xml['retas'].append(v_reta)
        dados_saida.append(v_reta)

    for w_poligono in dados_entrada_dict['poligonos']:
        v_poligono = transformacao.transformada_poligono(w_poligono)
        dados_saida_xml['poligonos'].append(v_poligono)
        dados_saida.append(v_poligono)

    gera_arquivo_saida(dados_saida_xml,'saida.xml')

    #guarda_arquivo_saida(dados_saida_xml)


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
                dados_saida_xml,
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

        realiza_transformacao_dados(dados_entrada_dict=dados_entrada_dict,
                                    dados_saida=dados_saida,
                                    dados_saida_xml=dados_saida_xml)

        # Adiciona cada objeto na lista
        atualiza_lista_objetos(ui=ui,
                               dados_saida=dados_saida)

        exibe_na_viewport(ui=ui,
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
    atualiza_objeto(ui=ui)

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


def adiciona_objeto(ui: QDialog,
                    scene: QGraphicsScene,
                    dados_entrada: list,
                    dados_saida: list):
    if ui.radioButton_ponto.isChecked():
        num_linhas = ui.tableWidget_objetos.rowCount()
        for linha in range(num_linhas):
            try:   
                valor_x = int(ui.tableWidget_objetos.item(linha, 0).text())
                valor_y = int(ui.tableWidget_objetos.item(linha, 1).text())
    
                ponto_aux = Ponto(valor_x, valor_y)
                ponto_aux.aplica_transformada(window=dados_entrada[0]['window'],
                                            viewport=dados_entrada[0]['viewport'])
                dados_saida.append(ponto_aux)
                del ponto_aux
            except:
                print('Digite os valores do ponto para o ponto!')
    elif ui.radioButton_reta.isChecked():
        try:    
            valor_x_1 = int(ui.tableWidget_objetos.item(0, 0).text())
            valor_y_1 = int(ui.tableWidget_objetos.item(0, 1).text())
            valor_x_2 = int(ui.tableWidget_objetos.item(1, 0).text())
            valor_y_2 = int(ui.tableWidget_objetos.item(1, 1).text())

            ponto_aux_1 = Ponto(valor_x_1, valor_y_1)
            ponto_aux_2 = Ponto(valor_x_2, valor_y_2)
            reta_aux = Reta(ponto_aux_1, ponto_aux_2)
            reta_aux.aplica_transformada(window=dados_entrada[0]['window'],
                                        viewport=dados_entrada[0]['viewport'])
            dados_saida.append(reta_aux)
            del reta_aux
        except:
            print('Digite os valores do ponto para a reta!')
    elif ui.radioButton_poligono.isChecked():
        lista_pontos = []
        num_linhas = ui.tableWidget_objetos.rowCount()
        if num_linhas >= 3:
            for linha in range(num_linhas):
                try:   
                    valor_x = int(ui.tableWidget_objetos.item(linha, 0).text())
                    valor_y = int(ui.tableWidget_objetos.item(linha, 1).text())
        
                    ponto_aux = Ponto(valor_x, valor_y)
                    
                    ponto_aux.aplica_transformada(window=dados_entrada[0]['window'],
                                                  viewport=dados_entrada[0]['viewport'])
                    lista_pontos.append(ponto_aux)
                    poligono_aux = Poligono(lista_pontos)
                    dados_saida.append(poligono_aux)
                    del ponto_aux
                except:
                    print('Digite os valores do ponto para o poligono!')
        else:
            print('Para formar um polígono é preciso pelo menos 3 pontos!')

    atualiza_lista_objetos(ui=ui,
                           dados_saida=dados_saida)

    exibe_na_viewport(ui=ui,
                      scene=scene,
                      dados_entrada=dados_entrada,
                      dados_saida=dados_saida)
    ui.tableWidget_objetos.setRowCount(0)
    ui.tableWidget_objetos.setColumnCount(2)
    return dados_saida

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


def reset_window(ui: QDialog,
                 scene: QGraphicsScene,
                 dados_entrada: list,
                 dados_saida: list):
    '''
    Reverte todas as transformações realizadas nos objetos, window e viewport, 
    voltando tudo as configurações originais do arquivo XML.
    '''
    dados_entrada[0]['window'].reset()
    dados_entrada[0]['viewport'].reset()

    for index in range(len(dados_saida)):
        dados_saida[index].reset()

    atualiza_lista_objetos(ui=ui,
                           dados_saida=dados_saida)

    exibe_na_viewport(ui=ui,
                      scene=scene,
                      dados_entrada=dados_entrada,
                      dados_saida=dados_saida)

def adiciona_lista_transformacoes(ui: QDialog):
    '''
    Adiciona a descrição das transformações na lista de transformações dos objetos.
    '''
    valor_x = ui.text_controle_x.toPlainText()
    valor_y = ui.text_controle_y.toPlainText()

    if ui.radioButton_translacao.isChecked():
        operacao = 'Translação'
    if ui.radioButton_rotacao.isChecked():
        operacao = 'Rotação'
    if ui.radioButton_escala.isChecked():
        operacao = 'Escala'

    num_linhas = ui.tableWidget.rowCount()
    ui.tableWidget.setRowCount(num_linhas+1)
    ui.tableWidget.setColumnCount(3)

    ui.tableWidget.setItem(num_linhas, 0, QtWidgets.QTableWidgetItem(operacao))
    ui.tableWidget.setItem(num_linhas, 1, QtWidgets.QTableWidgetItem(valor_x))
    ui.tableWidget.setItem(num_linhas, 2, QtWidgets.QTableWidgetItem(valor_y))

def adiciona_objeto_na_tabela(ui: QDialog):
    valor_x = ui.text_x.toPlainText()
    valor_y = ui.text_y.toPlainText()

    num_linhas = ui.tableWidget_objetos.rowCount()
    ui.tableWidget_objetos.setRowCount(num_linhas+1)
    ui.tableWidget_objetos.setColumnCount(2)

    ui.tableWidget_objetos.setItem(num_linhas, 0, QtWidgets.QTableWidgetItem(valor_x))
    ui.tableWidget_objetos.setItem(num_linhas, 1, QtWidgets.QTableWidgetItem(valor_y))
    ui.text_x.clear()
    ui.text_y.clear()