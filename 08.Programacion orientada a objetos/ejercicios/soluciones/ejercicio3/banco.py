from cuenta_bancaria import CuentaBancaria

class Banco:
    __cuentas : dict
    
    def __init__(self) -> None:
        self.__cuentas = {}
        
    def get_cuentas(self) -> list:
        return self.__cuentas

    def set_cuentas(self, value:dict):
        self.__cuentas = value.copy()
    
    def crear_cuenta(self, cuenta: CuentaBancaria) -> None:
        self.__cuentas.update({cuenta.get_numero_cuenta() : cuenta})
    
    