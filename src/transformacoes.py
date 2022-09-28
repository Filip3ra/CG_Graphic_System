import numpy as np
from PyQt5.QtWidgets import QDialog, QGraphicsScene

from graficos import atualiza_lista_objetos, exibe_na_viewport
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
                                   objeto_geometrico: ObjetoGeometrico):
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
                    print(f'Inicio: {dados_saida[index]}')
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
                        print(f'transformacoes: {transformacoes.matriz}')
                        dados_saida[index] = aplica_transformacoes_objetos(objeto_geometrico= dados_saida[index],
                                                                           transformacoes= transformacoes)
                        print(f'Transformado: {dados_saida[index]}')
                        flag_checked_object = True

            if not flag_checked_object:
                # TODO Exibir alerta
                print('Objeto Geométrico não selecionado!')
        elif ui.radioButton_window.isChecked():
            ui.button_reset.setDisabled(True)
            # Procura o index da window na lista de dados_saida
            index = None
            for index_aux in range(len(dados_saida)):
                if isinstance(dados_saida[index_aux], Window):
                    index = index_aux
            if index is not None:
                # 0 - Movendo window conforme escolha do usuário
                constroi_matriz_transformacoes(index= index,
                                               transformacoes=transformacoes,
                                               dados_saida=dados_saida)
                
                dados_saida[index].aplica_transformacoes(transformacoes)

                # 1 - Transladando o centro do objeto para posição (0,0)
                x_centro, y_centro = dados_saida[index].centro_objeto()
                transformacoes_aux = TransformacaoGeometrica()
                transformacoes_aux.translacao(-x_centro, -y_centro)

                # 2 - Determina o ângulo de Vup com Y
                Vup = dados_saida[index].Vup()

                # 3 - Rotaciona para Vup ser paralelo com eixo Y
                angulo_para_rotacionar_mundo = None
                if Vup[1]['x'] != Vup[0]['x']:              # Se for igual, Vup paralelo com Y
                    m_Vup = (Vup[1]['y'] - Vup[0]['y']) / (Vup[1]['x'] - Vup[0]['x'])
                    
                # Alinha Vup com Y em radianos
                GRAU_TO_RAD = 0.0174533
                angulo_para_rotacionar_mundo = - np.arctan(np.abs(1/m_Vup)) * GRAU_TO_RAD

                transformacoes_aux.rotacao()
                
                # 4 - Armazene as coordenadas PPC de cada objeto e o mundo
                if angulo_para_rotacionar_mundo is not None:
                    for objeto, index in zip(dados_saida, range(len(dados_saida))):
                        try:
                            # Atualizo somente para ponto, reta e poligono, pois somente eles tem o método atualiza_valores_PPC
                            objeto.atualiza_valores_PPC(transformacoes_aux,
                                                        angulo_para_rotacionar_mundo)   
                        except:
                            pass 
                
                ## Aplicando a rotação também para a window
                dados_saida[index].aplica_transformacoes_PPC(transformacoes_aux)
            else:
                print('Não foi encontrado o objeto window! Verifique se foi inserido o arquivo de entrada e se ele está correto.')       
        # Limpa lista de objetos e carrega os objetos atualizados
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

