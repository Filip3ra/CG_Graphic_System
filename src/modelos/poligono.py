import numpy as np

class Poligono:
    '''
    Classe para representar o objeto geométrico Poligono.

    Obs: A lista de pontos representa os pontos que constituem um poligono.
    '''
    def __init__(self, lista_pontos: list) -> None:
        if len(lista_pontos) < 3:
            raise ValueError(
                "O polígono precisa ter no mínimo três pontos que não sejam coincidentes")
        else:
            self.lista_pontos = lista_pontos

    def __str__(self) -> str:
        str_ = 'Poligono: '
        for ponto in self.lista_pontos:
            str_ += f'{ponto} '
        return str_

    def centro_objeto(self):
        '''
        Função que realiza o cálculo do centro do polígono. 
        O cálculo apresentado nessa função foi baseado no seguinte site:
        - https://dan-scientia.blogspot.com/2009/10/centroide-de-um-poligono.html
        '''
        # Fórmula da área de um polígono
        parte_1_equacao_area = 0
        for i in range(len(self.lista_pontos)-1):
            parte_1_equacao_area += self.lista_pontos[i].x * self.lista_pontos[i+1].y - \
                                    self.lista_pontos[i+1].x * self.lista_pontos[i].y

        area = 0.5 * parte_1_equacao_area

        # Fórmula das coordenadas do centro de um polígono
        sum_equacao_coord_Cx = 0
        sum_equacao_coord_Cy = 0
        for i in range(len(self.lista_pontos)-1):
            sum_equacao_coord_Cx += (self.lista_pontos[i].x + self.lista_pontos[i+1].x) * \
                                    (self.lista_pontos[i].x * self.lista_pontos[i+1].y - \
                                     self.lista_pontos[i+1].x * self.lista_pontos[i].y)
            sum_equacao_coord_Cy += (self.lista_pontos[i].y + self.lista_pontos[i+1].y) * \
                                    (self.lista_pontos[i].x * self.lista_pontos[i+1].y - \
                                     self.lista_pontos[i+1].x * self.lista_pontos[i].y)

        Cx = 1/(6*area) * sum_equacao_coord_Cx
        Cy = 1/(6*area) * sum_equacao_coord_Cy
        return Cx, Cy
