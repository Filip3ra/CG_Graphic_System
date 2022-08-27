# vou converter esse valor pra inteiro de fato
def converte_valores_dicionario_para_numerico(dic, int_ou_float):
    if int_ou_float != 'int' and int_ou_float != 'float':
        raise ValueError('O parâmetro int_ou_float deve ser "int" ou "float".')

    # estou acessando a estrutura da minha árvore
    # dic.items() == [('x', '10'), ('y', '10')])   onde key guarda o 'x' e value guarda o '10'
    if int_ou_float == 'int':
        for key, value in dic.items():
            dic[key] = int(value)
    else:
        for key, value in dic.items():
            dic[key] = float(value)

    return dic
