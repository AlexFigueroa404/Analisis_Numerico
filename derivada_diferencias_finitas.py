import cmath
import math
from sympy import *
from tabulate import tabulate


def formulas(tipo,num_derivada,Y_4,Y_3,Y_2,Y_1,Y0,Y1,Y2,Y3,Y4,h):
    if(tipo==1):
        if(num_derivada==1):
            prim_dif_derivada=(Y1-Y0)/h
            seg_dif_derivada=(-Y2+(4*Y1)-(3*Y0))/(2*h)
        elif(num_derivada==2):
            prim_dif_derivada=(Y2-(2*Y1)+Y0)/(h**2)
            seg_dif_derivada=(-Y3+(4*Y2)-(5*Y1)+(2*Y0))/(h**2)
        elif(num_derivada==3):
            prim_dif_derivada=(Y3-(3*Y2)+(3*Y1)-Y0)/(2*(h**3))
            seg_dif_derivada=((-3*Y4)+(14*Y3)-(24*Y2)+(18*Y1)-(5*Y0))/(2*(h**3))
    elif(tipo==2):
        if(num_derivada==1):
            prim_dif_derivada=(Y0-Y_1)/h
            seg_dif_derivada=(3*Y0-(4*Y_1)+Y_2)/(2*h)
        elif(num_derivada==2):
            prim_dif_derivada=(Y0-2*Y_1+Y_2)/(h**2)
            seg_dif_derivada=(2*Y0-5*Y_1+4*Y_2-Y_3)/(h**2)
        elif(num_derivada==3):
            prim_dif_derivada=(Y0-3*Y_1+3*Y_2-Y_3)/(2*(h**3))
            seg_dif_derivada=(5*Y0-18*Y_1+24*Y_2-14*Y_3+3*Y_4)/(2*(h**3))
    elif(tipo==3):
        if(num_derivada==1):
            prim_dif_derivada=(Y1-Y_1)/(2*h)
            seg_dif_derivada=(-Y2+(8*Y1)-(8*Y_1)+Y_2)/(12*h)
        elif(num_derivada==2):
            prim_dif_derivada=(Y1-(2*Y0)+Y_1)/(h**2)
            seg_dif_derivada=(-Y2+(16*Y1)-(30*Y0)+(16*Y_1)-(Y_2))/(12*(h**2))
        elif(num_derivada==3):
            prim_dif_derivada=(Y2-2*Y1+2*Y_1-Y_2)/(2*(h**3))
            seg_dif_derivada=(-Y3+8*Y2-13*Y1+13*Y_1-8*Y_2+Y_3)/(8*(h**3))
    return [prim_dif_derivada,seg_dif_derivada]

def errores_fun(funcion,deriv_aprox,num_deriv,X0,funcion_tabla):
    x,e= symbols('x e')
    if(num_deriv==1):
        Ev=abs(diff(funcion.subs(e,math.e)).subs(x,X0)-deriv_aprox) if funcion_tabla==2 else abs(funcion-deriv_aprox)
        Er=abs(Ev/diff(funcion.subs(e,math.e)).subs(x,X0)) if funcion_tabla==2 else abs(Ev-funcion)
        Er_porc=Er*100
        return [Ev,Er,Er_porc]
    elif(num_deriv==2):
        Ev=abs(diff(diff(funcion.subs(e,math.e))).subs(x,X0)-deriv_aprox) if funcion_tabla==2 else abs(funcion-deriv_aprox)
        Er=abs(Ev/diff(diff(funcion.subs(e,math.e))).subs(x,X0)) if funcion_tabla==2 else abs(Ev-funcion)
        Er_porc=Er*100
        return [Ev,Er,Er_porc]
    elif(num_deriv==3):
        Ev=abs(diff(diff(diff(funcion.subs(e,math.e)))).subs(x,X0)-deriv_aprox) if funcion_tabla==2 else abs(funcion-deriv_aprox)
        Er=abs(Ev/diff(diff(diff(funcion.subs(e,math.e)))).subs(x,X0)) if funcion_tabla==2 else abs(Ev-funcion)
        Er_porc=Er*100
        return [Ev,Er,Er_porc]


