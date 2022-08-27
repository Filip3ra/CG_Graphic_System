class Viewport:
  def __init__(self, min_ponto_2d, max_ponto_2d):
    self.min_ponto = min_ponto_2d
    self.max_ponto = max_ponto_2d

# método especial usado para representar o objeto da classe como string
  def __repr__(self): 
    return f'Min Point = {self.min_ponto} | Max Point = {self.max_ponto}'
