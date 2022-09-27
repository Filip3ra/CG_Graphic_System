import numpy as np

from modelos.ponto import Ponto

# Classe da window, onde salvo seus dados
class Window:
    def __init__(self, window) -> None:
        self.xwmin = window.xwmin
        self.ywmin = window.ywmin
        self.xwmax = window.xwmax
        self.ywmax = window.ywmax
        
    def __init__(self, xwmin: float, ywmin: float, xwmax: float, ywmax: float):
        self.xwmin = float(xwmin)
        self.ywmin = float(ywmin)
        self.xwmax = float(xwmax)
        self.ywmax = float(ywmax)
        self.p1 =  Ponto(self.xwmin, self.ywmin)
        self.p2 =  Ponto(self.xwmin, self.ywmax)
        self.p3 =  Ponto(self.xwmax, self.ywmax)
        self.p4 =  Ponto(self.xwmax, self.ywmin)
        self.Vup = [{'x': self.xwmin,
                     'y': self.ywmin},
                    {'x': self.xwmin,
                     'y': self.ywmax}]
        self.xwmin_original = float(xwmin)
        self.ywmin_original = float(ywmin)
        self.xwmax_original = float(xwmax)
        self.ywmax_original = float(ywmax)
        self.p1_original =  Ponto(self.xwmin_original, self.ywmin_original)
        self.p2_original =  Ponto(self.xwmin_original, self.ywmax_original)
        self.p3_original =  Ponto(self.xwmax_original, self.ywmax_original)
        self.p4_original =  Ponto(self.xwmax_original, self.ywmin_original)
    
    def centro_objeto(self):
        centro_x = (self.xwmin + self.xwmax)/2
        centro_y = (self.ywmin + self.ywmax)/2
        return centro_x, centro_y

    def Vup(self):
        self.Vup = [{'x': self.xwmin,
                     'y': self.ywmin},
                    {'x': self.xwmin,
                     'y': self.ywmax}]
        return self.Vup

    def aplica_transformacoes(self, transformacao):
        '''
        Aplica as transformações na window e atualiza os pontos mínimos e máximos da PPC
        '''
        self.p1.matriz = np.dot(transformacao.matriz, self.p1.matriz)
        self.p2.matriz = np.dot(transformacao.matriz, self.p2.matriz)
        self.p3.matriz = np.dot(transformacao.matriz, self.p3.matriz)
        self.p4.matriz = np.dot(transformacao.matriz, self.p4.matriz)

        # Atualiza valores mínimos e máximos
        self.xwmin = self.p1.x
        self.ywmin = self.p1.y
        self.xwmax = self.p3.x
        self.ywmax = self.p3.y
