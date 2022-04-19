import math
import sympy as sp
from tabulate import tabulate

def fx(x):
    return math.e**(x-1)+x

def tolerancia(cifras):
    return 0.5*math.pow(10,2-cifras)

def errorAproximacion(valorActual,valorAnterior):
    return abs((valorActual - valorAnterior)/(valorActual))*100

def secante(f,X0,X1,cifras):
    valor1=float(X0)
    valor2=float(X1)
    if f(X0)*f(X1)<0:
        iteracion=1
        tabla=[]
        Ea=1
        while Ea>tolerancia(cifras):
            siguiente_valor=valor2-f(valor2)*((valor2-valor1)/(f(valor2)-f(valor1)))
            if(iteracion>1):
                Ea=abs((siguiente_valor-valor1)/siguiente_valor)*100
            else:
                None
            tabla.append([iteracion,valor1,valor2,f(valor1),f(valor2),siguiente_valor,Ea])
            valor1=valor2
            valor2=siguiente_valor
            iteracion+=1
    else:
        print("La funcion no tiene raiz")
    return tabla
lista=secante(fx,-0.5,0,3)
print(tabulate(lista,headers = ["Iteracion", "Xn-1", "Xn", "f(Xn-1)","f(Xn)","Xn+1","Ea"],tablefmt="github"))