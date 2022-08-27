import os
import xml.etree.ElementTree as ET

PONTO = 'ponto'
LINHA = 'linha'
POLIGONO = 'poligono'

class LeitorEntradaXml:
    def __init__(self):
        # leitura do arquivo .xml em formato de árvore
        caminho = os.path.join(os.path.dirname(
            __file__), '..', 'entrada', 'entrada.xml')
        self.xml_raiz = ET.parse(caminho).getroot()

    def getDadosEntrada(self):
        viewport = self.getDadosViewport()

    def getDadosViewport(self):
        xml = self.xml_raiz
        v_min_ponto = 