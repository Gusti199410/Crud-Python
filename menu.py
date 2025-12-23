from ast import While

from pickle import TRUE
from colorama import Fore,Style,init,Back
from producto import *
import os
init(autoreset=True)

def menu_Principal(conexion):
    print(Fore.YELLOW+"\t\tMENU DE OPCIONES: "+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"1-\tCARGAR      PRODUCTO"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"2-\tMOSTRAR     PRODUCTO"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"3-\tACTUALIZAR  PRODUCTO"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"4-\tBUSCAR      PRODUCTO"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"5-\tELIMINAR    PRODUCTO"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"6-\tREPORTE     PRODUCTOS"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+"7-\tSALIR"+Style.RESET_ALL)
    opcion=input(Fore.LIGHTBLUE_EX+"INGRESE UNA OPCION: "+Style.RESET_ALL)
    os.system("cls")
    while True:
        if opcion == "1":
           cargar_datos_producto(conexion)
        elif opcion =="2":
            mostrar_Producto(conexion)
        elif opcion=="3":
            actualizar_Producto(conexion)
        elif opcion =="4":
            buscar=input("INGRESE EL ID, NOMBRE O CATEGORIA:").strip().capitalize()
            if buscar.isdigit():
                buscar=int(buscar)
                buscar_Por_Id(conexion,buscar)
            elif buscar.isalpha():
                buscar_por_nombre_o_categoria(conexion,buscar)
        elif opcion == "5" :
            eliminar_Producto(conexion)
        elif opcion =="6":
            reporte_Producto(conexion)    
        elif opcion =="7":
                conexion.close()
                return              
        print(Fore.YELLOW+"\t\tMENU DE OPCIONES: "+Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX+"1-\tCARGAR      PRODUCTO"+Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX+"2-\tMOSTRAR     PRODUCTO"+Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX+"3-\tACTUALIZAR  PRODUCTO"+Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX+"4-\tBUSCAR      PRODUCTO"+Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX+"5-\tELIMINAR    PRODUCTO"+Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX+"6-\tREPORTE     PRODUCTOS"+Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX+"7-\tSALIR"+Style.RESET_ALL)
        opcion=input(Fore.LIGHTBLUE_EX+"INGRESE UNA OPCION: "+Style.RESET_ALL)
        os.system("cls")
 