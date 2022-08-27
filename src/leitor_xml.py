import os
import xml.etree.ElementTree as ET
from modelos.ponto2d import Ponto2D_int
from modelos.ponto3d import Ponto2D_float
from modelos.viewport import Viewport
from modelos.window import Window


class LeitorEntradaXml:
    def __init__(self):
        # leitura do arquivo .xml para interpretar como uma árvore
        caminho = os.path.join(os.path.dirname(
            __file__), '..', 'entrada', 'entrada.xml')
        self.xml_raiz = ET.parse(caminho).getroot()

    def getDadosEntradaCompletos(self):
        viewport = self.getDadosViewport()
        window = self.getDadosWindow()

        pontos = []

        for i in range(2, len(self.xml_raiz)):
            elemento = self.xml_raiz[i]

            if elemento.tag == 'ponto':
                ponto = self.getPonto(elemento)
                pontos.append(ponto)

        return { 
            'viewport': viewport,
            'window': window,
            'pontos': pontos
        }

# ----- VIEWPORT E WINDOW ----- #

    def getDadosViewport(self):
        xml = self.xml_raiz
        v_min_ponto = Ponto2D_int.cria_atributos_dicionario_do_xml(
            xml[0][0].attrib)  # 10 X 10 margem
        v_max_ponto = Ponto2D_int.cria_atributos_dicionario_do_xml(
            xml[0][1].attrib)  # 620 X 470 dimensão
        return Viewport(v_min_ponto, v_max_ponto)

    def getDadosWindow(self):
        xml = self.xml_raiz
        w_min_ponto = Ponto2D_float.cria_atributos_dicionario_do_xml(
            xml[1][0].attrib)  # 0.0   0.0
        w_max_ponto = Ponto2D_float.cria_atributos_dicionario_do_xml(
            xml[1][1].attrib)  # 10.0  10.0
        return Window(w_min_ponto, w_max_ponto)

# ----- PONTOS, LINHAS E POLIGONOS ----- #

    def getPonto(self, ponto_individual):
        atributo = ponto_individual.attrib
        return Ponto2D_float.cria_atributos_dicionario_do_xml(atributo)


'''

ÁRVORE DA XML

xml_raiz = <dados>
    xml_raiz[0][0] == vpmin
    xml_raiz[0][1] == vpmax

        xml_raiz[0][0].atrib == {'x': 10, 'y': 10}
        xml_raiz[0][1].atrib == {'x': '630', 'y': '470'}

            xml_raiz[0][1].atrib.items() == dict_items([('x', '10'), ('y', '10')])
            ...

'''
