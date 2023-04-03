from familia import Familia, Persona

hijo = Persona('Arturo', 'Lorenzo Hernandez', 24)
hermano = Persona('Alvaro', 'Lorenzo Hernandez', 26)
padre = Persona ('Antonio','Lorenzo Alvarez', 58)
madre = Persona('Antonia', 'Perez Hernandez',58)

miembros = [hijo,hermano,padre,madre]
familia = Familia()
for miembro in miembros:
    familia.agregar_miemrbro(miembro)
familia.listar_miembros()