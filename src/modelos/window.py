import numpy as np

from modelos.ponto import Ponto

class Window:       
    def __init__(self, xwmin: float, ywmin: float, xwmax: float, ywmax: float):
        self.ponto_min = Ponto(float(xwmin), float(ywmin))
        self.ponto_max = Ponto(float(xwmax), float(ywmax))
        self.ponto_min_original = Ponto(float(xwmin), float(ywmin))
        self.ponto_max_original = Ponto(float(xwmax), float(ywmax))
    
    def __str__(self) -> str:
        return f'Window: ({self.ponto_min.x}, {self.ponto_min.y}), ({self.ponto_max.x},{self.ponto_max.y})'

    def centro_objeto(self):
        centro_x = (self.ponto_min.x + self.ponto_max.x)/2
        centro_y = (self.ponto_min.y + self.ponto_max.y)/2
        return centro_x, centro_y

    def Vup(self):
        return [{'x': self.ponto_min.x,
                 'y': self.ponto_min.y},
                {'x': self.ponto_min.x,
                 'y': self.ponto_max.y}]

    def aplica_transformacoes(self, tag_transformacao):
        '''
        Aplica as transformações na window e atualiza os pontos mínimos e máximos da PPC
        '''
        ZOOM_DEFAULT = 0.1
        TRANSLACAO_DEFAULT = 1
        ANGULO_DEFAULT = 0.1745     # 10° = 0.1745 rad

        if tag_transformacao == 'Ampliar':
            self.aplica_zoom(ZOOM_DEFAULT)
        elif tag_transformacao == 'Diminuir':
            self.aplica_zoom(-ZOOM_DEFAULT)
        elif tag_transformacao == 'Cima':
            self.aplica_translacao_y(TRANSLACAO_DEFAULT)
        elif tag_transformacao == 'Baixo':
            self.aplica_translacao_y(-TRANSLACAO_DEFAULT)
        elif tag_transformacao == 'Esquerda':
            self.aplica_translacao_x(-TRANSLACAO_DEFAULT)
        elif tag_transformacao == 'Direita':
            self.aplica_translacao_x(TRANSLACAO_DEFAULT)
        elif tag_transformacao == 'Girar Negativamente':
            self.aplica_rotacao(- ANGULO_DEFAULT)
        elif tag_transformacao == 'Girar Positivamente':
            self.aplica_rotacao(ANGULO_DEFAULT)


    def aplica_zoom(self, zoom):
        self.ponto_max.x -= self.ponto_max.x * zoom
        self.ponto_max.y -= self.ponto_max.y * zoom

    def aplica_translacao_x(self, translacao):
        self.ponto_min.x = self.ponto_min.x + translacao
        self.ponto_max.x = self.ponto_max.x + translacao

    def aplica_translacao_y(self, translacao):
        self.ponto_min.y = self.ponto_min.y + translacao
        self.ponto_max.y = self.ponto_max.y + translacao

    def aplica_rotacao(self, angulo_rad):
        self.ponto_min.x = self.ponto_min.x * np.cos(angulo_rad) - self.ponto_min.y * np.sin(angulo_rad)
        self.ponto_min.y = self.ponto_min.x * np.sin(angulo_rad) + self.ponto_min.y * np.cos(angulo_rad)

        self.ponto_max.x = self.ponto_max.x * np.cos(angulo_rad) - self.ponto_min.y * np.sin(angulo_rad)
        self.ponto_max.y = self.ponto_max.x * np.sin(angulo_rad) + self.ponto_min.y * np.cos(angulo_rad)

