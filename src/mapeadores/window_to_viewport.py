
from modelos.reta import Reta
from modelos.ponto import Ponto
from modelos.poligono import Poligono
from modelos.viewport import Viewport
from modelos.window import Window


class TransformadaViewport:
    def __init__(self, window_param: Window, viewport_param: Viewport):
        self.window = window_param
        self.viewport = viewport_param

    def transformada_ponto(self, window_ponto: Ponto):
        # Window
        Xw_min = self.window.ponto_min.x
        Xw_max = self.window.ponto_max.x
        Yw_min = self.window.ponto_min.y
        Yw_max = self.window.ponto_max.y
        # Viewport
        Xv_min = self.viewport.ponto_min.x
        Xv_max = self.viewport.ponto_max.y
        Yv_min = self.viewport.ponto_min.y
        Yv_max = self.viewport.ponto_max.y

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
