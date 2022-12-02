#cuenta bancaria


class CuentaBancaria:
    def __init__(self,numero_de_cuenta,cantidad):
        self.numero_de_cuenta = numero_de_cuenta
        self.cantidad = cantidad
        self.movimientos= [False]
    def extraer_dinero(self):
        self.movimientos = True

        print("extraccion de dinero de ", self.numero_de_cuenta, self.cantidad)


cuenta = CuentaBancaria("su cuenta :  0012341993", "su saldo es:  50000",)


print (cuenta.numero_de_cuenta)
print(cuenta.cantidad)

cuenta.extraer_dinero()
print(cuenta.movimientos)
