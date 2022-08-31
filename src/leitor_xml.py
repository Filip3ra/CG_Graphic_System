import os
import xml.etree.ElementTree as ET
from modelos.reta import Reta
from modelos.ponto2d import Ponto2D_int, Ponto2D_float
from modelos.ponto3d import Ponto3D_float
from modelos.poligono import Poligono
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
        poligonos = []

        for i in range(2, len(self.xml_raiz)):
            elemento = self.xml_raiz[i]

            if elemento.tag == 'ponto':
                ponto = self.getPonto(elemento)
                pontos.append(ponto)

            if elemento.tag == 'reta':
                reta = self.getReta(elemento)
                retas.append(reta)
            
            if elemento.tag == 'poligono':
                poligono = self.getPoligono(elemento)
                poligonos.append(poligono)

        return { 
            'viewport': viewport,
            'window': window,
            'pontos': pontos,
            'retas': retas,
            'poligonos': poligonos
        }

# ----- VIEWPORT E WINDOW ----- #

    def getDadosViewport(self):
        xml = self.xml_raiz
        '''
        v_min_ponto = Ponto2D_int.cria_atributos_dicionario_do_xml_int(
            xml[0][0].attrib)  # 10 X 10 margem
        v_max_ponto = Ponto2D_int.cria_atributos_dicionario_do_xml_int(
            xml[0][1].attrib)  # 620 X 470 dimensão
        '''
        xvmin = xml[0][0].attrib['x']
        xvmax = xml[0][1].attrib['x']

        yvmin = xml[0][0].attrib['y']
        yvmax = xml[0][1].attrib['y']

        return Viewport(xvmin = xvmin, yvmin = yvmin, xvmax = xvmax, yvmax = yvmax)

    def getDadosWindow(self):
        xml = self.xml_raiz
        '''
        w_min_ponto = Ponto2D_float.cria_atributos_dicionario_do_xml_float(
            xml[1][0].attrib)  # 0.0   0.0
        w_max_ponto = Ponto2D_float.cria_atributos_dicionario_do_xml_float(
            xml[1][1].attrib)  # 10.0  10.0
        '''
        xwmin = xml[1][0].attrib['x']
        xwmax = xml[1][1].attrib['x']

        ywmin = xml[1][0].attrib['y']
        ywmax = xml[1][1].attrib['y']

        return Window(xwmin = xwmin, ywmin = ywmin, xwmax = xwmax, ywmax = ywmax)

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

    def getPoligono(self, poligono):
        pontos = []
        for i in range(len(poligono)):
            param = poligono[i].attrib
            pontos.append(Ponto2D_int.cria_atributos_dicionario_do_xml_int(param))
        return Poligono(pontos)


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
