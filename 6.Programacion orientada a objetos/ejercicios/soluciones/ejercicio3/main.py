from banco import Banco,CuentaBancaria


cuenta1 = CuentaBancaria('Arturo',39081048,1000000)
cuenta2 = CuentaBancaria('Maria', 34019381,100)

banco = Banco()
banco.crear_cuenta(cuenta1)
banco.crear_cuenta(cuenta2)

print(banco.cuentas)