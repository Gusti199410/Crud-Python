from base_de_datos import *
from menu import *
from producto import *
init(autoreset=True)
conexion = sqlite3.connect("inventario.db")
crear_base_de_Datos(conexion)
menu_Principal(conexion)
conexion.close()
