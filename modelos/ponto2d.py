
class Ponto2D:
    def __init__(self, x, y):
        numero_x = isinstance(x, int) or isinstance(x, float)
        numero_y = isinstance(y, int) or isinstance(y, float)
    
        # garante que estou lendo um valor numérico
        if not numero_x or not numero_y:
            raise ValueError('As coordenadas do ponto (x, y) devem ser um numero.')

        self.x = x 
        self.y = y


    def converte_valores_dicionario_para_numerico(dic, int_ou_float):
        if int_ou_float != 'int' and int_ou_float != 'float':
            raise ValueError('The parameter int_or_float must be "int" or "float".')

        if int_ou_float == 'int':
            for key, value in dic.items():
                dic[key] = int(value)
        else:
            for key, value in dic.items():
                dic[key] = float(value)

        return dic

    def cria_atributos_dicionario(dic):
        dic = converte_valores_dicionario_para_numerico(dic, 'int')
        return Ponto2D(dic['x'], dic['y'])

