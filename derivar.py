
import math
from sympy import *
from tabulate import tabulate

##Recibe un string
##Devuelve un string
def derivar(funcion):
    x,y,z,e=symbols('x y z e')
    funcion=simplify(funcion).subs(e,math.e)
    derivada=diff(funcion)
    return str(derivada)
