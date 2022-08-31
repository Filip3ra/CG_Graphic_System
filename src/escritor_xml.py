from asyncore import write
import pandas as pd
import os


def gera_arquivo_saida(dados_saida, nome_arquivo_saida):
    dados = []

    dados.append('PONTOS:')
    if len(dados_saida['pontos']) > 0:
        for ponto in dados_saida['pontos']:
            str_ponto = '(' + str(ponto.x) + ', ' + str(ponto.y) + ')'
            dados.append(str_ponto)
            #dados.append('x =' + str(ponto.x))
            #dados.append('y =' + str(ponto.y))

    if len(dados_saida['retas']) > 0:
        dados.append('RETAS:')
        for reta in dados_saida['retas']:
            str_reta = '((' + str(reta.p1.x) + ', ' + str(reta.p1.y) + '), (' + str(reta.p2.x) + ', ' + str(reta.p2.y) + '))'
            dados.append(str_reta)
            #dados.append('x =' + str(reta.p1.x))
            #dados.append('y =' + str(reta.p2.y))

    if len(dados_saida['poligonos']) > 0:
        dados.append('POLIGONOS:')
        for poligono in dados_saida['poligonos']:
            str_poligono = '('
            qtd_pontos = len(poligono.lista_pontos)
            for ponto in poligono.lista_pontos:
                ## Forma de adicionar mais pontos ao poligono
                if qtd_pontos > 1:
                    str_poligono += '(' + str(ponto.x) + ', ' + str(ponto.y) + '), '
                else:
                    str_poligono += '(' + str(ponto.x) + ', ' + str(ponto.y) + ')'
                qtd_pontos -= 1

            str_poligono += ')'
            dados.append(str_poligono)

    meu_arquivo = pd.DataFrame(dados)

    meu_arquivo.to_csv(os.path.join(os.path.dirname(
        __file__),'..', 'saida', nome_arquivo_saida + '.csv'), header=False, index=False)
