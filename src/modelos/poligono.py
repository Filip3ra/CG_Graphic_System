from auxiliares import VizObjViewport
from modelos.ponto import Ponto
from modelos.reta import Reta
from modelos.window import Window
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

    def clipping_poligono(self, dados_entrada: list, dados_saida: list):
        ## 1 - Cria lista dos polígonos e descobre as interseções
        lista_pontos_inter = []
        lista_poligono = []
        for index in range(len(self.lista_pontos)):
            lista_poligono.append(self.lista_pontos[index])

            try:
                ponto_aux = Ponto(self.lista_pontos[index+1])
            except:
                ## Caso o ponto 1 seja o último, a reta fecha com o ponto 0
                ponto_aux = Ponto(self.lista_pontos[0])

            reta_aux = Reta(Ponto(self.lista_pontos[index]),
                                  ponto_aux)          

            lista_pontos_inter_aux = reta_aux.clipping_liang_barsky(dados_entrada= dados_entrada,
                                                                    return_intersecao= True)
            lista_pontos_inter.append(ponto_aux for ponto_aux in lista_pontos_inter_aux)
            lista_poligono.append(ponto_aux for ponto_aux in lista_pontos_inter_aux)
            lista_poligono.append(ponto_aux)

        ## 2.1 - Cria lista da janela
        lista_janela = []
        for objeto in dados_saida:
            if isinstance(objeto, Window):
                window = objeto
                p2_window = Ponto(window.ponto_min.x, window.ponto_max.y)
                p4_window = Ponto(window.ponto_max.x, window.ponto_min.y)

                lista_janela.append(window.ponto_min)

                ## Verifica em cada segmento de reta se tem pontos de interseção
                # para adicionar na lista da janela
                reta_window = Reta(window.ponto_min, p2_window)
                adiciona_pontos_lista(lista_pontos_inter = lista_pontos_inter,
                                      lista_janela = lista_janela,
                                      reta = reta_window)
                lista_janela.append(p2_window)

                reta_window = Reta(p2_window, window.ponto_max)
                adiciona_pontos_lista(lista_pontos_inter = lista_pontos_inter,
                                      lista_janela = lista_janela,
                                      reta = reta_window)
                lista_janela.append(window.ponto_max)

                reta_window = Reta(window.ponto_max, p4_window)
                adiciona_pontos_lista(lista_pontos_inter = lista_pontos_inter,
                                      lista_janela = lista_janela,
                                      reta = reta_window)
                lista_janela.append(p4_window)

                reta_window = Reta(p4_window, window.ponto_min)
                adiciona_pontos_lista(lista_pontos_inter = lista_pontos_inter,
                                      lista_janela = lista_janela,
                                      reta = reta_window)

        ## 3 - Verifica pontos de entrada e saida

        ## 4 - Inicia pela lista do polígono, encontra o 1° ponto de entrada

        ## 5 - Se encontrar ponto de saída, procura ele na lista da janela

        ## 6 - Se encontrar ponto de janela, procura ele na lista de polígono
       
    def reset(self):
        for index in range(len(self.lista_pontos)):
            self.lista_pontos[index].reset()

def adiciona_pontos_lista(lista_pontos_inter: list,
                          lista: list,
                          reta: Reta):
    for ponto_inter in lista_pontos_inter:
        if (reta.p1.x <= ponto_inter.x) & \
            (ponto_inter.x <= reta.p2.x) & \
            (reta.p1.y <= ponto_inter.y) & \
            (ponto_inter.y <= reta.p2.y):
            ## Achou o ponto de interseção nesse segmento de reta
            lista.append(ponto_inter)
            lista_pontos_inter.remove(ponto_inter)
        
    return lista