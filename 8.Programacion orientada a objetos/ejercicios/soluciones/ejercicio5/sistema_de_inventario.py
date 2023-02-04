class Producto:
    
    __nombre : str
    __cantidad : int 
    __precio : float
    
    def __init__(self, nombre, cantidad, precio):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value
    
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value
    
    def vender(self, cantidad: int) -> bool:
        if self.cantidad >= cantidad:
         self.cantidad = self.cantidad - cantidad
         return True
        else:
            print(f'No hay tantos ejemplares de este producto, solo nos quedan {self.cantidad}')
            return False
            
    def comprar(self, cantidad: int):
         self.cantidad = self.cantidad + cantidad
        
 
class Inventario:
    __productos : list
    __total_ventas : int
    
    def __init__(self) -> None:
        self.__productos = []
        self.__total_ventas = 0
    
    @property
    def total_ventas(self):
        return self.__total_ventas

    @total_ventas.setter
    def total_ventas(self, value):
        self.__total_ventas = value
        
    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self, value : list):
        self.__productos = value.copy()
    
    def agregar_producto(self, producto : Producto) -> None:
        self.productos.append(producto)
    
    def vender_producto(self, producto: Producto, cantidad: int) -> None:
        for producto_inventario in self.productos:
            if producto_inventario == producto:
                venta_realizada = producto_inventario.vender(cantidad)
        if venta_realizada:
            self.total_ventas = self.total_ventas + (producto.precio * cantidad)
            
    def comprar_producto(self, producto: Producto, cantidad: int) -> None:        
        for producto_inventario in self.productos:
                if producto_inventario == producto:
                    producto_inventario.comprar(cantidad)
                
        
