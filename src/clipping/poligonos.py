from PyQt5.QtWidgets import QDialog
from modelos.poligono import Poligono
from modelos.ponto import Ponto

from modelos.reta import Reta
from modelos.window import Window

def adiciona_lista_janela(lista_pontos_inter: list,
                          lista_janela: list,
                          reta: Reta):
    for ponto_inter in lista_pontos_inter:
        if (reta.p1.x <= ponto_inter.x) & \
            (ponto_inter.x <= reta.p2.x) & \
            (reta.p1.y <= ponto_inter.y) & \
            (ponto_inter.y <= reta.p2.y):
            ## Achou o ponto de interseção nesse segmento de reta
            lista_janela.append(ponto_inter)
            lista_pontos_inter.remove(ponto_inter)

def clipping_poligono(ui: QDialog,
                      dados_entrada: list,
                      dados_saida: list):
    '''
    Algoritmo de clipping de Weiler-Atherton.
    '''
    ## 1 - Calcula pontos de interseção entre janela e polígono
    lista_pontos_inter = []
    for objeto in dados_saida:
        if isinstance(objeto, Poligono):
            poligono = objeto
            for index in range(len(poligono.lista_pontos)):
                ponto_aux_1 = Ponto(poligono.lista_pontos[index])
                try:
                    ponto_aux_2 = Ponto(poligono.lista_pontos[index+1])
                except:
                    ## Caso o ponto 1 seja o último, a reta fecha com o ponto 0
                    ponto_aux_2 = Ponto(poligono.lista_pontos[0])

                reta_aux = Reta(ponto_aux_1, ponto_aux_2)

                ## TODO Para cada reta precisa encontrar as interseções
                # lista_pontos_inter.append(intersecoes)

    ## 1.1 -  
    ## 2 - Cria lista dos polígonos

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
            adiciona_lista_janela(lista_pontos_inter = lista_pontos_inter,
                                  lista_janela = lista_janela,
                                  reta = reta_window)
            lista_janela.append(p2_window)

            reta_window = Reta(p2_window, window.ponto_max)
            adiciona_lista_janela(lista_pontos_inter = lista_pontos_inter,
                                  lista_janela = lista_janela,
                                  reta = reta_window)
            lista_janela.append(window.ponto_max)

            reta_window = Reta(window.ponto_max, p4_window)
            adiciona_lista_janela(lista_pontos_inter = lista_pontos_inter,
                                  lista_janela = lista_janela,
                                  reta = reta_window)
            lista_janela.append(p4_window)

            reta_window = Reta(p4_window, window.ponto_min)
            adiciona_lista_janela(lista_pontos_inter = lista_pontos_inter,
                                  lista_janela = lista_janela,
                                  reta = reta_window)

    ## 3 - Verifica pontos de entrada e saida

    ## 4 - Inicia pela lista do polígono, encontra o 1° ponto de entrada

    ## 5 - Se encontrar ponto de saída, procura ele na lista da janela

    ## 6 - Se encontrar ponto de janela, procura ele na lista de polígono