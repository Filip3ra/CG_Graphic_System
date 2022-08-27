from asyncore import write
import pandas as pd


def gera_arquivo_saida(dados_saida):
    dados = []
    dados.append('PONTOS:')

    if len(dados_saida['pontos']) > 0:
        for ponto in dados_saida['pontos']:
            dados.append('x =' + str(ponto.x))
            dados.append('y =' + str(ponto.y))

    meu_arquivo = pd.DataFrame(dados)
    meu_arquivo.to_csv('saida/saida.csv', header=False, index=False)
