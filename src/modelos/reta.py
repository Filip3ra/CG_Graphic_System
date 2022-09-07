# classe onde obtenho os dados da reta, ou seja, seus dois pontos
class Reta:
    # p1 e p2 são os pontos de início e fim de uma reta
    def __init__(self, p1, p2):
        if p1 == p2:
            raise ValueError(
                'Erro: Pontos iguais, p1 e p2 devem ser diferentes')
        else:
            self.p1 = p1
            self.p2 = p2

    def __str__(self) -> str:
        return f'Reta: {self.p1} {self.p2}'
