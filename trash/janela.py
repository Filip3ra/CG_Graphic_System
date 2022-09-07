from PySide6 import QtCore, QtGui, QtWidgets

HABILITA_COORDENADAS = True

# 'dados_objetos' deve conter as informações dos pontos após a transformação,
# mas pra isso tem que melhorar a saída, organizar os dados de modo que fica
# fácil acessar por aqui. 
#
# Uma forma seria configurar a saída em xml, aproveitar que já tem um leitor xml e etc, 
# mas acho trabalhoso. 
# 
# Outra solução seria simplesmente ler a saía e organizar num conjunto de arrays, um pra 
# ponto, linhas e poligonos. 
# 
# Por enquanto coloquei 'dados_objetos' com os dados da entrada só pra testar se funciona. 
def renderiza_objetos(dados_objetos, dados_viewport):
    app = QtWidgets.QApplication()
    janela = Renderizador(dados_objetos, dados_viewport)
    janela.show()
    app.exec()
    #print('---> ')

class Renderizador(QtWidgets.QWidget):
    def __init__(self, dados_obj, dados_vp):
        super().__init__()
        self.dados_obj = dados_obj
        self.dados_vp = dados_vp
        self.config_window()
        self.config_background()

    # configura dimensões da viewport
    def config_window(self):
        largura = self.dados_vp.xvmin + self.dados_vp.xvmax
        altura = self.dados_vp.yvmin + self.dados_vp.yvmax
        
        self.setFixedSize(QtCore.QSize(largura, altura))
        self.setWindowTitle(f'Janela {int(largura)} x {int(altura)} px')

    # permite configurar o fundo
    def config_background(self): # change
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.Qt.white)
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def paintEvent(self, event): # change
        self.desenha_limites_viewport()
        self.desenha_ponto()
        #self.drawLines()
        #self.drawPolygons()
        print('sss')

    def desenha_limites_viewport(self):        
        painter = QtGui.QPainter(self)   # cria um painter
        pen = QtGui.QPen(QtGui.Qt.black) # define a caneta como preta
        painter.setPen(pen)              # seta o painter pra usar a caneta definida

        # define os quatro pontos
        ponto1 = QtCore.QPointF(self.dados_vp.xvmin, self.dados_vp.yvmin)
        ponto2 = QtCore.QPointF(self.dados_vp.xvmax, self.dados_vp.yvmin)
        ponto3 = QtCore.QPointF(self.dados_vp.xvmax, self.dados_vp.yvmax)
        ponto4 = QtCore.QPointF(self.dados_vp.xvmin, self.dados_vp.yvmax)

        # defino que uma linha é uma ligação entre dois pontos
        linha1 = QtCore.QLineF(ponto1, ponto2)
        linha2 = QtCore.QLineF(ponto2, ponto3)
        linha3 = QtCore.QLineF(ponto3, ponto4)
        linha4 = QtCore.QLineF(ponto4, ponto1)
        
        # desenho a linha de fato 
        painter.drawLine(linha1)
        painter.drawLine(linha2)
        painter.drawLine(linha3)
        painter.drawLine(linha4)

        # posição do texto 
        qtTextPoint = QtCore.QPointF(290, 25)
        painter.drawText(qtTextPoint, 'VIEWPORT')

    
    def desenha_ponto(self):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtGui.Qt.darkRed)
        painter.setPen(pen)

        for pt in self.dados_obj['pontos']:
            ponto = QtCore.QPointF(pt.x, pt.y)
            painter.drawPoint(ponto)
            self.desenha_coordenadas(painter, ponto)
    
    def desenha_coordenadas(self, painter, ponto):
        if HABILITA_COORDENADAS:
            x = ponto.x()
            y = ponto.y()
            coordenada_ponto = QtCore.QPointF(x + 5, y + 10)
            painter.drawText(coordenada_ponto, f'({x}, {y})')