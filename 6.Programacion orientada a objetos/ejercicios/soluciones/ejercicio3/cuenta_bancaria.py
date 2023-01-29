
class CuentaBancaria:
    __nombre_titular : str
    __numero_cuenta : int
    __saldo :  int
    
    def __init__(self, nombre_titular, numero_cuenta, saldo) -> None:
        self.__nombre_titular = nombre_titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        
    @property
    def nombre_titular(self):
        return self.__nombre_titular

    @nombre_titular.setter
    def nombre_titular(self, value):
        self.__nombre_titular = value
        
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, value):
        self.__numero_cuenta = value
        
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value
        
    def depositar(self, cantidad:int) -> None:
        self.saldo = self.saldo + cantidad
    
    def retirar(self, cantidad:int) -> None:
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad
        else:
            print('No hay suficiente saldo en la cuenta.')
    