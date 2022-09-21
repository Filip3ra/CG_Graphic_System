import numpy as np
from modelos.poligono import Poligono

from modelos.ponto import Ponto
from modelos.reta import Reta

class TransformacaoGeometrica:
    def __init__(self) -> None:
        self.matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        
    def translacao(self, posicao_x, posicao_y):
        '''
        Função que multiplica a matriz de translação pela matriz atual.
        '''
        matriz_translacao = [[1, 0, posicao_x], [0, 1, posicao_y], [0, 0, 1]]
        self.matriz = np.dot(matriz_translacao, self.matriz)

    def rotacao(self, angulo_rad):
        '''
        Função que multiplica a matriz de translação pela matriz atual.
        '''
        matriz_rotacao = [[np.cos(angulo_rad), -np.sin(angulo_rad), 0], 
                             [np.sin(angulo_rad), np.cos(angulo_rad), 0],
                             [0, 0, 1]]
        self.matriz = np.dot(matriz_rotacao, self.matriz)

    def escala(self, Sx, Sy):
        matriz_escala = [[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]]
        self.matriz = np.dot(matriz_escala, self.matriz)

    def limpar(self):
        self.matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def aplica_transformacoes_ponto(self, objeto_geometrico: Ponto):
        matriz_aux_p1 = np.dot(self.matriz, objeto_geometrico.matriz)

        # Cria um objeto geométrico auxiliar para retornar as novas
        # coordenadas do ponto
        objeto_geometrico_aux = Ponto(matriz_aux_p1[0], matriz_aux_p1[1])
        return objeto_geometrico_aux

    def aplica_transformacoes_reta(self, objeto_geometrico: Reta):
        matriz_aux_p1 = np.dot(self.matriz, 
                            objeto_geometrico.p1.matriz)
        matriz_aux_p2 = np.dot(self.matriz, 
                            objeto_geometrico.p2.matriz) 
        
        # Cria um objeto geométrico auxiliar para retornar as novas
        # coordenadas da reta
        objeto_geometrico_aux = Reta(Ponto(matriz_aux_p1[0], matriz_aux_p1[1]),
                                     Ponto(matriz_aux_p2[0], matriz_aux_p2[1]))
        return objeto_geometrico_aux  

    def aplica_transformacoes_poligono(self, objeto_geometrico: Poligono):
        lista_pontos_aux = []
        for ponto in objeto_geometrico.lista_pontos:
            matriz_aux_ponto = np.dot(self.matriz, ponto.matriz)         
            lista_pontos_aux.append(Ponto(matriz_aux_ponto[0],matriz_aux_ponto[1]))

        # Cria um objeto geométrico auxiliar para retornar as novas
        # coordenadas do poligono
        objeto_geometrico_aux = Poligono(lista_pontos_aux)
        return objeto_geometrico_aux                              