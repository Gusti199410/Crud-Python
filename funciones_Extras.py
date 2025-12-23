def validar_Numeros_Reales(numero):
    try:
        if float(numero) > 0:
            return True
    except:
        return False