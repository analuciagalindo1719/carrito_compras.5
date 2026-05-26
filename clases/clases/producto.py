class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio  # Encapsulado
        self.__stock = stock    # Encapsulado

    # Métodos para ver los datos protegidos
    def obtener_precio(self):
        return self.__precio

    def obtener_stock(self):
        return self.__stock