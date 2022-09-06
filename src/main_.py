import os
import sys
from PyQt5 import uic,QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog,QFileDialog,QListWidgetItem
from leitor_xml import LeitorEntradaXml
from transformacao import Transformacao

def browseFiles():
    arquivo_xml = QFileDialog.getOpenFileName(QDialog(), "Open File","\\")
    print(f'Carregou {arquivo_xml}')

    ## Realizando parse de xml para uma lista de palavras
    dados_entrada = LeitorEntradaXml(arquivo_xml[0]).getDadosEntradaCompletos()

    # executo transformação em cima dos dados lidos
    transformacao = Transformacao(dados_entrada['window'], dados_entrada['viewport'])

    dados_saida = {
        'pontos': [],
        'retas': [],
        'poligonos': []
    }

    for w_ponto in dados_entrada['pontos']:
        v_ponto = transformacao.transformada_ponto(w_ponto)
        dados_saida['pontos'].append(v_ponto)

    for w_reta in dados_entrada['retas']:
        v_reta = transformacao.transformada_reta(w_reta)
        dados_saida['retas'].append(v_reta)

    for w_poligono in dados_entrada['poligonos']:
        v_poligono = transformacao.transformada_poligono(w_poligono)
        dados_saida['poligonos'].append(v_poligono)            

    ## Adiciona cada objeto na lista
    for objeto in dados_saida:
        for dados_objeto in dados_saida[objeto]:
            ui.list_objects.addItem(dados_objeto.__str__())

    atualiza_objeto()

    exibe_na_viewport()
    return dados_saida

def atualiza_objeto():
    '''
    Atualizando objeto para ficar com o checkbox
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
    for index in range(ui.list_objects.count()):
        if ui.list_objects.item(index).checkState() == QtCore.Qt.Checked:
            print(ui.list_objects.item(index).text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sistema-grafico.ui"))
    ui.show()

    # Procurando arquivo no diretorio
    dados_saida = ui.button_open.clicked.connect(browseFiles)

    ui.list_objects.pressed.connect(exibe_na_viewport)

    ## Fechando janela
    ui.button_close.clicked.connect(Dialog.close)

    sys.exit(app.exec_())