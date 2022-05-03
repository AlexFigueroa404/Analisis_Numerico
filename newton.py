
import math
from sympy import *
from tabulate import tabulate

x,e = symbols('x e')

def tolerancia(cifras):
    return 0.5*math.pow(10,2-cifras)

def errorAproximacion(valorActual,valorAnterior):
    return abs((valorActual - valorAnterior)/(valorActual))*100

def derivar(funcion):
    e=symbols('e')
    funcion=simplify(funcion).subs(e,math.e)
    derivada=diff(funcion)
    return str(derivada)


def newton(fx,x0,cifras):
    #Probar convergencia
    fx=simplify(fx)
    deriv=simplify(derivar(fx))
    seg_deriv=simplify(derivar(deriv))

    fx0=fx.subs(x,x0).subs(e,math.e)
    deriv=deriv.subs(x,x0).subs(e,math.e)
    seg_deriv=seg_deriv.subs(x,x0).subs(e,math.e)

    if (abs((fx0*seg_deriv)/(deriv**2))<1):
        iteracion=1

        tabla=[]
        # encabezado = ["Iteracion", "X0", "f(x0)", "f'(X0)","X0+1","Ea"]
        # tabla.append(encabezado)
        Ea=1
        while Ea>tolerancia(cifras):
            fx0=fx.subs(x,x0).subs(e,math.e)
            deriv=deriv.subs(x,x0).subs(e,math.e)
            seg_deriv=seg_deriv.subs(x,x0).subs(e,math.e)

            siguiente_valor=x0-(fx0/deriv)
            Ea=errorAproximacion(siguiente_valor,x0)
            tabla.append([iteracion,x0,fx0,deriv,siguiente_valor,Ea])
            x0=siguiente_valor
            iteracion+=1

    else:
        print("La funcion no converge")
    return tabla
lista=newton("e**(x-1)+x",-0.3,3)
print(tabulate(lista,headers = ["Iteracion", "Xi", "f(Xi)", "f'(Xi)","Xi+1","Ea"],tablefmt="github"))
