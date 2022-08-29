from auxiliares import converte_valores_dicionario_para_numerico


class Ponto3D_float:
    def __init__(self, x, y, z):
        numero_x = isinstance(x, int) or isinstance(x, float)
        numero_y = isinstance(y, int) or isinstance(y, float)
        numero_z = isinstance(z, int) or isinstance(z, float)

        if not numero_x or not numero_y or not numero_z:
            raise ValueError(
                'Valor errado, as coordenadas devem ser um numero.')
        else:
            self.x = x
            self.y = y
            self.z = z

    def __str__(self) -> str:
        return f'Ponto 3D: ({self.x},{self.y},{self.z})'

    def cria_atributos_dicionario_do_xml(dic):
        dic = converte_valores_dicionario_para_numerico(dic, 'float')
        return Ponto3D_float(dic['x'], dic['y'], dic['z'])
