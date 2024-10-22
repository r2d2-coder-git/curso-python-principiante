
class CuentaBancaria:
    __nombre_titular : str
    __numero_cuenta : int
    __saldo :  int
    
    def __init__(self, nombre_titular, numero_cuenta, saldo) -> None:
        self.__nombre_titular = nombre_titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        
    def get_nombre_titular(self) -> str:
        return self.__nombre_titular
    
    def set_nombre_titular(self, value):
        self.__nombre_titular = value
        
    def get_numero_cuenta(self) -> int:
        return self.__numero_cuenta

    def set_numero_cuenta(self, value):
        self.__numero_cuenta = value
        
    def get_saldo(self) -> int:
        return self.__saldo

    def set_saldo(self, value):
        self.__saldo = value
        
    def depositar(self, cantidad:int) -> None:
        self.__saldo = self.__saldo + cantidad
    
    def retirar(self, cantidad:int) -> None:
        if self.__saldo >= cantidad:
            self.__saldo = self.__saldo - cantidad
        else:
            print('No hay suficiente saldo en la cuenta.')
    