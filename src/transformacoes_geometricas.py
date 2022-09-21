import numpy as np

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

    def diminui_objeto(self):
        # Diminui em 10% do tamanho atual
        Sx = 0.9
        Sy = 0.9
        matriz_diminuir = [[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]]
        self.matriz = np.dot(matriz_diminuir, self.matriz)
    
    def amplia_objeto(self):
        # Amplia em 10% do tamanho atual
        Sx = 1.1
        Sy = 1.1
        matriz_ampliar = [[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]]
        self.matriz = np.dot(matriz_ampliar, self.matriz)

    def limpar(self):
        self.matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]