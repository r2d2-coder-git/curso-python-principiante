def comer_manzana_valor(manzanas):
    manzanas -= 1

def comer_manzana_referencia(manzanas):
    manzanas[0] -= 1
    
def main():
    manzanas = 10
    print(f"Antes de pasar manzanas por valor, tengo {manzanas} manzanas.")
    comer_manzana_valor(manzanas)
    print(f"Despues de pasar manzanas por valor, tengo {manzanas} manzanas, NO SE MODIFICA LA VARIABLE.")

#def main():
#    manzanas = [10]
#    print(f"Antes de pasar manzanas por referencia, tengo {manzanas[0]} manzanas.")
#    comer_manzana_referencia(manzanas)
#    print(f"Despues de pasar manzanas por referencia, tengo {manzanas[0]} manzanas, SI SE MODIFICA LA VARIABLE.")

if __name__ == '__main__':
    main()
