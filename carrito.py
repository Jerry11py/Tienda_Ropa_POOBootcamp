class Carrito:
    def __init__(self):
        self._productos = {}  # Diccionario para almacenar productos y sus cantidades

    def agregar_producto(self, producto, cantidad):
        if producto.hay_stock(cantidad):
            if producto in self._productos:
                self._productos[producto] += cantidad
            else:
                self._productos[producto] = cantidad
            producto.reducir_stock(cantidad)
        else:
            print(f"No hay suficiente stock para {producto.mostrar_info()}.")

    def calcular_total(self):
        total = sum(producto.obtener_precio() * cantidad for producto, cantidad in self._productos.items())
        return total

    def mostrar_resumen(self):
        resumen = "Resumen de compra:\n"
        for producto, cantidad in self._productos.items():
            resumen += f"- {producto.mostrar_info()} || Cantidad: {cantidad}\n"
        resumen += f"Total a pagar: ${self.calcular_total()}"
        return resumen
