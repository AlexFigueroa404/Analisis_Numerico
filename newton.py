import cmath
import math
import sympy as sp
from tabulate import tabulate

def fx(x):
    return math.e**(x-1)+x
def derivada(x):
    return math.e**(x-1)+1
def seg_derivada(x):
    return math.e**(x-1)
def tolerancia(cifras):
    return 0.5*math.pow(10,2-cifras)

def errorAproximacion(valorActual,valorAnterior):
    return abs((valorActual - valorAnterior)/(valorActual))*100

def newton(f,deriv,seg_deriv,X0,cifras):
    #Probar convergencia
    valor1=float(X0)
    if (abs((f(valor1)*seg_deriv(valor1))/(deriv(valor1)**2))<1):
        iteracion=1

        tabla=[]
        # encabezado = ["Iteracion", "X0", "f(x0)", "f'(X0)","X0+1","Ea"]
        # tabla.append(encabezado)
        Ea=1
        while Ea>tolerancia(cifras):
            siguiente_valor=valor1-(f(valor1)/deriv(valor1))
            Ea=abs((siguiente_valor-valor1)/siguiente_valor)*100
            tabla.append([iteracion,valor1,f(valor1),deriv(valor1),siguiente_valor,Ea])
            valor1=siguiente_valor
            iteracion+=1

    else:
        print("La funcion no converge")
    return tabla
lista=newton(fx,derivada,seg_derivada,-0.3,3)
print(tabulate(lista,headers = ["Iteracion", "Xi", "f(Xi)", "f'(Xi)","Xi+1","Ea"],tablefmt="github"))
