
from modelos.reta import Reta
from modelos.ponto import Ponto
from modelos.poligono import Poligono


class Transformacao:
    def __init__(self, window_param, viewport_param):
        self.window = window_param
        self.viewport = viewport_param

    def transformada_ponto(self, window_ponto):
        # Window
        Xw_min = self.window.xwmin
        Xw_max = self.window.xwmax
        Yw_min = self.window.ywmin
        Yw_max = self.window.ywmax
        # Viewport
        Xv_min = self.viewport.xvmin
        Xv_max = self.viewport.xvmax
        Yv_min = self.viewport.yvmin
        Yv_max = self.viewport.yvmax

        # As duas equações de transformação são:
        # Xvp = ( (Xw - Xw_min) / Xw_max - Xw_min ) * (Xvp_max - Xvp_min)
        x_vp = (window_ponto.x - Xw_min) / \
            (Xw_max - Xw_min) * (Xv_max - Xv_min)

        # Yvp = (1 - (Yw - Yw_min) / (Yw_max - Yw_min)) * (Yvp_max - Yvp_min)
        y_vp = (1 - ((window_ponto.y - Yw_min) /
                (Yw_max - Yw_min))) * (Yv_max - Yv_min)

        return Ponto(x_vp, y_vp)

    # para transformar a reta e o polígono basta transformar seus pontos
    def transformada_reta(self, window_reta: Reta):
        p1 = self.transformada_ponto(window_reta.p1)
        p2 = self.transformada_ponto(window_reta.p2)
        return Reta(p1, p2)

    def transformada_poligono(self, window_poligono: Poligono):
        pontos = []
        for ponto in window_poligono.lista_pontos:
            pontos.append(self.transformada_ponto(ponto))

        return Poligono(pontos)
