
from leitor_xml import LeitorEntradaXml
from transformacao import Transformacao
from escritor_xml import gera_arquivo_saida

# leio arquivo xml de entrada e obtenho os dados
dados_entrada = LeitorEntradaXml().getDadosEntradaCompletos()

# executo transformação em cima dos dados lidos
transformacao = Transformacao(dados_entrada['window'], dados_entrada['viewport'])

dados_saida = {
    'pontos': []
}

for w_ponto in dados_entrada['pontos']:
    v_ponto = transformacao.transformada_ponto(w_ponto)
    dados_saida['pontos'].append(v_ponto)

gera_arquivo_saida(dados_saida)
