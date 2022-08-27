import os
import xml.etree.ElementTree as ET
from modelos.ponto2d import Ponto2D
from modelos.ponto3d import Ponto3D
from modelos.viewport import Viewport
from modelos.window import Window

PONTO = 'ponto'
LINHA = 'linha'
POLIGONO = 'poligono'

class LeitorEntradaXml:
    def __init__(self):
        # leitura do arquivo .xml em formato de árvore
        caminho = os.path.join(os.path.dirname(
            __file__), '..', 'entrada', 'entrada.xml')
        self.xml_raiz = ET.parse(caminho).getroot()
        self.getDadosEntrada()

    def getDadosViewport(self):
        xml = self.xml_raiz
        v_min_ponto = Ponto2D.cria_atributos_dicionario_do_xml(xml[0][0].attrib)
        v_max_ponto = Ponto2D.cria_atributos_dicionario_do_xml(xml[0][1].attrib)
        return Viewport(v_min_ponto, v_max_ponto)

    def getDadosWindow(self):
        xml = self.xml_root
        w_min_ponto = Ponto3D.create_from_xml_attrib_dict(xml[1][0].attrib)
        w_max_ponto = Ponto3D.create_from_xml_attrib_dict(xml[1][1].attrib)
        return Window(w_min_ponto, w_max_ponto)
        
        

    def getDadosEntrada(self):
        self.getDadosViewport()
        #viewport = self.getDadosViewport()

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