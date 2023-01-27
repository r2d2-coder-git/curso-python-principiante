import utilidades

def formatear_texto(cadena:str, formato) -> str:
    if formato == 'minusculas':
        return utilidades.minusculas(cadena)
    elif formato == 'mayusculas':
        return utilidades.mayusculas(cadena)
    return 'Formato invalido.'