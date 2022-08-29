import os
import xml.etree.ElementTree as ET
from modelos.reta import Reta
from modelos.ponto2d import Ponto2D_int, Ponto2D_float
from modelos.ponto3d import Ponto3D_float
from modelos.viewport import Viewport
from modelos.window import Window


class LeitorEntradaXml:
    def __init__(self, diretorio_arquivo):
        # leitura do arquivo .xml para interpretar como uma árvore

        #caminho = os.path.join(os.path.dirname(
        #    __file__), '..', 'entrada', 'entrada.xml')
        caminho = os.path.join(os.path.dirname(
            __file__), '../', diretorio_arquivo)
        self.xml_raiz = ET.parse(caminho).getroot()

    def getDadosEntradaCompletos(self):
        viewport = self.getDadosViewport()
        window = self.getDadosWindow()

        pontos = []
        retas = []

        for i in range(2, len(self.xml_raiz)):
            elemento = self.xml_raiz[i]

            if elemento.tag == 'ponto':
                ponto = self.getPonto(elemento)
                pontos.append(ponto)

            if elemento.tag == 'reta':
                reta = self.getReta(elemento)
                retas.append(reta)

        return { 
            'viewport': viewport,
            'window': window,
            'pontos': pontos,
            'retas': retas
        }

# ----- VIEWPORT E WINDOW ----- #

    def getDadosViewport(self):
        xml = self.xml_raiz
        v_min_ponto = Ponto2D_int.cria_atributos_dicionario_do_xml_int(
            xml[0][0].attrib)  # 10 X 10 margem
        v_max_ponto = Ponto2D_int.cria_atributos_dicionario_do_xml_int(
            xml[0][1].attrib)  # 620 X 470 dimensão
        return Viewport(v_min_ponto, v_max_ponto)

    def getDadosWindow(self):
        xml = self.xml_raiz
        w_min_ponto = Ponto2D_float.cria_atributos_dicionario_do_xml_float(
            xml[1][0].attrib)  # 0.0   0.0
        w_max_ponto = Ponto2D_float.cria_atributos_dicionario_do_xml_float(
            xml[1][1].attrib)  # 10.0  10.0
        return Window(w_min_ponto, w_max_ponto)

# ----- PONTOS, LINHAS E POLIGONOS ----- #

    def getPonto(self, ponto):
        param = ponto.attrib
        return Ponto2D_int.cria_atributos_dicionario_do_xml_int(param)

    def getReta(self, reta):
        param_1 = reta[0].attrib
        param_2 = reta[1].attrib
        p1 = Ponto2D_int.cria_atributos_dicionario_do_xml_int(param_1)
        p2 = Ponto2D_int.cria_atributos_dicionario_do_xml_int(param_2)
        return Reta(p1, p2)


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
