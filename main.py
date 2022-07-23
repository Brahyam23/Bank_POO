class Persona:
    def __init__(self, nombre: str, apellido:str, documento:str,saldo:float=0.0):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.__saldo = saldo
    
    def __str__(self):
        return f"Nombre completo: {self.nombre.capitalize()} {self.apellido.capitalize()} | DNI: {self.documento}"
    
    def get_saldo(self):
        return self.__saldo
    
    def realizar_pago(self,monto:float):
        self.__saldo -= monto
        return f"Se han descontado ${monto} de la cuenta"
    
    def realizar_deposito(self,monto):
        self.__saldo += monto
        return f"Se han depositado ${monto} en la cuenta"

class Banco:
    
    def __init__(self, nombre:str , direccion:str):
        self.__clientes = []
        self.nombre = nombre
        self.direccion = direccion
    
    def __str__(self):
        return f"Este es el banco {self.nombre} y esta ubicado en {self.direccion}"

    def agregar_cliente(self, persona:Persona):
        self.__clientes.append(persona)
        print (f"Se ha agregado el nuevo cliente correctamente")
    
    def eliminar_cliente(self, persona):
        self.__clientes.remove(persona)
        print (f"Se ha eliminado el cliente {self.persona}correctamente")

    def consultar_cuenta_cliente(self, documento:str): #Como buscar elemenmtos en una lista
        for cliente in self.__clientes:
            if cliente.documento == documento:
                return cliente

bancoA = Banco("BBVA","Cuenca 3385")

clienteA = Persona("Brahyam", "Leiva", "95919428", 100000)

bancoA.agregar_cliente(clienteA)

print(bancoA.consultar_cuenta_cliente("95919428"))

# if cliente:
#    print(f"Saldo de {cliente}: ${cliente.get_saldo()}")