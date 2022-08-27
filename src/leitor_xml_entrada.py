import os
import xml.etree.ElementTree as ET


class LeitorEntradaXml:
    def __init__(self):
        # leitura do arquivo .xml em formato de árvore
        caminho = os.path.join(os.path.dirname(
            __file__), '..', 'entrada', 'entrada.xml')
        self.xml_root = ET.parse(caminho).getroot()

    
