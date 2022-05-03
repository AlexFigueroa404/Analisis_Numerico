import math
import sympy as sp
from tabulate import tabulate
from sympy import *

x,e = symbols('x e')

def tolerancia(cifras):
    return 0.5*math.pow(10,2-cifras)

def errorAproximacion(valorActual,valorAnterior):
    return abs((valorActual - valorAnterior)/(valorActual))*100


def secante(fx,x0,x1,cifras):
    fx=simplify(fx)
    fx0=fx.subs(x,x0).subs(e,math.e)
    fx1=fx.subs(x,x1).subs(e,math.e)

    if fx0*fx1<0:
        iteracion=1
        tabla=[]
        Ea=1
        while Ea>tolerancia(cifras):
            fx0=fx.subs(x,x0).subs(e,math.e)
            fx1=fx.subs(x,x1).subs(e,math.e)
            siguiente_valor=x1-fx1*((x1-x0)/(fx1-fx0))
            if(iteracion>1):
                Ea=errorAproximacion(siguiente_valor,x0)
            else:
                None
            tabla.append([iteracion,x0,x1,fx0,fx1,siguiente_valor,Ea])
            x0=x1
            x1=siguiente_valor
            iteracion+=1
    else:
        print("La funcion no tiene raiz")
    return tabla
lista=secante("e**(x-1)+x",-0.5,0,3)
print(tabulate(lista,headers = ["Iteracion", "Xn-1", "Xn", "f(Xn-1)","f(Xn)","Xn+1","Ea"],tablefmt="github"))
# ultima_fila=lista.pop()
# print("La raiz es "+str(ultima_fila[5])+" y el error es de "+str(ultima_fila[6]))