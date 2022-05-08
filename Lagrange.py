from sympy import *
from math import *
import cmath
from tabulate import tabulate

x = Symbol('x')

def tolerancia(cifras):
	return 0.5*pow(10, 2-cifras)


def errorAproximacion(valorActual, valorAnterior):
	try:
		return abs((valorActual - valorAnterior)/(valorActual))*100
	except:
		return -1



# comprobar que los datos ingresados sean corectos 
#----------------------------------------------------------#

# def datosLagrange(lista):
	
# 	try:
# 		lista = ([float(x) for x in lista.split(',')])
# 	except:
# 		return -1
# 	return lista


# valorx = (input("Valores de x separados por comas \n"))
# valory = (input("Valores de y separados por comas \n"))
# valorPunto = (input("Punto a evaluar"))

# listaX = datosLagrange(valorx)
# listaY = datosLagrange(valory)
# punto = valorPunto

#-----------------------------------------------------------#



def lagrange(listaX,listaY,punto):
	tabla = []
	tabla.append(["Polinomio","Respuesta"])
	length = len(listaX)
	polinomio = 0
	
	for i in range(length):
		termino = 1

		for j in range(length):

			if i != j:
				termino *= (x-listaX[j])/(listaX[i] - listaX[j])

		polinomio += termino*listaY[i]	

	polinomio = expand(polinomio)
	respuesta = polinomio.evalf(subs={x: punto})

	tabla.append([polinomio,respuesta])
	return tabla


listaX = [0, 0.2, 0.3, 0.4]
listaY = [1, 1.6, 1.7, 2.0]

a = lagrange(listaX, listaY, 0.25)

print(tabulate(a,headers="firstrow",tablefmt="fancy_grid",floatfmt=".3f",numalign="center"))