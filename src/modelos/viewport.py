from PyQt5.QtGui import QPen, QColor

from modelos.ponto import Ponto

# Classe da viewport, onde salvo seus dados
class Viewport:
    def __init__(self, xvmin: float, yvmin: float, xvmax: float, yvmax: float):
        self.ponto_min = Ponto(float(xvmin), float(yvmin))
        self.ponto_max = Ponto(float(xvmax), float(yvmax))

    def atualiza_scene(self, scene):
        '''
        Atualiza a cena da viewport
        '''
        # Adicionando retângulo conforme o viewport passado
        scene.addRect(self.ponto_min.x,
                      self.ponto_min.y,
                      self.ponto_max.x,
                      self.ponto_max.y, 
                      QPen(QColor("black")))
        return scene

    def __str__(self) -> str:
        return f'Viewport: ({self.ponto_min.x}, {self.ponto_min.y}), ({self.ponto_max.x},{self.ponto_max.y})'

    def centro_objeto(self):
        centro_x = (self.ponto_min.x + self.ponto_max.x)/2
        centro_y = (self.ponto_min.y + self.ponto_max.y)/2
        return centro_x, centro_y

    def reset(self):
        self.ponto_min.reset()
        self.ponto_max.reset()

