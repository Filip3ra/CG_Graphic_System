from auxiliares import converte_valores_dicionario_para_numerico

class Ponto3D:
    def __init__(self, x, y, z):
        numero_x = isinstance(x, int) or isinstance(x, float)
        numero_y = isinstance(y, int) or isinstance(y, float)
    
        if not numero_x or not numero_y:
            raise ValueError('Valor errado, as coordenadas devem ser um numero.')
        else:
            self.x = x 
            self.y = y
            self.z = z

    def cria_atributos_dicionario_do_xml(dic):
        dic = converte_valores_dicionario_para_numerico(dic, 'float')
        return Ponto3D(dic['x'], dic['y'], dic['z'])