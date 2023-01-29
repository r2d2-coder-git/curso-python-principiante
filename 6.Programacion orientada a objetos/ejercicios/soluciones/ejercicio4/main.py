from sistema_de_gestion import Empleado,Departamento,Empresa


empleado1 = Empleado('Arturo', 'Lorenzo Hernandez', 24, 'Ingeniero de datos', 50000)
empleado2 = Empleado('Pepe', 'Lorenzo Hernandez', 20, 'Desarrollador Web', 40000)

empleado3 = Empleado('Maria', 'Lorenzo Hernandez', 19, 'Recruiter', 20000)
empleado4 = Empleado('Ana', 'Lorenzo Hernandez', 30, 'Contable', 40000)

departamento1 = Departamento('Tecnologia')

departamento1.agregar_empleado(empleado1)
departamento1.agregar_empleado(empleado2)

departamento2 = Departamento('Recursos Humanos')

departamento2.agregar_empleado(empleado3)
departamento2.agregar_empleado(empleado4)

empresa = Empresa('R2D2 LEARN')

empresa.agregar_departamento(departamento1)
empresa.agregar_departamento(departamento2)

empresa.listar_departamentos()



