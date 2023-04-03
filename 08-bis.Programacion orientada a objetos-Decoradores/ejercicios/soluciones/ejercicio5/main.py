from sistema_de_inventario import Producto, Inventario


producto1 = Producto('Ordenador',10,1000)
producto2 = Producto('Pantalla', 100, 100)
producto3 = Producto('Teclado', 1000,10)

inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

inventario.vender_producto(producto1, 5)


print(f'Ahora quedan {inventario.productos[0].cantidad} del producto {inventario.productos[0].nombre}')
print(f'Tenemos un total de ventas de {inventario.total_ventas} euros.')

inventario.comprar_producto(producto1, 10)

print(f'Ahora quedan {inventario.productos[0].cantidad} del producto {inventario.productos[0].nombre}')
