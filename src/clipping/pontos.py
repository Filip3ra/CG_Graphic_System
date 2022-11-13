
def ponto_fora_da_window(window, ponto):
  x_fora_da_window = window.min_point.x >= ponto.x or window.max_point.x <= ponto.x
  y_fora_da_window = window.min_point.y >= ponto.y or window.max_point.y <= ponto.y
  return x_fora_da_window or y_fora_da_window