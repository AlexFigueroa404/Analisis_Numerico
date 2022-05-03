import cmath
import math
from sympy import *
from tabulate import tabulate

x,e= symbols('x e')

def dif_divididas(fx, x0, x1, x2, x3, x4, x5, y0, y1, y2, y3, y4, y5, grado, interpo):
    resultado = []
    resultado.append(["X",x0, x1, x2, x3, x4, x5])
    b0, b1, b2, b3, b4, b5, = 0, 0, 0, 0, 0, 0
    if type(fx)==int:
        resultado.append(["Y",y0, y1, y2, y3, y4, y5])
        #fila-columna
        p23=((y1-y0)/(x1-x0))
        p33=((y2-y1)/(x2-x1))
        p34=((p33-p23)/(x2-x0)) ##
        p43=((y3-y2)/(x3-x2))
        p44=((p43-p33)/(x3-x1))
        p45=((p44-p34)/(x3-x0))
        p53=((y4-y3)/(x4-x3))
        p54=((p53-p43)/(x4-x2))
        p55=((p54-p44)/(x4-x1))
        p56=((p55-p45)/(x4-x0))
        p63=((y5-y4)/(x5-x4))
        p64=((p63-p53)/(x5-x3))
        p65=((p64-p54)/(x5-x2))
        p66=((p65-p55)/(x5-x1))
        p67=((p66-p56)/(x5-x0))


        b0=y0
        b1=p23
        b2=p34
        b3=p45
        b4=p56
        b5=p67
    else:
        fx=simplify(fx)
        y0=fx.subs(x,x0).subs(e,math.e)
        y1=fx.subs(x,x1).subs(e,math.e)
        y2=fx.subs(x,x2).subs(e,math.e)
        y3=fx.subs(x,x3).subs(e,math.e)
        y4=fx.subs(x,x4).subs(e,math.e)
        y5=fx.subs(x,x5).subs(e,math.e)
        resultado.append(["Y",y0, y1, y2, y3, y4, y5])
        #fila-columna
        p23=((y1-y0)/(x1-x0))
        p33=((y2-y1)/(x2-x1))
        p34=((p33-p23)/(x2-x0)) ##
        p43=((y3-y2)/(x3-x2))
        p44=((p43-p33)/(x3-x1))
        p45=((p44-p34)/(x3-x0))
        p53=((y4-y3)/(x4-x3))
        p54=((p53-p43)/(x4-x2))
        p55=((p54-p44)/(x4-x1))
        p56=((p55-p45)/(x4-x0))
        p63=((y5-y4)/(x5-x4))
        p64=((p63-p53)/(x5-x3))
        p65=((p64-p54)/(x5-x2))
        p66=((p65-p55)/(x5-x1))
        p67=((p66-p56)/(x5-x0))


        b0=y0
        b1=p23
        b2=p34
        b3=p45
        b4=p56
        b5=p67

    if grado == 1:
        polinomio = b0 + b1 * (x - x0)
        resultado.append(["b",b0])
    elif grado == 2:
        polinomio = b0 + b1 * (x - x0) + (b2 * expand((x - x0) * (x - x1)))
        resultado.append(["b",b0, b1, b2])
    elif grado == 3:
        polinomio = b0 + b1 * (x - x0) + (b2 * expand((x - x0) * (x - x1))) + (
                    b3 * expand((x - x0) * (x - x1) * (x - x2)))
        resultado.append(["b",b0, b1, b2, b3])
    elif grado == 4:
        polinomio = b0 + b1 * (x - x0) + (b2 * expand((x - x0) * (x - x1))) + (
                    b3 * expand((x - x0) * (x - x1) * (x - x2))) + (
                                b4 * expand((x - x0) * (x - x1) * (x - x2) * (x - x3)))
        resultado.append(["b",b0, b1, b2, b3, b4])
    elif grado == 5:
        polinomio = b0 + b1 * (x - x0) + (b2 * expand((x - x0) * (x - x1))) + (
                    b3 * expand((x - x0) * (x - x1) * (x - x2))) + (
                                b4 * expand((x - x0) * (x - x1) * (x - x2) * (x - x3))) + (
                                b5 * expand((x - x0) * (x - x1) * (x - x2) * (x - x3) * (x - x4)))
        resultado.append(["b",b0, b1, b2, b3, b4, b5])

    interpolacion = polinomio.subs(x, interpo)
    if type(interpo) != 0:
        resultado.append(["Polinomio", "Interpolacion"])
        resultado.append([polinomio, interpolacion])
    else:
        resultado.append([polinomio])

    return resultado
lista = []
lista = dif_divididas(0, -2, -1, 0, 2, 3, 6, -18, -5, -2, -2, 7, 142, 5, 1.5)

print(tabulate(lista,headers = ["0", "1", "2", "3","4",'5']))