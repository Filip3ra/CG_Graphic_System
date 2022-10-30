
import os
import sys
from PyQt5 import uic

from enum import Enum

class VizObjViewport(Enum):
    DENTRO = 1
    FORA = 2
    PARCIAL = 3
    
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

def encontra_rks(p1,p2,p3,p4,q1,q2,q3,q4):
  '''
  Algoritmo auxiliar para encontrar os rk's do método de Liang-Barsky.
  '''
  if p1 < 0:
    rx_max = q1/p1
    rx_min = q2/p2
  else: 
    rx_max = q2/p2
    rx_min = q1/p1

  if p3 < 0:
    ry_max = q3/p3
    ry_min = q4/p4
  else: 
    ry_max = q4/p4
    ry_min = q3/p3

  return rx_max,rx_min,ry_max,ry_min  

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