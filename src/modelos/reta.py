import numpy as np
from auxiliares import PontoIntersecao, VizObjViewport, encontra_rks
from modelos.ponto import Ponto

from transformacoes_geometricas import TransformacaoGeometrica
from modelos.objeto_geometrico import ObjetoGeometrico

class Reta(ObjetoGeometrico):
    '''
    Classe para representar o objeto geométrico Reta.

    Obs: Os pontos p1 e p2 são os pontos de início e fim de uma reta.
    '''
    def __init__(self, p1: Ponto, p2: Ponto):
        if p1 == p2:
            raise ValueError(
                'Erro: Pontos iguais, p1 e p2 devem ser diferentes')
        else:
            self.p1 = p1
            self.p2 = p2
            self.exibe_obj_viewport = VizObjViewport.DENTRO

    def __str__(self) -> str:
        return f'Reta: {self.p1} {self.p2}'

    def centro_objeto(self):
        centro_x = (self.p1.x + self.p2.x)/2
        centro_y = (self.p1.y + self.p2.y)/2
        return centro_x, centro_y

    def aplica_transformacoes(self, transformacoes: TransformacaoGeometrica):
        self.p1.aplica_transformacoes(transformacoes)
        self.p2.aplica_transformacoes(transformacoes)

    def atualiza_valores_PPC(self, transformacao: TransformacaoGeometrica):
        self.p1.atualiza_valores_PPC(transformacao)
        self.p1.atualiza_valores_PPC(transformacao)

    def aplica_transformada(self, window, viewport):
        self.p1.aplica_transformada(window, viewport)
        self.p2.aplica_transformada(window, viewport)
    
    def clipping_liang_barsky(self, 
                              dados_entrada: dict):
        '''
        Algoritmo de clipping de retas de Liang-Barsky.
        '''
        ## Lista dos pontos de interseção entre a reta e viewport
        pontos_intersecao = []

        p1 = - (self.p2.x - self.p1.x)
        p2 = self.p2.x - self.p1.x
        p3 = - (self.p2.y - self.p1.y)
        p4 = self.p2.y - self.p1.y

        q1 = self.p1.x - dados_entrada["viewport"].ponto_min.x
        q2 = dados_entrada["viewport"].ponto_max.x - self.p1.x
        q3 = self.p1.y - dados_entrada["viewport"].ponto_min.y
        q4 = dados_entrada["viewport"].ponto_max.y - self.p1.y

        rx_max,rx_min,ry_max,ry_min = encontra_rks(p1,p2,p3,p4,q1,q2,q3,q4)

        u1 = max(0, rx_max, ry_max) ## Fora p/ dentro
        u2 = min(1, rx_min, ry_min) ## Dentro p/ fora

        if u1 <= u2:
            ## (u1 > u2) Reta completamente fora
            ## Substituindo na reta p/ encontrar pontos de interseção
            if u1 > 0:
                ponto_aux = Ponto(self.p1.x + u1*p2,
                                  self.p1.y + u1*p4)
                self.p1.x = ponto_aux.x
                self.p1.y = ponto_aux.y
                self.p2.flag_ponto_inter = PontoIntersecao.ENTRANDO

            if u2 < 1:
                ponto_aux = Ponto(self.p1.x + u2*p2,
                                  self.p1.y + u2*p4)
                self.p2.x = ponto_aux.x
                self.p2.y = ponto_aux.y
                self.p2.flag_ponto_inter = PontoIntersecao.SAINDO

            self.exibe_obj_viewport = VizObjViewport.PARCIAL
        elif u1 > u2:
            self.exibe_obj_viewport = VizObjViewport.FORA

    def reset(self):
        self.p1.reset()
        self.p2.reset()