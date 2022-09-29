import numpy as np
from PyQt5.QtWidgets import QDialog, QGraphicsScene

from graficos import atualiza_lista_objetos, exibe_na_viewport
from mapeadores.window_to_ppc import WindowToPPC, window_to_PPC
from mapeadores.window_to_viewport import TransformadaViewport
from modelos.objeto_geometrico import ObjetoGeometrico
from modelos.poligono import Poligono
from modelos.ponto import Ponto
from modelos.reta import Reta
from modelos.window import Window
from transformacoes_geometricas import TransformacaoGeometrica


def adiciona_lista_transformacoes(ui: QDialog, 
                                  transformacoes: TransformacaoGeometrica):
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
        elif item_lista_transformacoes == 'Girar Negativamente':
            # Rotacionando -10° = -0.1745 rad
            transformacoes.rotacao(-0.1745)
        elif item_lista_transformacoes == 'Girar Positivamente':
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
    adiciona_lista_transformacoes(ui = ui,
                                  transformacoes= transformacoes)

    # Transladando o centro do objeto (0,0) para posição original
    transformacoes.translacao(x_centro, y_centro)

    return transformacoes


def verifica_transformacoes(ui: QDialog, 
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
        # Verifica se a transformação será realizada com os objetos ou com a viewport

        if ui.radioButton_objetos.isChecked():
            for index in range(ui.list_objects.count()):
                # Verifica qual objeto está marcado na lista de objetos
                # Se tiver objeto marcado chama a função aplica_transformacoes
                # QtCore.Qt.Checked
                if ui.list_objects.item(index).checkState() > 1:
                    if flag_checked_object:
                        # Não precisa construir a matriz de transformações, pois já foi construída.
                        dados_saida[index] = aplica_transformacoes_objetos(objeto_geometrico= dados_saida[index],
                                                                           transformacoes= transformacoes)
                    else:
                        
                        # Se não tiver encontrado nenhum objeto marcado ainda,
                        # precisa construir a matriz de transformações,
                        # depois aplica as transformações nos objetos marcados
                        transformacoes = constroi_matriz_transformacoes(ui= ui,
                                                                        objeto_geometrico= dados_saida[index],)

                        dados_saida[index] = aplica_transformacoes_objetos(objeto_geometrico= dados_saida[index],
                                                                           transformacoes= transformacoes)

                        flag_checked_object = True

            if not flag_checked_object:
                # TODO Exibir alerta
                print('Objeto Geométrico não selecionado!')
        elif ui.radioButton_window.isChecked():
            ui.button_reset.setDisabled(True)
            for index in range(ui.list_transformacoes.count()):
                # Verifica qual objeto está marcado na lista de objetos
                tag_transformacao = ui.list_transformacoes.item(index).text()
            
                dados_entrada[0]['window'].aplica_transformacoes(tag_transformacao)
                dados_entrada[0]['window'], transformacoes_aux = window_to_PPC(dados_entrada[0]['window'])

                for index in range(len(dados_saida)):
                    try:
                        # Atualizo somente para ponto, reta e poligono, pois somente eles tem o método atualiza_valores_PPC
                        dados_saida[index].atualiza_valores_PPC(transformacoes_aux)   
                    except:
                        pass 

                # Window -> viewport
                transformada = TransformadaViewport(dados_entrada[0]['window'],
                                                    dados_entrada[0]['viewport'])
                                                    
                for index in range(len(dados_saida)):
                    if isinstance(dados_saida[index], Ponto):
                        dados_saida[index] = transformada.transformada_ponto(dados_saida[index])
                    elif isinstance(dados_saida[index], Reta):
                        dados_saida[index] = transformada.transformada_reta(dados_saida[index])
                    elif isinstance(dados_saida[index], Poligono):
                        dados_saida[index] = transformada.transformada_poligono(dados_saida[index])

        atualiza_lista_objetos(ui= ui,
                               dados_saida= dados_saida)
        exibe_na_viewport(ui= ui,
                          scene= scene,
                          dados_entrada=dados_entrada,
                          dados_saida= dados_saida)

        # Limpa matriz de transformações
        transformacoes.limpar()

        # Limpa lista de transformações
        ui.list_transformacoes.clear()