def derivada_diferencias_finitas():

    resultados=[]
    x,e= symbols('x e')
    num_derivada=int(input("Que numero de derivada quiere?\n"))
    funcion_tabla=int(input("Usara tabla o funcion? 1.Tabla 2.Funcion\n"))
    if(funcion_tabla==2):
        funcion=input("Escriba la funcion\n")
        X0=float(input("Escriba el valor de X0\n"))
        h=float(input("Escriba el valor de h\n"))
        tipo=int(input("Escriba el tipo de diferencia: 1.Hacia delante 2.Hacia atras 3.Centradas\n"))
        X_4,X_3,X_2,X_1,X1,X2,X3,X4=X0-(4*h),X0-(3*h),X0-(2*h),X0-h,X0+h,X0+(2*h),X0+(3*h),X0+(4*h)
        funcion=simplify(funcion)
        Y_4,Y_3,Y_2,Y_1,Y0,Y1,Y2,Y3,Y4=funcion.subs(x,X_4).subs(e,math.e),funcion.subs(x,X_3).subs(e,math.e),funcion.subs(x,X_2).subs(e,math.e),funcion.subs(x,X_1).subs(e,math.e),funcion.subs(x,X0).subs(e,math.e),funcion.subs(x,X1).subs(e,math.e),funcion.subs(x,X2).subs(e,math.e),funcion.subs(x,X3).subs(e,math.e),funcion.subs(x,X4).subs(e,math.e)

        respuestas=formulas(tipo,num_derivada,Y_4,Y_3,Y_2,Y_1,Y0,Y1,Y2,Y3,Y4,h)
        respuestas[0]=simplify(respuestas[0])

        errores=errores_fun(funcion,respuestas[0],num_derivada,X0,2)

        respuestas[1]=simplify(respuestas[1])

        errores1=errores_fun(funcion,respuestas[1],num_derivada,X0,2)

        resultados.append(["Orden dos" if tipo==3 else "Primera diferencia",respuestas[0],errores[0],errores[1],errores[2]])
        resultados.append(["Orden cuatro" if tipo==3 else "Segunda diferencia",respuestas[1],errores1[0],errores1[1],errores1[2]])
        print(tabulate(resultados,headers=["Derivada","Error verdadero","Error relativo","Error relativo(%)"],tablefmt="fancy_grid"))

    elif(funcion_tabla==1):
        tipo=int(input("Escriba el tipo de diferencia: 1.Hacia delante 2.Hacia atras 3.Centradas\n"))
        lista_x=input("Escriba los valores de X separados por comas\n")
        lista_y=input("Escriba los valores de Y separados por comas\n")
        lista_x.replace(" ","")
        lista_y.replace(" ","")
        mismo_esp=True
        lista_x=lista_x.split(sep=',')
        lista_y=lista_y.split(sep=',')
        valor1=0
        h=0
        ##Validar espaciado
        for i in range(len(lista_x)-1):
            valor=round(float(lista_x[i+1])-float(lista_x[i]),5)
            if(valor==valor1 or i==0):
                valor1=valor
                h=valor
            else:
                mismo_esp=False
                print("Los valores de x no tienen el mismo espaciado entre si")
                break
        esta=False
        while(esta==False):
            X0=input("Escribe el valor de X0\n")
            valor_derivada=float(input("Escriba el valor de f'(X0) para calcular el error relativo\n"))
            try:
                posicion=lista_x.index(X0)
                esta=True
            except:
                print("Ese valor no esta en la lista antes dada")
        if(mismo_esp==True):
        
            Y_4,Y_3,Y_2,Y_1,Y0,Y1,Y2,Y3,Y4=0,0,0,0,0,0,0,0,0
            if(tipo==3):
                try:
                    Y0=float(lista_y[posicion])
                    Y_1=float(lista_y[posicion-1])
                    Y1=float(lista_y[posicion+1])
                    Y_2=float(lista_y[posicion-2])
                    Y2=float(lista_y[posicion+2])
                    Y_3=float(lista_y[posicion-3])
                    Y3=float(lista_y[posicion+4])
                except:
                    None
            elif(tipo==2):
                try:
                    Y0=float(lista_y[posicion])
                    Y_1=float(lista_y[posicion-1])
                    Y_2=float(lista_y[posicion-2])
                    Y_3=float(lista_y[posicion-3])
                    Y_4=float(lista_y[posicion-4])
                except:
                    None
            elif(tipo==1):
                try:
                    Y0=float(lista_y[posicion])
                    Y1=float(lista_y[posicion+1])
                    Y2=float(lista_y[posicion+2])
                    Y3=float(lista_y[posicion+3])
                    Y4=float(lista_y[posicion+4])
                except:
                    None
            respuestas=formulas(tipo,num_derivada,Y_4,Y_3,Y_2,Y_1,Y0,Y1,Y2,Y3,Y4,h)
            respuestas[0]=simplify(respuestas[0])

            errores=errores_fun(valor_derivada,respuestas[0],num_derivada,X0,1)

            respuestas[1]=simplify(respuestas[1])

            errores1=errores_fun(valor_derivada,respuestas[1],num_derivada,X0,1)

            resultados.append(["Orden dos" if tipo==3 else "Primera diferencia",respuestas[0],errores[0],errores[1],errores[2]])
            try:
                resultados.append(["Orden cuatro" if tipo==3 else "Segunda diferencia",respuestas[1],errores1[0],errores1[1],errores1[2]])
            except:
                None
            print(tabulate(resultados,headers=["Derivada","Error verdadero","Error relativo","Error relativo(%)"],tablefmt="fancy_grid"))
derivada_diferencias_finitas()