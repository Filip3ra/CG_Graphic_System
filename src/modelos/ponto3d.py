from auxiliares import converte_valores_dicionario_para_numerico


class Ponto2D_float:
    def __init__(self, x, y):
        numero_x = isinstance(x, int) or isinstance(x, float)
        numero_y = isinstance(y, int) or isinstance(y, float)

        if not numero_x or not numero_y:
            raise ValueError(
                'Valor errado, as coordenadas devem ser um numero.')
        else:
            self.x = x
            self.y = y

    def __str__(self) -> str:
        return f'Ponto 3D: ({self.x},{self.y})'

    def cria_atributos_dicionario_do_xml(dic):
        dic = converte_valores_dicionario_para_numerico(dic, 'float')
        return Ponto2D_float(dic['x'], dic['y'])
