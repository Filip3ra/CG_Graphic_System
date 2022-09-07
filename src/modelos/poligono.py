# classe onde tenho a lista de pontos que constituem um poligono
class Poligono:
    def __init__(self, lista_pontos) -> None:
        if len(lista_pontos) < 3:
            raise ValueError(
                "O polígono precisa ter no mínimo três pontos que não sejam coincidentes")
        else:
            self.lista_pontos = lista_pontos

    def __str__(self) -> str:
        str_ = 'Poligono: '
        for ponto in self.lista_pontos:
            str_ += f'{ponto} '
        return str_
