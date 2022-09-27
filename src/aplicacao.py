from PyQt5 import QtCore, QtWidgets
from escritor_xml import gera_arquivo_saida

from graficos import browseFiles, att_opcao_selecionada, adiciona_objeto
from transformacoes import verifica_transformacoes

def controle(ui, tag: str):
    ui.list_transformacoes.addItem(tag)

def exporta_arquivo_xml(dados_saida: list):
    '''
    Salva o arquivo dos dados de saída no formato XML
    '''
    nome_arquivo_saida = '..\saida.xml'
    gera_arquivo_saida(dados_saida, nome_arquivo_saida)

def aplicacao(ui: QtWidgets.QDialog, scene):
    dados_entrada = []
    dados_saida = []

    # Ao butão button_open for clicado, chama a função browseFiles
    ui.button_open.clicked.connect(lambda: browseFiles(ui=ui,
                                                       dados_entrada= dados_entrada,
                                                       dados_saida= dados_saida,
                                                       scene = scene))

    # Ao pressionar o botão de adicionar um objeto, chama a função
    ui.button_atualizar.pressed.connect(lambda: att_opcao_selecionada(ui= ui))
    ui.button_adicionar.pressed.connect(lambda: adiciona_objeto())

    # Ao clicar nos butões das transformações geométricas
    # é chamada a função específica para aquele butão
    #ui.button_diminuir.clicked.connect(controle_diminuir)
    ui.button_diminuir.clicked.connect(lambda: controle(ui = ui, tag = 'Diminuir'))
    ui.button_ampliar.clicked.connect(lambda: controle(ui = ui, tag = 'Ampliar'))
    ui.button_girar_negativo.clicked.connect(lambda: controle(ui = ui, tag = 'Girar Negativamente'))
    ui.button_girar_positivo.clicked.connect(lambda: controle(ui = ui, tag = 'Girar Positivamente'))
    ui.button_cima.clicked.connect(lambda: controle(ui = ui, tag = 'Cima'))
    ui.button_baixo.clicked.connect(lambda: controle(ui = ui, tag = 'Baixo'))
    ui.button_esquerda.clicked.connect(lambda: controle(ui = ui, tag = 'Esquerda'))
    ui.button_direita.clicked.connect(lambda: controle(ui = ui, tag = 'Direita'))

    # Ao clicar em Aplicar, chama a função verifica_transformacoes
    ui.button_aplicar.clicked.connect(lambda: verifica_transformacoes(ui= ui,
                                                                      scene= scene,
                                                                      dados_entrada = dados_entrada,
                                                                      dados_saida= dados_saida))

    # Ao pressionar o botão será gerado o arquivo de saída
    ui.button_exportar.pressed.connect(lambda: exporta_arquivo_xml(dados_saida= dados_saida))
    
    # Fechando janela
    ui.button_close.clicked.connect(QtCore.QCoreApplication.instance().quit)