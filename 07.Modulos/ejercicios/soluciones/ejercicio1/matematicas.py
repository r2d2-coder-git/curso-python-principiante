def calcular_promedio(numeros: list) -> int:
    suma_total = 0
    for numero in numeros:
        suma_total = suma_total + numero
    return suma_total / len(numeros)