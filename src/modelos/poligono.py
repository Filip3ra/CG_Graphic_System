import copy
from auxiliares import PontoIntersecao, VizObjViewport, pontos_iguais
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

    def clipping_poligono(self, dados_entrada: dict, dados_saida: list):
        ## 1 - Cria lista dos polígonos e descobre as interseções
        lst_pts_inter = []
        lst_poligono = []
        lst_poligono,lst_pontos_inter = cria_lst_poligono_inter(dados_entrada= dados_entrada,
                                                                lista_pontos= self.lista_pontos)

        # TODO verificar qnd a reta está toda dentro

        ## 2.1 - Cria lista da janela
        lst_janela = []
        lst_janela = cria_lst_janela(dados_entrada= dados_entrada,
                                     lista_pts_inter= lst_pontos_inter)

        ## 4 - Inicia pela lista do polígono, encontra o 1° ponto de entrada
        flag_achou_ponto = False
        
        '''Lista com os pontos do polígono que foi encontrado no clipping'''
        lst_poligono_clip = []

        print(f'Lista poligono:')
        for p in lst_poligono:
            print(p)

        print(f'Lista janela:')
        for p in lst_janela:
            print(p)
        '''
        for ponto_poligono in lst_poligono:
            if ponto_poligono.flag_ponto_inter == PontoIntersecao.ENTRANDO:
                lst_poligono_clip.append(ponto_poligono)

                for ponto_janela in lst_janela:
                    if pontos_iguais(ponto_poligono, ponto_janela):
                        flag_achou_ponto = True
                        break
                    else:
                        lst_poligono_clip.append(ponto_janela)

                    if ponto_janela.flag_ponto_inter == PontoIntersecao.SAINDO:
                        break

            if flag_achou_ponto:
                break
            '''
        print('Lista clip:')
        for p in lst_poligono_clip:
            print(p)

    def reset(self):
        for index in range(len(self.lista_pontos)):
            self.lista_pontos[index].reset()

def add_pontos_lista(lst_pts_inter: list,
                     lista: list,
                     reta: Reta):
    for ponto_inter in lst_pts_inter:
        if ((reta.p1.x <= ponto_inter.x <= reta.p2.x) | \
            (reta.p2.x <= ponto_inter.x <= reta.p1.x)) & \
           ((reta.p1.y <= ponto_inter.y <= reta.p2.y) | \
            (reta.p2.y <= ponto_inter.y <= reta.p1.y)):
            ## Achou o ponto de interseção nesse segmento de reta
            lista.append(ponto_inter)
        
    return lista

def cria_lst_poligono_inter(dados_entrada: dict,
                            lista_pontos: list):
    """Cria 2 listas: uma de poligonos e outra dos pontos de interseção.

    Args:
        dados_entrada (dict): Dados de entrada dos objetos
        lista_pontos (list): Pontos do polígono

    Returns:
        list: Pontos do polígono 
        list: Pontos de interseção
    """
    lst_poligono = []
    for index in range(len(lista_pontos)):
        lst_pts_inter = []
        print(f'Add {lista_pontos[index]}')
        lst_poligono.append(lista_pontos[index])

        try:
            ponto_aux = lista_pontos[index+1]
        except:
            ## Caso o ponto 1 seja o último, a reta fecha com o ponto 0
            ponto_aux = lista_pontos[0]

        reta_aux = Reta(Ponto(lista_pontos[index].x, lista_pontos[index].y),
                        Ponto(ponto_aux.x, ponto_aux.y))

        reta_aux.clipping_liang_barsky(dados_entrada= dados_entrada)

        print(f'-> {reta_aux} , {lista_pontos[index]}')
        if not pontos_iguais(reta_aux.p1, lista_pontos[index]):
            ponto_inter = Ponto(reta_aux.p1.x, reta_aux.p1.y)
            lst_pts_inter.append(ponto_inter)
            print(f'Add {ponto_inter}')

        if not pontos_iguais(reta_aux.p2, ponto_aux):
            ponto_inter = Ponto(reta_aux.p2.x, reta_aux.p2.y)
            lst_pts_inter.append(ponto_inter)
            print(f'Add {ponto_inter}')

        lst_poligono.append(p for p in lst_pts_inter)

    return lst_poligono, lst_pts_inter

def cria_lst_janela(dados_entrada: dict,
                      lista_pts_inter: list):
    lst_janela = []
    window = dados_entrada["window"]
    viewport = dados_entrada["viewport"]
    p1_window = Ponto(viewport.ponto_min.x, viewport.ponto_min.y)
    p2_window = Ponto(viewport.ponto_min.x, viewport.ponto_max.y)
    p3_window = Ponto(viewport.ponto_max.x, viewport.ponto_max.y)
    p4_window = Ponto(viewport.ponto_max.x, viewport.ponto_min.y)

    lst_janela.append(p1_window)

    ## Verifica em cada segmento de reta se tem pontos de interseção
    # para adicionar na lista da janela
    reta_window = Reta(p1_window, p2_window)
    lst_janela = add_pontos_lista(lst_pts_inter = lista_pts_inter,
                                  lista = lst_janela,
                                  reta = reta_window)
    lst_janela.append(p2_window)

    reta_window = Reta(p2_window, p3_window)
    lst_janela = add_pontos_lista(lst_pts_inter = lista_pts_inter,
                                  lista = lst_janela,
                                  reta = reta_window)
    lst_janela.append(p3_window)

    reta_window = Reta(p3_window, p4_window)
    lst_janela = add_pontos_lista(lst_pts_inter = lista_pts_inter,
                                  lista = lst_janela,
                                  reta = reta_window)
    lst_janela.append(p4_window)

    reta_window = Reta(p4_window, p1_window)
    lst_janela = add_pontos_lista(lst_pts_inter = lista_pts_inter,
                                  lista = lst_janela,
                                  reta = reta_window)

    return lst_janela