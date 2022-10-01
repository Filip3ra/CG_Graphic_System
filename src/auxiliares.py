
import os
import sys
from PyQt5 import uic

# converte o valor lido no meu dicionario de palavras para um valor numérico
def converte_valores_dicionario_para_numerico(dic, int_ou_float):
    if int_ou_float != 'int' and int_ou_float != 'float':
        raise ValueError('O parâmetro int_ou_float deve ser "int" ou "float".')

    # estou acessando a estrutura da minha árvore
    # dic.items() == [('x', '10'), ('y', '10')])  onde 'key' guarda o 'x' e 'value' guarda o '10', por exemplo.
    if int_ou_float == 'int':
        for key, value in dic.items():
            dic[key] = int(value)
    else:
        for key, value in dic.items():
            dic[key] = float(value)

    return dic

def indenta_xml(root, level = 0):
  i = '\n' + level * '  '
  if len(root):
    if not root.text or not root.text.strip():
      root.text = i + '  '
    if not root.tail or not root.tail.strip():
      root.tail = i
    for root in root:
      indenta_xml(root, level + 1)
    if not root.tail or not root.tail.strip():
      root.tail = i
  else:
    if level and (not root.tail or not root.tail.strip()):
      root.tail = i

'''
def addPonto(condicao):
    ui.label_ponto_1_x.setDisabled(True)
    ui.text_x_1.setDisabled(True)

    ui.label_ponto_2_x.setDisabled(condicao)
    ui.text_x_2.setDisabled(condicao)

    ui.label_ponto_2_y.setDisabled(condicao)
    ui.text_y_2.setDisabled(condicao)

    ui.label_ponto_3_x.setDisabled(condicao)
    ui.text_x_3.setDisabled(condicao)

    ui.label_ponto_3_y.setDisabled(condicao)
    ui.text_y_3.setDisabled(condicao)

    ui.button_add_ponto.setDisabled(condicao)

def addReta(condicao):
    ui.label_ponto_2_x.setDisabled(condicao)
    ui.text_x_2.setDisabled(condicao)
    ui.label_ponto_2_y.setDisabled(condicao)
    ui.text_y_2.setDisabled(condicao)
    ui.label_ponto_3_x.setDisabled(condicao)
    ui.text_x_3.setDisabled(condicao)
    ui.label_ponto_3_y.setDisabled(condicao)
    ui.text_y_3.setDisabled(condicao)
    ui.button_add_ponto.setDisabled(condicao)

    '''