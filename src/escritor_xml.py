from asyncore import write
from auxiliares import indenta_xml
import pandas as pd
import os
import xml.etree.ElementTree as ET


dados_saida_xml = {
    'pontos': [],
    'retas': [],
    'poligonos': []
}


def guarda_arquivo_saida(saida_xml):
    global dados_saida_xml
    dados_saida_xml = saida_xml


# Função para gerar um arquivo de sáida com as transformações aplicadas na entrada.
# dados_saida_xml: list, nome_arquivo_saida: str
def gera_arquivo_saida():
    # O array 'dados' irá guardar as informações contitas em 'dados_saida_xml'
    dados = []
    raiz = ET.Element('root')
    arvore = ET.ElementTree(raiz)
    global dados_saida_xml

    # percorre 'dados_saida_xml' que está estruturada em pontos, retas e poligonos
    if len(dados_saida_xml['pontos']) > 0:
        grupo_pontos = ET.SubElement(raiz, 'pontos')
        for ponto in dados_saida_xml['pontos']:
            print(ponto)
            print('-->', dados_saida_xml['pontos'])

            ET.SubElement(grupo_pontos, 'ponto',
                          x=str(ponto.x), y=str(ponto.y))
#            str_ponto = '(' + str(ponto.x) + ', ' + str(ponto.y) + ')'
 #           dados.append(str_ponto)
    #print('\n-->', dados_saida_xml['pontos'])
    #print('\n\n-->', dados_saida_xml['retas'])
    #print('\n\n-->', dados_saida_xml['poligonos'])

    if len(dados_saida_xml['retas']) > 0:
        grupo_retas = ET.SubElement(raiz, 'retas')
        for reta in dados_saida_xml['retas']:
            linha = ET.SubElement(grupo_retas, 'retas')
            # print(reta)
            #print('-->', dados_saida_xml['retas'])
            ET.SubElement(linha, 'ponto', x=str(reta.p1.x), y=str(reta.p1.y))
            ET.SubElement(linha, 'ponto', x=str(reta.p2.x), y=str(reta.p2.y))
        #    str_reta = '((' + str(reta.p1.x) + ', ' + str(reta.p1.y) + \
        #        '), (' + str(reta.p2.x) + ', ' + str(reta.p2.y) + '))'
        #    dados.append(str_reta)

    if len(dados_saida_xml['poligonos']) > 0:
        grupo_poligonos = ET.SubElement(raiz, 'poligonos')
        for poligono in dados_saida_xml['poligonos']:
            poli = ET.SubElement(grupo_poligonos, 'poligonos')
            for ponto in poligono.lista_pontos:
                ET.SubElement(poli, 'ponto', x=str(ponto.x), y=str(ponto.y))

    indenta_xml(raiz)

    arvore.write('saida.xml', encoding="utf-8", xml_declaration=True)
    print('Arquivo gerado com sucesso!')
