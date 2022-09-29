import math
import numpy as np
import copy
from modelos.window import Window
from transformacoes_geometricas import TransformacaoGeometrica

def window_to_PPC(window: Window):
    window_ppc = copy.deepcopy(window)

    # 1 - Transladando o centro do objeto para posição (0,0)
    x_centro, y_centro = window_ppc.centro_objeto()
    window_ppc.aplica_translacao_x(-x_centro)
    window_ppc.aplica_translacao_y(-y_centro)

    ANGULO_DEFAULT = 10
    ## Rotaciona no sentido inverso
    angulo_para_rotacionar_mundo = - math.radians(ANGULO_DEFAULT)

    window_ppc.aplica_rotacao(angulo_para_rotacionar_mundo)

    transformacoes_aux = TransformacaoGeometrica()
    transformacoes_aux.translacao(-x_centro, -y_centro)
    transformacoes_aux.rotacao(angulo_para_rotacionar_mundo)
    return window_ppc, transformacoes_aux