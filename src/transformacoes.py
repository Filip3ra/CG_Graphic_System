import math
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QGraphicsScene

from graficos import atualiza_lista_objetos, exibe_na_viewport, realiza_transformacao_dados
from mapeadores.window_to_ppc import window_to_PPC
from mapeadores.window_to_viewport import TransformadaViewport
from modelos.objeto_geometrico import ObjetoGeometrico
from modelos.poligono import Poligono
from modelos.ponto import Ponto
from modelos.reta import Reta
from modelos.window import Window
from transformacoes_geometricas import TransformacaoGeometrica


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
            
def aplica_transformacoes_objetos(objeto_geometrico: ObjetoGeometrico, 
                                  transformacoes: TransformacaoGeometrica):
    '''
    Verifica qual objeto geometrico e aplica a transformação.
    '''
    if isinstance(objeto_geometrico, Ponto):
        objeto_geometrico.aplica_transformacoes(transformacoes)
    elif isinstance(objeto_geometrico, Reta):
        objeto_geometrico.aplica_transformacoes(transformacoes)
    elif isinstance(objeto_geometrico, Poligono):
        objeto_geometrico.aplica_transformacoes(transformacoes)
    else:
        raise TypeError("Tipo de objeto não encontrado!")

    return objeto_geometrico

def atualiza_matriz_transformacoes(ui: QDialog,
                                   objeto_geometrico: ObjetoGeometrico) -> TransformacaoGeometrica:
    '''
    Constroi a matriz de transformações.
    '''
    transformacoes = TransformacaoGeometrica()

    # Transladando o centro do objeto para posição (0,0)
    x_centro, y_centro = objeto_geometrico.centro_objeto()
    transformacoes.translacao(-x_centro, -y_centro)

    # Aplicando as transformações que estiverem na lista de transformações
    adiciona_lista_transformacoes(ui = ui,
                                  transformacoes= transformacoes)

    # Transladando o centro do objeto (0,0) para posição original
    transformacoes.translacao(x_centro, y_centro)

    return transformacoes

def constroi_matriz_transformacoes(ui: QDialog,
                                   objeto_geometrico: ObjetoGeometrico) -> TransformacaoGeometrica:
    '''
    Constroi a matriz de transformações.
    '''
    transformacoes = TransformacaoGeometrica()

    # Transladando o centro do objeto para posição (0,0)
    x_centro, y_centro = objeto_geometrico.centro_objeto()
    transformacoes.translacao(-x_centro, -y_centro)

    # Aplicando as transformações que estiverem na lista de transformações
    for index in range(ui.tableWidget.rowCount()):
        try:
            valor_x = int(ui.tableWidget.item(index, 1).text())
            valor_y = int(ui.tableWidget.item(index, 2).text())
            if str(ui.tableWidget.item(index, 0).text()) == 'Translação':
                transformacoes.translacao(valor_x, valor_y)
            elif str(ui.tableWidget.item(index, 0).text()) == 'Rotação':
                valor_x_rad = math.radians(valor_x)
                transformacoes.rotacao(valor_x_rad)
            elif str(ui.tableWidget.item(index, 0).text()) == 'Escala':
                transformacoes.escala(valor_x, valor_y)
        except:
            pass
    # Transladando o centro do objeto (0,0) para posição original
    transformacoes.translacao(x_centro, y_centro)

    return transformacoes

def verifica_transformacoes_objetos(ui: QDialog, 
                                    scene: QGraphicsScene, 
                                    dados_entrada: list,
                                    dados_saida: list):
    if len(dados_saida) < 1:
        # Não possui dados
        print('O arquivo XML inserido está incorreto ou não foi inserido o arquivo de entrada.')
        pass
    else:
        transformacoes = TransformacaoGeometrica()
        flag_checked_object = False
        for index in range(ui.list_objects.count()):
            # Verifica qual objeto está marcado na lista de objetos
            # Se tiver objeto marcado chama a função aplica_transformacoes
            if ui.list_objects.item(index).checkState() > 1:
                flag_checked_object = True
                transformacoes = constroi_matriz_transformacoes(ui= ui,
                                                                objeto_geometrico= dados_saida[index],)

                dados_saida[index] = aplica_transformacoes_objetos(objeto_geometrico= dados_saida[index],
                                                                   transformacoes= transformacoes)

        if not flag_checked_object:
            # TODO Exibir alerta
            print('Objeto Geométrico não selecionado!')

        atualiza_lista_objetos(ui= ui,
                               dados_saida= dados_saida)
        exibe_na_viewport(ui= ui,
                          scene= scene,
                          dados_entrada=dados_entrada,
                          dados_saida= dados_saida)

        # Limpa matriz de transformações
        transformacoes.limpar()

        # Limpa tabela de transformações
        ui.tableWidget.clear()  
        ui.tableWidget.setRowCount(0)  
        ui.tableWidget.setColumnCount(0)
        ## TODO Colocar nomes nas colunas

def atualiza_window(ui: QDialog,
                    scene: QGraphicsScene,
                    dados_entrada: list,
                    dados_saida: list,
                    tag_transformacao: str):
    try:
        dados_entrada[0]['window'].aplica_transformacoes(tag_transformacao)

        if tag_transformacao == 'Rotação':
            dados_entrada[0]['window'], transformacoes_aux = window_to_PPC(dados_entrada[0]['window'])

            for index in range(len(dados_saida)):
                try:
                    # Atualizo somente para ponto, reta e poligono, pois somente eles tem o método atualiza_valores_PPC
                    dados_saida[index].atualiza_valores_PPC(transformacoes_aux)   
                except:
                    pass 

        transformada = TransformadaViewport(dados_entrada[0]['window'],
                                            dados_entrada[0]['viewport'])

        dados_saida_xml = {
            'pontos': [],
            'retas': [],
            'poligonos': []
        }
        realiza_transformacao_dados(dados_entrada_dict= dados_entrada[0],
                                    dados_saida_xml= dados_saida_xml,
                                    dados_saida= dados_saida)

        atualiza_lista_objetos(ui= ui,
                               dados_saida= dados_saida)

        exibe_na_viewport(ui= ui,
                          scene= scene,
                          dados_entrada=dados_entrada,
                          dados_saida= dados_saida)
    except:
        print('Adicione um arquivo XML no programa!')