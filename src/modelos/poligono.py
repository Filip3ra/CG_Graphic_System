from auxiliares import VizObjViewport
from transformacoes_geometricas import TransformacaoGeometrica
from modelos.objeto_geometrico import ObjetoGeometrico

class Poligono(ObjetoGeometrico):
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
            self.exibe_obj_viewport = VizObjViewport.DENTRO

    def __str__(self) -> str:
        str_ = 'Poligono: '
        for ponto in self.lista_pontos:
            str_ += f'{ponto} '
        return str_

    def centro_objeto(self):
        '''
        Função que realiza o cálculo do centro do polígono. 
        '''
        soma_x = 0
        soma_y = 0
        for i in range(len(self.lista_pontos)):
            soma_x += self.lista_pontos[i].x
            soma_y += self.lista_pontos[i].y
        Cx = soma_x / len(self.lista_pontos)
        Cy = soma_y / len(self.lista_pontos)
        return Cx, Cy

    def aplica_transformacoes(self, transformacoes: TransformacaoGeometrica):
        for index in range(len(self.lista_pontos)):
            self.lista_pontos[index].aplica_transformacoes(transformacoes)

    def atualiza_valores_PPC(self, transformacao: TransformacaoGeometrica):
        for index in range(len(self.lista_pontos)):
            self.lista_pontos[index].atualiza_valores_PPC(transformacao)

    def aplica_transformada(self, window, viewport):
        for index in range(len(self.lista_pontos)):
            self.lista_pontos[index].aplica_transformada(window, viewport)
            
    def reset(self):
        for index in range(len(self.lista_pontos)):
            self.lista_pontos[index].reset()