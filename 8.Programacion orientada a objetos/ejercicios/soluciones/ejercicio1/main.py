from concesionaria import Concesionaria,Vehiculo


concesionaria = Concesionaria()
bmw = Vehiculo('bmw','X4',2020,'negro')
ferrari = Vehiculo('ferrari','el mejor',2023,'rojo')

concesionaria.agregar_vehiculo(bmw)
concesionaria.agregar_vehiculo(ferrari)

print(concesionaria.inventario_coches)