from cuenta_bancaria import CuentaBancaria

class Banco:
    __cuentas : dict
    
    def __init__(self) -> None:
        self.__cuentas = {}
        
    @property
    def cuentas(self):
        return self.__cuentas

    @cuentas.setter
    def cuentas(self, value:dict):
        self.__cuentas = value.copy()
    
    def crear_cuenta(self, cuenta: CuentaBancaria) -> None:
        self.cuentas.update({cuenta.numero_cuenta : cuenta})
    
    