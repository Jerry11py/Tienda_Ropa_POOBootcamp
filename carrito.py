# carrito.py

class Carrito:
    def __init__(self):
        self._productos = []  # Lista para almacenar los productos del carrito

    def agregar_producto(self, producto):
        self._productos.append(producto)  # Agrega un producto al carrito

    def calcular_total(self):
        # Calcula el total de los productos en el carrito
        total = sum(producto.obtener_precio() for producto in self._productos)
        return total

    def mostrar_resumen(self):
        # Muestra un resumen de los productos en el carrito y el total
        resumen = "Resumen de compra:\n"
        for producto in self._productos:
            resumen += f"- {producto.mostrar_info()}\n"
        resumen += f"Total a pagar: ${int(self.calcular_total())}"  # Muestra el total sin decimales
        return resumen
