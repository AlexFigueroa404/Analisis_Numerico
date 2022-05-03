
import math
from sympy import *
from tabulate import tabulate

##Recibe un string
##Devuelve un string
def derivar(funcion):
    e=symbols('e')
    funcion=simplify(funcion).subs(e,math.e)
    derivada=diff(funcion)
    return str(derivada)

