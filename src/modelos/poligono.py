class Poligono:
    def __init__(self, lista_pontos) -> None:
        if len(lista_pontos) < 3:
            raise ValueError("O polígono precisa ter no mínimo três pontos que não sejam coincidentes")
        else:
            self.lista_pontos = lista_pontos