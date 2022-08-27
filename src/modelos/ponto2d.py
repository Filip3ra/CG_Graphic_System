from auxiliares import converte_valores_dicionario_para_numerico


class Ponto2D_int:
    def __init__(self, x, y):
        # isintance == verifica se o objeto(x ou y) é do tipo especificado(int ou float)
        numero_x = isinstance(x, int) or isinstance(x, float)
        numero_y = isinstance(y, int) or isinstance(y, float)

        # garante que estou lendo um valor numérico
        if not numero_x or not numero_y:
            raise ValueError(
                'Valor errado, as coordenadas devem ser um numero.')
        else:
            self.x = x
            self.y = y

    def cria_atributos_dicionario_do_xml(dic):
        dic = converte_valores_dicionario_para_numerico(dic, 'int')
        return Ponto2D_int(dic['x'], dic['y'])
