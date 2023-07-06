import numpy as np
from Cliente import *
from Funciones import *
arreglo=np.full((10,10),'---')
lista_Cliente = []
ciclo =True
llenar(arreglo)


def AgregarClienteConcierto(lista_Cliente,num_asiento):
    c = Cliente()
    c.rut = (input("ingrese su rut:"))
    c.nombre = input("Ingrese nombre:")
    c.apellido = input("Ingrese Apellido")
    c.num_asiento = num_asiento
    if num_asiento>=1 and num_asiento<=20:
        c.valor = 100000
    if num_asiento>=21 and num_asiento<=50:
        c.valor = 80000
    if num_asiento>=51 and num_asiento<=100:
        c.valor = 50000
    lista_Cliente.append(c)




def ComprarClienteConcierto(arreglo,lista_Cliente):
    try:
        ubicaciones = int(input("Ingrese Ubicaciones(1-100):"))
        if ubicaciones>=1 and ubicaciones<=5:
            compra=0
            while compra<ubicaciones:
                mostrarUbicaciones(arreglo)
                num_asiento = int(input("numero Asiento:"))
                if num_asiento>=1 and num_asiento<=100:
                    disponible = ComprobarAsiento(arreglo,num_asiento)
                    if disponible == True:
                        AgregarClienteConcierto(lista_Cliente,num_asiento)
                        Comprar(arreglo,num_asiento)
                        compra = compra + 1
                    else:
                        print("no disponible")
                else:
                    print("Opcion invalida")
        else:
            print("ubicaciones entre 1 y 100")
    except BaseException as error:
        print(f"error{error}")



def salir():
    print("salio")
    return False
def listarClientes(lista_Cliente):
   for c in lista_Cliente:
        print(f"nombre:{c.nombre} valor:{c.valor} puesto{c.num_asiento}")
def totales(arreglo):
    p = 0
    g = 0
    s = 0
    tot_p=0
    tot_g=0
    tot_s=0
    for cl in lista_Cliente:
        if int(cl.valor) == 100000:
            p = p + 1
            tot_p = tot_p + 100000
        if int(cl.valor) == 80000:
            g = g + 1
            tot_g = tot_g + 80000
        if int(cl.valor) == 50000:
            s = s + 1
            tot_s + tot_s + 50000
    print(f"platinum: cantidad{p} total:{tot_p}")
    print(f"gold    : cantidad{g} total:{tot_g}")
    print(f"silver  : cantidad{s} total:{tot_s}")






while ciclo:

    print("Concierto")
    print("---------------------------------")
    print("1) Comprar entradas")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver listado de asistentes")
    print("4) Mostrar ganancias totales")
    print("5) Salir")
    try:
        op=int(input("seleccione:"))
        match op:
            case 1:
                ComprarClienteConcierto(arreglo,lista_Cliente)
            case 2:
                mostrarUbicaciones(arreglo)
            case 3:
                listarClientes(lista_Cliente)
            case 4:
                totales(lista_Cliente)
            case 5:
                ciclo = salir
    except BaseException as error:
        print(f"error{error}")
