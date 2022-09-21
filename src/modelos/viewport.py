from PyQt5.QtGui import QPen, QColor

from modelos.ponto import Ponto

# Classe da viewport, onde salvo seus dados
class Viewport:
    def __init__(self, xvmin: float, yvmin: float, xvmax: float, yvmax: float):
        self.xvmin = float(xvmin)
        self.yvmin = float(yvmin)
        self.xvmax = float(xvmax)
        self.yvmax = float(yvmax)
        self.p1 =  Ponto(self.xvmin, self.yvmin)
        self.p2 =  Ponto(self.xvmin, self.yvmax)
        self.p3 =  Ponto(self.xvmax, self.yvmax)
        self.p4 =  Ponto(self.xvmax, self.yvmin)

    def atualiza_scene(self, scene):
        '''
        Atualiza a cena da viewport
        '''
        # Adicionando retângulo conforme o viewport passado
        scene.addRect(self.xvmin,
                      self.yvmin,
                      self.xvmax,
                      self.yvmax, 
                      QPen(QColor("black")))
        return scene

    def centro_objeto(self):
        centro_x = (self.xvmin + self.xvmax)/2
        centro_y = (self.yvmin + self.yvmax)/2
        return centro_x, centro_y

