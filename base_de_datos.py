from nt import system
import sqlite3
from colorama import Fore, Back, Style, init
import os


def crear_base_de_Datos(conexion):
    cursor = conexion.cursor()
    if not os.path.exists("inventario.db"):
        cursor.execute(""" CREATE TABLE IF NOT EXISTS  
        inventario (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio_Producto REAL NOT NULL,
        categoria TEXT NOT NULL)""")
        conexion.commit() # Guardar los cambios en la base de datos
        if cursor.rowcount > 0:
            print(Fore.GREEN + "Base de datos creada correctamente" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error al crear la base de datos" + Style.RESET_ALL)
        
    else:
        print(Fore.YELLOW + "Base de datos ya existe" + Style.RESET_ALL)


def agregar_producto(conexion, nombre, descripcion, cantidad, precio_Producto, categoria):
    try:
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO inventario (nombre, descripcion, cantidad, precio_Producto, categoria)
         VALUES (?, ?, ?, ?, ?)""", (nombre, descripcion, cantidad, precio_Producto, categoria))
        conexion.commit() # Guardar los cambios en la base de datos
        print(Fore.GREEN + "Producto agregado correctamente" + Style.RESET_ALL)
        input("presione una tecla para continuar")
        
    except sqlite3.Error as e:
        print(Fore.RED + "Error al agregar el producto" + Style.RESET_ALL)
        print(Fore.RED + str(e) + Style.RESET_ALL)
    finally:
        os.system("cls")
        return

    

    

