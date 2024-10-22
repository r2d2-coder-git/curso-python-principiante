class Producto:
    
    __nombre : str
    __cantidad : int 
    __precio : float
    
    def __init__(self, nombre, cantidad, precio):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
        
    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value
        
    def get_cantidad(self) -> int:
        return self.__cantidad

    def set_cantidad(self, value):
        self.__cantidad = value
    
    def get_precio(self) -> int:
        return self.__precio

    def set_precio(self, value):
        self.__precio = value
    
    def vender(self, cantidad: int) -> bool:
        if self.__cantidad >= cantidad:
         self.__cantidad = self.__cantidad - cantidad
         return True
        else:
            print(f'No hay tantos ejemplares de este producto, solo nos quedan {self.__cantidad}')
            return False
            
    def comprar(self, cantidad: int):
         self.__cantidad = self.__cantidad + cantidad
        
 
class Inventario:
    __productos : list
    __total_ventas : int
    
    def __init__(self) -> None:
        self.__productos = []
        self.__total_ventas = 0
    
    def get_total_ventas(self) -> int:
        return self.__total_ventas

    def set_total_ventas(self, value):
        self.__total_ventas = value
        
    def get_productos(self) -> list:
        return self.__productos

    def set_productos(self, value : list):
        self.__productos = value.copy()
    
    def agregar_producto(self, producto : Producto) -> None:
        self.__productos.append(producto)
    
    def vender_producto(self, producto: Producto, cantidad: int) -> None:
        for producto_inventario in self.__productos:
            if producto_inventario == producto:
                venta_realizada = producto_inventario.vender(cantidad)
        if venta_realizada:
            self.__total_ventas = self.__total_ventas + (producto.get_precio() * cantidad)
            
    def comprar_producto(self, producto: Producto, cantidad: int) -> None:        
        for producto_inventario in self.__productos:
                if producto_inventario == producto:
                    producto_inventario.comprar(cantidad)
                
        
