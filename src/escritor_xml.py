from asyncore import write
import pandas as pd
import os


def gera_arquivo_saida(dados_saida):
    dados = []
    dados.append('PONTOS:')

    if len(dados_saida['pontos']) > 0:
        for ponto in dados_saida['pontos']:
            dados.append('x =' + str(ponto.x))
            dados.append('y =' + str(ponto.y))

    meu_arquivo = pd.DataFrame(dados)

    NOME_ARQUIVO = 'saida.csv'
    meu_arquivo.to_csv(os.path.join(os.path.dirname(
        __file__),'..', 'saida', NOME_ARQUIVO), header=False, index=False)
