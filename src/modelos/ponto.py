from auxiliares import converte_valores_dicionario_para_numerico

class Ponto:
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
            self.matriz = [x, y, 1]

    def __str__(self) -> str:
        return f'Ponto: ({self.x}, {self.y})'

    def centro_objeto(self):
        return self.x, self.y

    # acesso os valores do .xml e faço a conversão deles para um número
    def cria_atributos_dicionario_do_xml_int(dic):
        dic = converte_valores_dicionario_para_numerico(dic, 'float')
        return Ponto(dic['x'], dic['y'])
