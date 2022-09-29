import math
import numpy as np
from copy import copy
from modelos.window import Window
from transformacoes_geometricas import TransformacaoGeometrica

def window_to_PPC(window: Window):
    window_ppc = copy.deepcopy(window)

    # 1 - Transladando o centro do objeto para posição (0,0)
    x_centro, y_centro = window_ppc.centro_objeto()
    window_ppc.aplica_translacao_x(-x_centro)
    window_ppc.aplica_translacao_y(-y_centro)

    # 2 - Determina o ângulo de Vup com Y
    Vup = window_ppc.Vup
    print(f'Vup: {Vup}')

    angulo_para_rotacionar_mundo = 0
    if Vup[1]['x'] != Vup[0]['x']:     # Se for igual, Vup paralelo com Y
        m_Vup = (Vup[1]['y'] - Vup[0]['y']) / (Vup[1]['x'] - Vup[0]['x'])
        
        # 3 - Rotaciona para Vup ser paralelo com eixo Y
        # Alinha Vup com Y em radianos
        angulo_para_rotacionar_mundo = - math.radians(np.arctan(np.abs(1/m_Vup)))

        print(f'Angulo: {angulo_para_rotacionar_mundo:.2f}')
        window_ppc.aplica_rotacao(angulo_para_rotacionar_mundo)

    # 4 Aplica transformações na window e demais objetos
    transformacoes_aux = TransformacaoGeometrica()
    window_ppc.ponto_min.atualiza_valores_PPC(transformacoes_aux)
    window_ppc.ponto_max.atualiza_valores_PPC(transformacoes_aux)

    return window_ppc, transformacoes_aux