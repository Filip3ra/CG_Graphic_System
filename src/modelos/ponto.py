import numpy as np

from modelos.objeto_geometrico import ObjetoGeometrico
from auxiliares import VizObjViewport, converte_valores_dicionario_para_numerico
from transformacoes_geometricas import TransformacaoGeometrica

class Ponto(ObjetoGeometrico):
    '''
    Classe para representar o objeto geométrico Ponto.
    '''
    def __init__(self, x, y):
        # isintance() verifica se o objeto(x ou y) é do tipo especificado(int ou float)
        numero_x = isinstance(x, int) or isinstance(x, float)
        numero_y = isinstance(y, int) or isinstance(y, float)

        # garante que estou lendo um valor numérico
        if not numero_x or not numero_y:
            raise ValueError(
                'Valor errado, as coordenadas devem ser um numero.')
        else:
            self.x = x
            self.y = y
            # Coordenadas do PPC
            self.x_original = x
            self.y_original = y
            self.matriz = [x, y, 1]
            self.matriz_original = [x, y, 1]
            self.exibe_obj_viewport = VizObjViewport.DENTRO

    def __str__(self) -> str:
        return f'Ponto: ({self.x}, {self.y})'

    def centro_objeto(self):
        return self.x, self.y

    # acesso os valores do .xml e faço a conversão deles para um número
    def cria_atributos_dicionario_do_xml_int(dic):
        dic = converte_valores_dicionario_para_numerico(dic, 'float')
        return Ponto(dic['x'], dic['y'])

    def aplica_transformacoes(self, transformacoes: TransformacaoGeometrica):
        print(f'Apl. transf. -> X: {self.x} - X_ORI: {self.x_original}')
        self.matriz = np.dot(transformacoes.matriz, self.matriz)
        self.x = self.matriz[0]
        self.y = self.matriz[1]

    def atualiza_valores_PPC(self, transformacao: TransformacaoGeometrica):
        print(f'At. val. ppc -> X: {self.x} - X_ORI: {self.x_original}')        
        self.matriz = np.dot(transformacao.matriz, self.matriz)
        self.x = self.matriz[0]
        self.y = self.matriz[1]
    
    def aplica_transformada(self, window, viewport):
        # Window
        Xw_min = window.ponto_min.x
        Xw_max = window.ponto_max.x
        Yw_min = window.ponto_min.y
        Yw_max = window.ponto_max.y
        # Viewport
        Xv_min = viewport.ponto_min.x
        Xv_max = viewport.ponto_max.x
        Yv_min = viewport.ponto_min.y
        Yv_max = viewport.ponto_max.y

        # As duas equações de transformação são:
        # Xvp = ( (Xw - Xw_min) / Xw_max - Xw_min ) * (Xvp_max - Xvp_min)
        self.x = (self.x - Xw_min) / \
            (Xw_max - Xw_min) * (Xv_max - Xv_min)

        # Yvp = (1 - (Yw - Yw_min) / (Yw_max - Yw_min)) * (Yvp_max - Yvp_min)
        self.y = (1 - ((self.y - Yw_min) /
                (Yw_max - Yw_min))) * (Yv_max - Yv_min)

    def clipping_ponto(self, dados_entrada: dict, dados_saida: list):
        """Função que verifica se o ponto está dentro da janela de viewport.

        Args:
            dados_entrada (dict): Dados de entrada dos objetos
            dados_saida (list): Dados de saída dos objetos (dados transformados)
        """        
        if (dados_entrada['viewport'].ponto_min.x <= self.x <= dados_entrada['viewport'].ponto_max.x) & \
           (dados_entrada['viewport'].ponto_min.y <= self.y <= dados_entrada['viewport'].ponto_max.y):
            self.exibe_obj_viewport = VizObjViewport.DENTRO
        else:
            self.exibe_obj_viewport = VizObjViewport.FORA

    def reset(self):
        self.x = self.x_original
        self.y = self.y_original
        self.matriz = self.matriz_original

