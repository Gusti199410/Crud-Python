
import sqlite3
from typing import final
import pandas as pd
import tabulate
from base_de_datos import agregar_producto
from colorama import Fore, Back, Style, init
from funciones_Extras import validar_Numeros_Reales
import os
from  tabulate import tabulate 

init(autoreset=True)


def cargar_datos_producto(conexion):
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
        if nombre.isalpha():
            break
        else:
            print(Fore.RED +"El nombre del producto debe contener solo letras"+ Style.RESET_ALL)
    while True:
        descripcion = input("Ingrese la descripcion del producto: ").strip().capitalize()
        if descripcion.isalpha():
            break
        else:
            print(Fore.RED +"La descripcion del producto debe contener solo letras"+ Style.RESET_ALL)
    while True:
        cantidad = input("Ingrese la cantidad del producto: ").strip().capitalize()
        if cantidad.isdigit():
            cantidad = int(cantidad)
            break
        else:
            print(Fore.RED +"La cantidad del producto debe ser un numero"+ Style.RESET_ALL)
    while True:
        precio_Producto = input("Ingrese el precio del producto: ").strip().capitalize()
        if validar_Numeros_Reales(precio_Producto):
            precio_Producto = float(precio_Producto)
            break
        else:
            print(Fore.RED +"El precio del producto debe ser un numero"+ Style.RESET_ALL)
    while True:
        categoria = input("Ingrese la categoria del producto: ").strip().capitalize()
        if categoria.isalpha():
            break
        else:
            print(Fore.RED +"La categoria del producto debe contener solo letras"+ Style.RESET_ALL)
    agregar_producto(conexion, nombre, descripcion, cantidad, precio_Producto, categoria)


def mostrar_Producto(conexion):
    try:
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM inventario")
        productos=cursor.fetchall()
        print(tabulate(productos,headers=["ID","NOMBRE","DESCRIPCION","CANTIDAD","PRECIO","CATEGORIA"], tablefmt="grid"))
        input("...")
        os.system("cls")
        while True:
            exportar=input("DESEA EXPORTARLO A UN CSV (SI/NO) ").strip().capitalize()
            if exportar =="Si":
                columnas=["ID","NOMBRE","DESCRIPCION","CANTIDAD","PRECIO","CATEGORIA"]
                df=pd.DataFrame(productos,columns=columnas)
                df.to_csv("ListaProductos.csv",sep=";",index=False)
                print("Guardado exitosamente")
                input("...")
                os.system("cls")
                return
            elif exportar=="No":
                os.system("cls")
                break
            else:
                print("INGRESE(SI/NO)")
        

    except sqlite3.Error as e:
        print(Fore.RED+"[ERROR] NO SE PUDO LEER LOS PRODUCTOS"+Style.RESET_ALL)
        print(Fore.RED+str(e)+Style.RESET_ALL)
    finally:
        cursor.close()
        return

def actualizar_Producto(conexion):
    try:
        cursor=conexion.cursor()
        cursor.execute("""SELECT * FROM inventario""")
        productos=cursor.fetchall()
        
        if not productos:
            print("El inventario esta vacio")
            return
        print(tabulate(productos,headers=["ID","NOMBRE","DESCRIPCION","CANTIDAD","PRECIO","CATEGORIA"], tablefmt="grid"))
        while True:
            id_producto=input("INGRESE EL ID que desea modificar(presione (*) para cancerlar): ").strip()
            if id_producto.isdigit():
                break
            elif id_producto=="*":
                os.system("cls")
                return
            else:
                print("[ERROR] INGRESE NUMEROS")
        id_producto=int(id_producto)
        
        while True:
            nuevo_Nombre=input("INGRESE NUEVO NOMBRE: ").strip().capitalize()
            if nuevo_Nombre.isalpha():
                break 
            print("[ERROR]Datos incorrectos")
        
        while True:
            nueva_Descripcion=input("INGRESE DESCRIPCION: ").strip().capitalize()
            if nueva_Descripcion.isalpha():
                break
            print("[ERROR]Datos incorrecto")
        
        while True:
            nueva_cantidad=input("NUEVA CANTIDAD: ").strip().capitalize()
            if nueva_cantidad.isdigit():
                nueva_cantidad=int(nueva_cantidad)
                break 
            print("[ERROR]INGRESE CANTIDAD")
        
        while True:
            nuevo_Precio=input("INGRESE PRECIO: ")
            if validar_Numeros_Reales(nuevo_Precio):
                nuevo_Precio=float(nuevo_Precio)
                break 
            print("[ERROR]INGRESE UN VALOR CORRECTO")
        cursor.execute("""UPDATE inventario SET nombre = ?,descripcion = ?,cantidad = ?,precio_Producto= ?  where id= ?""",(nuevo_Nombre,nueva_Descripcion,nueva_cantidad,nuevo_Precio,id_producto))
        print(Fore.GREEN+f"MODIFICACION EXITOSA DEL ID:{id_producto}"+Style.RESET_ALL)
        #GUARDO CAMBIO
        conexion.commit()
        cursor.execute("""SELECT * FROM inventario where id=?""",(id_producto,))
        producto_Actualizado=cursor.fetchone()
        print(f"ID:{producto_Actualizado[0]}")
        print(f"NOMBRE: {producto_Actualizado[1]}")
        print(f"DESCRIPCION: {producto_Actualizado[2]}")
        print(f"CANTIDAD: {producto_Actualizado[3]}")
        print(f"PRECIO DE PRODUCTO: {producto_Actualizado[4]}")
        print(f"CATEGORIA: {producto_Actualizado[5]}")
        input("--------------------------------------")
    except sqlite3.Error as e:
        print(Fore.RED+"[ERROR]MODIFICAR PRODUCTO"+Style.RESET_ALL)
        print(Fore.RED+str(e)+Style.RESET_ALL)
    finally:
        cursor.close()

        
