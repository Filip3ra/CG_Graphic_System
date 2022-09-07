# Classe da window, onde salvo seus dados
class Window:
    def __init__(self, xwmin: float, ywmin: float, xwmax: float, ywmax: float):
        self.xwmin = float(xwmin)
        self.ywmin = float(ywmin)
        self.xwmax = float(xwmax)
        self.ywmax = float(ywmax)
