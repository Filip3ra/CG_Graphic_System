from modelos.ponto import Ponto

# Classe da window, onde salvo seus dados
class Window:
    def __init__(self, xwmin: float, ywmin: float, xwmax: float, ywmax: float):
        self.xwmin = float(xwmin)
        self.ywmin = float(ywmin)
        self.xwmax = float(xwmax)
        self.ywmax = float(ywmax)
        self.p1 =  Ponto(self.xwmin, self.ywmin)
        self.p2 =  Ponto(self.xwmin, self.ywmax)
        self.p3 =  Ponto(self.xwmax, self.ywmax)
        self.p4 =  Ponto(self.xwmax, self.ywmin)
    
    def centro_objeto(self):
        centro_x = (self.xwmin + self.xwmax)/2
        centro_y = (self.ywmin + self.ywmax)/2
        return centro_x, centro_y