def buscar_Por_Id(conexion,id):
    try:
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM   inventario where id = ?",(id,))
        producto=cursor.fetchone()
        if not producto:
            print(Fore.RED+"NO HAY PRODUCTO EN LA BASE DE DATOS"+Style.RESET_ALL)
            return
        print("-----PRODUCTO----")
        print(f"ID:{producto[0]}")
        print(f"NOMBRE: {producto[1]}")
        print(f"DESCRIPCION: {producto[2]}")
        print(f"CANTIDAD: {producto[3]}")
        print(f"PRECIO DE PRODUCTO: {producto[4]}")
        print(f"CATEGORIA: {producto[5]}")
        print("--------------------------------------")
    except sqlite3.Error as e:
        print(Fore.RED+"No existe el id"+Style.RESET_ALL)
        print(Fore.RED+str(e)+Style.RESET_ALL)
        return
    
    """BUSCAR DATOS POR CATEGORIA O NOMBRE """
def buscar_por_nombre_o_categoria(conexion,buscar):
    try:
        cursor=conexion.cursor()
        cursor.execute("""SELECT * FROM inventario Where nombre = ? or categoria = ?""",(buscar,buscar,))
        productos=cursor.fetchall()
        print(tabulate(productos,headers=["ID","NOMBRE","DESCRIPCION","CANTIDAD","PRECIO","CATEGORIA"],tablefmt="grid"))
        input("...")
        os.system("cls")
    
    except sqlite3.Error as e:
        print(Fore.RED+"No existe el el nombre o categoria"+Style.RESET_ALL)
        print(Fore.RED+str(e)+Style.RESET_ALL)
        return



  

def eliminar_Producto(conexion):
    try:
        cursor=conexion.cursor()
        
        cursor.execute("SELECT id, nombre, descripcion FROM inventario")
        productos=cursor.fetchall()

        if not productos:
            print("NO HAY PRODCUTOS EN EL INVENTARIO")
            input("...")
            return
        
        print(tabulate(productos,headers=["ID","NOMBRE","DESCRIPCION"],tablefmt="grid"))
        
        while True:
        
            id_Eliminar=input("INGRESE EL ID QUE DESEA ELIMINAR: ").strip()
        
            if id_Eliminar.isdigit():
        
                break
        
            print("INGRESE DATO VALIDOS")
        
        id_Eliminar=int(id_Eliminar)
        
        cursor.execute("SELECT id,nombre FROM inventario WHERE id = ? ",(id_Eliminar,))
        producto_A_Eliminar=cursor.fetchone()
        
        print(f"SEGURO QUE DESEA ELIMINAR PRODUCTO EL PRODUCTO: {producto_A_Eliminar[1]}")
        
        while True:
            
            consulta=input("ingrese SI para confirmar O NO para cancelar: ").strip().capitalize()
            
            if consulta=="Si":
            
                cursor.execute("DELETE FROM inventario where id= ?",(id_Eliminar,))
                print(Fore.GREEN+f"PRODUCTO {producto_A_Eliminar[1]} ELIMINADO EXITOSAMENTE")
                input("presione una tecla para continuar")
                os.system("cls")
                break            
            elif consulta =="No":
            
                print(Fore.RED+"SE CANCELO LA ELIMINACION"+Style.RESET_ALL)
                input("presione una tecla para continuar")
                os.system("cls")
                break
            
            else:
                print("[ERROR](ingrese SI o NO)")

    except sqlite3.Error as e:
        print(Fore.RED+"[ERROR]"+Style.RESET_ALL)
        print(Fore.RED+str(e)+Style.RESET_ALL)
               
    

def reporte_Producto(conexion):
    try:
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM inventario")
        productos=cursor.fetchall()
        if not productos:
            print("NO HAY PRODUCTOS...")
            input("presione una tecla para continuar...")
            os.system("cls")
            return
        while True:
            cantidad=input("INGRESE CANTIDAD DE PRODUCTO: ")
            if cantidad.isdigit():
                cantidad=int(cantidad)
                break 
            print("[ERROR]Ingrese dato valido")
        cursor.execute("SELECT * FROM inventario WHERE cantidad <= ?",(cantidad,))
        productos=cursor.fetchall()
        print(tabulate(productos,headers=["ID","PRODUCTO","DESCRIPCION","CANTIDAD","PRECIO","CATEGORIA"],tablefmt="grid"))
        while True:
            exportar=input("Desea exportarlo a csv(si o no): ").strip().capitalize()
            if exportar == "Si":
                titulos=["ID","NOMBRE","DESCRIPCION","CANTIDAD", "PRECIO", "CATEGORIA"]
                df=pd.DataFrame(productos,columns=titulos)
                df.to_csv("reporte_Productos.csv",sep=";",index=False)
                print("Exportado exitosamente")
                input("...")
                os.system("cls")
                return
            elif exportar=="No":
                input("Cancelado")
                os.system("cls")
                return
            else:
                print("DATO INVALIDO")
    
    except sqlite3.Error as e:
        print(Fore.RED+"[ERROR]"+Style.RESET_ALL)
        print(Fore.RED+str(e)+Style.RESET_ALL)
        input("...")
        os.system("cls")

            
    