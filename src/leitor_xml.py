import os
import xml.etree.ElementTree as ET
from modelos.reta import Reta
from modelos.ponto import Ponto
from modelos.poligono import Poligono
from modelos.viewport import Viewport
from modelos.window import Window


class LeitorEntradaXml:
    # Leitura do arquivo .xml para interpretar como uma árvore
    def __init__(self, diretorio_arquivo):
        caminho = os.path.join(os.path.dirname(
            __file__), '../', diretorio_arquivo)
        self.xml_raiz = ET.parse(caminho).getroot()

    # Realizo todas as chamadas de funções necessárias para obter todos os dados de entrada
    def getDadosEntradaCompletos(self):
        viewport = self.getDadosViewport()
        window = self.getDadosWindow()

        # Obtenho os dados dos pontos, retas e poligonos
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

        # organizo o retorno com todos os dados necessários
        return {
            'viewport': viewport,
            'window': window,
            'pontos': pontos,
            'retas': retas,
            'poligonos': poligonos
        }

# O arquivo .xml de entrada está sendo interpretado como uma árvore,
# portanto, através da raiz eu acesso os nós da árvore, que constituem
# as informações da vvieport, window, pontos, retas e poligono.

# ----- VIEWPORT E WINDOW ----- #

    def getDadosViewport(self):
        xml = self.xml_raiz

        xvmin = xml[0][0].attrib['x']
        xvmax = xml[0][1].attrib['x']

        yvmin = xml[0][0].attrib['y']
        yvmax = xml[0][1].attrib['y']

        return Viewport(xvmin=xvmin, yvmin=yvmin, xvmax=xvmax, yvmax=yvmax)

    def getDadosWindow(self):
        xml = self.xml_raiz

        xwmin = xml[1][0].attrib['x']
        xwmax = xml[1][1].attrib['x']

        ywmin = xml[1][0].attrib['y']
        ywmax = xml[1][1].attrib['y']

        return Window(xwmin=xwmin, ywmin=ywmin, xwmax=xwmax, ywmax=ywmax)

# ----- PONTOS, LINHAS E POLIGONOS ----- #

    def getPonto(self, ponto):
        param = ponto.attrib
        return Ponto.cria_atributos_dicionario_do_xml_int(param)

    def getReta(self, reta):
        param_1 = reta[0].attrib
        param_2 = reta[1].attrib
        p1 = Ponto.cria_atributos_dicionario_do_xml_int(param_1)
        p2 = Ponto.cria_atributos_dicionario_do_xml_int(param_2)
        return Reta(p1, p2)

    def getPoligono(self, poligono):
        pontos = []
        for i in range(len(poligono)):
            param = poligono[i].attrib
            pontos.append(
                Ponto.cria_atributos_dicionario_do_xml_int(param))
        return Poligono(pontos)
