from PyQt5 import QtCore, QtWidgets
from escritor_xml import gera_arquivo_saida

from graficos import browseFiles, att_opcao_selecionada, adiciona_objeto, reset_window
from transformacoes import adiciona_lista_transformacoes, atualiza_window, verifica_transformacoes_objetos
from transformacoes_geometricas import TransformacaoGeometrica


def exporta_arquivo_xml(dados_saida: list):
    '''
    Salva o arquivo dos dados de saída no formato XML
    '''
    nome_arquivo_saida = 'saida.xml'
    gera_arquivo_saida()


def aplicacao(ui: QtWidgets.QDialog, scene):
    dados_entrada = []
    dados_saida = []
    dados_saida_xml = {
        'pontos': [],
        'retas': [],
        'poligonos': []
    }

    # Ao butão button_open for clicado, chama a função browseFiles
    ui.button_open.clicked.connect(lambda: browseFiles(ui=ui,
                                                       dados_entrada=dados_entrada,
                                                       dados_saida=dados_saida,
                                                       dados_saida_xml=dados_saida_xml,
                                                       scene=scene))

    # Ao pressionar o botão de adicionar um objeto, chama a função
    ui.button_atualizar.pressed.connect(lambda: att_opcao_selecionada(ui=ui))
    ui.button_adicionar.pressed.connect(lambda: adiciona_objeto(ui=ui,
                                                                scene=scene,
                                                                dados_entrada=dados_entrada,
                                                                dados_saida=dados_saida,))

    # Ao clicar nos butões das transformações geométricas
    # é chamada a função específica para aquele butão
    ui.button_diminuir.clicked.connect(lambda: atualiza_window(ui=ui,
                                                               scene=scene,
                                                               dados_entrada=dados_entrada,
                                                               dados_saida=dados_saida,
                                                               tag_transformacao='Diminuir'))
    ui.button_ampliar.clicked.connect(lambda: atualiza_window(ui=ui,
                                                              scene=scene,
                                                              dados_entrada=dados_entrada,
                                                              dados_saida=dados_saida,
                                                              tag_transformacao='Ampliar'))
    ui.button_girar_negativo.clicked.connect(lambda: atualiza_window(ui=ui,
                                                                     scene=scene,
                                                                     dados_entrada=dados_entrada,
                                                                     dados_saida=dados_saida,
                                                                     tag_transformacao='Girar Negativamente'))
    ui.button_girar_positivo.clicked.connect(lambda: atualiza_window(ui=ui,
                                                                     scene=scene,
                                                                     dados_entrada=dados_entrada,
                                                                     dados_saida=dados_saida,
                                                                     tag_transformacao='Girar Positivamente'))
    ui.button_cima.clicked.connect(lambda: atualiza_window(ui=ui,
                                                           scene=scene,
                                                           dados_entrada=dados_entrada,
                                                           dados_saida=dados_saida,
                                                           tag_transformacao='Cima'))
    ui.button_baixo.clicked.connect(lambda: atualiza_window(ui=ui,
                                                            scene=scene,
                                                            dados_entrada=dados_entrada,
                                                            dados_saida=dados_saida,
                                                            tag_transformacao='Baixo'))
    ui.button_esquerda.clicked.connect(lambda: atualiza_window(ui=ui,
                                                               scene=scene,
                                                               dados_entrada=dados_entrada,
                                                               dados_saida=dados_saida,
                                                               tag_transformacao='Esquerda'))
    ui.button_direita.clicked.connect(lambda: atualiza_window(ui=ui,
                                                              scene=scene,
                                                              dados_entrada=dados_entrada,
                                                              dados_saida=dados_saida,
                                                              tag_transformacao='Direita'))

    ui.button_reset.clicked.connect(lambda: reset_window(ui=ui,
                                                         scene=scene,
                                                         dados_entrada=dados_entrada,
                                                         dados_saida=dados_saida))

    ui.button_add_controle.clicked.connect(
        lambda: adiciona_lista_transformacoes(ui=ui))

    # Ao clicar em Aplicar, chama a função verifica_transformacoes
    ui.button_aplicar.clicked.connect(lambda: verifica_transformacoes_objetos(ui=ui,
                                                                              scene=scene,
                                                                              dados_entrada=dados_entrada,
                                                                              dados_saida=dados_saida))

    # Ao pressionar o botão será gerado o arquivo de saída
    ui.button_exportar.pressed.connect(
        lambda: exporta_arquivo_xml(dados_saida))

    # Fechando janela
    ui.button_close.clicked.connect(QtCore.QCoreApplication.instance().quit)
