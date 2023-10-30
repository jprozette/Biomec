"""
Created on Sat Oct 21 16:32:34 2023

@author: Joao Pedro T Rozette
"""


def calcular_coeficiente_angular(x1, y1, x2, y2):
    """
    Calcula o coeficiente angular da reta que passa pelos pontos (x1, y1) e (x2, y2).
    """
    return (y2 - y1) / (x2 - x1)


def calcular_intersecao_x(x1, y1, x2, y2, coef1, coef2):
    """
    Calcula a coordenada x da interseção entre duas retas definidas por (x1, y1) e (x2, y2) com coeficientes angulares coef1 e coef2.
    """
    return ((-coef2 * x2) + y2 + (coef1 * x1) - y1) / (coef1 - coef2)


def calcular_intersecao_y(coef1, x, x1, y1):
    """
    Calcula a coordenada y da interseção de uma reta definida por (x1, y1) com um coeficiente angular coef1 no ponto x.
    """
    return (coef1 * x) - (coef1 * x1) + y1


xcamera1 = float(input("Entre com a coordenada x da câmera 1: "))
ycamera1 = float(input("Entre com a coordenada y da câmera 1: "))
xcamera2 = float(input("Entre com a coordenada x da câmera 2: "))
ycamera2 = float(input("Entre com a coordenada y da câmera 2: "))
xprojecao1 = float(input("Entre com a coordenada x da projeção 1: "))
yprojecao1 = float(input("Entre com a coordenada y da projeção 1: "))
xprojecao2 = float(input("Entre com a coordenada x da projeção 2: "))
yprojecao2 = float(input("Entre com a coordenada y da projeção 2: "))


coef_angular1 = calcular_coeficiente_angular(xcamera1, ycamera1, xprojecao1, yprojecao1)
coef_angular2 = calcular_coeficiente_angular(xcamera2, ycamera2, xprojecao2, yprojecao2)


coord_x_intersecao = calcular_intersecao_x(xcamera1, ycamera1, xcamera2, ycamera2, coef_angular1, coef_angular2)
coord_y_intersecao = calcular_intersecao_y(coef_angular1, coord_x_intersecao, xcamera1, ycamera1)


print(f"A coordenada de interseção x é: {coord_x_intersecao}")
print(f"A coordenada de interseção y é: {coord_y_intersecao}")