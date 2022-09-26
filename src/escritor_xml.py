from asyncore import write
import pandas as pd
import os
import xml.etree.ElementTree as ET

# Função para gerar um arquivo de sáida com as transformações aplicadas na entrada.



def gera_arquivo_saida(dados_saida, nome_arquivo_saida):
    # O array 'dados' irá guardar as informações contitas em 'dados_saida'
    dados = []
    raiz = ET.Element('root')
    arvore = ET.ElementTree(raiz)

    # percorre 'dados_saida' que está estruturada em pontos, retas e poligonos
    if len(dados_saida['pontos']) > 0:
        grupo_pontos = ET.SubElement(raiz, 'pontos')
        for ponto in dados_saida['pontos']:
            ET.SubElement(grupo_pontos, 'ponto', x = str(ponto.x), y = str(ponto.y))
#            str_ponto = '(' + str(ponto.x) + ', ' + str(ponto.y) + ')'
 #           dados.append(str_ponto)

    if len(dados_saida['retas']) > 0:
        grupo_retas = ET.SubElement(raiz, 'retas')
        for reta in dados_saida['retas']:            
            linha = ET.SubElement(grupo_retas, 'retas')
            ET.SubElement(linha, 'ponto', x = str(reta.point_1.x), y = str(reta.point_1.y))
            ET.SubElement(linha, 'ponto', x = str(reta.point_2.x), y = str(reta.point_2.y))
        #    str_reta = '((' + str(reta.p1.x) + ', ' + str(reta.p1.y) + \
        #        '), (' + str(reta.p2.x) + ', ' + str(reta.p2.y) + '))'
        #    dados.append(str_reta)

    if len(dados_saida['poligonos']) > 0:
        grupo_poligonos = ET.SubElement(raiz, 'poligonos')
        for poligono in dados_saida['poligonos']:
            poli = ET.SubElement(grupo_poligonos, 'poligonos')
            for ponto in poligono.lista_pontos:
                ET.SubElement(poli, 'ponto', x = str(ponto.x), y = str(ponto.y))
    
    arvore.write(nome_arquivo_saida, encoding = "utf-8", xml_declaration = True)
    print('Arquivo gerado com sucesso!')
    
