import numpy as np
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
            self.p1_original = p1
            self.p2_original = p2

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