
from modelos.ponto2d import Ponto2D_int


class Transformacao:
    def __init__(self, window_param, viewport_param):
        self.window = window_param
        self.viewport = viewport_param

    def transformada_ponto(self, window_ponto):
        w_min = self.window.min_ponto
        w_max = self.window.max_ponto
        v_min = self.viewport.min_ponto
        v_max = self.viewport.max_ponto

        # Xvp = ( (Xw - Xw_min) / Xw_max - Xw_min ) * (Xvp_max - Xvp_min)
        x_vp = (window_ponto.x - w_min.x) / \
            (w_max.x - w_min.x) * (v_max.x - v_min.x)

        # colocar segunda equação
        y_vp = (1 - ((window_ponto.y - w_min.y) /
                (w_max.y - w_min.y))) * (v_max.y - v_min.y)

        return Ponto2D_int(x_vp, y_vp)
