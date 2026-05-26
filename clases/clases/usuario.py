class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

# Cliente hereda de Usuario
class Cliente(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.tipo = "Cliente"

# Administrador hereda de Usuario
class Administrador(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.tipo = "Administrador"