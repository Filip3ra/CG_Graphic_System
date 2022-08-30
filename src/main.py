import sys
from leitor_xml import LeitorEntradaXml
from transformacao import Transformacao
from escritor_xml import gera_arquivo_saida

if __name__ == '__main__':

    ## Nome do arquivo .xml passado como argumento
    ## Chamada do arquivo: python main.py <nome_arquivo_xml> <nome_arquivo_saida Opcional>
    arquivo_xml = sys.argv[1]
    if sys.argv[2] is not None:
        nome_arquivo_saida = sys.argv[2]
    else:
        nome_arquivo_saida = 'saida'

    # Leio o arquivo xml de entrada e obtenho os dados
    dados_entrada = LeitorEntradaXml(arquivo_xml).getDadosEntradaCompletos()

    # executo transformação em cima dos dados lidos
    transformacao = Transformacao(dados_entrada['window'], dados_entrada['viewport'])

    dados_saida = {
        'pontos': [],
        'retas': []
    }

    for w_ponto in dados_entrada['pontos']:
        v_ponto = transformacao.transformada_ponto(w_ponto)
        dados_saida['pontos'].append(v_ponto)

    for w_reta in dados_entrada['retas']:
        v_reta = transformacao.transformada_reta(w_reta)
        dados_saida['retas'].append(v_reta)

    gera_arquivo_saida(dados_saida, nome_arquivo_saida)
