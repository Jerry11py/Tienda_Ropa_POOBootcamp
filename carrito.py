# carrito.py

class Carrito:
    def __init__(self):
        self._productos = {}  # Diccionario para almacenar los productos y sus cantidades

    def agregar_producto(self, producto, cantidad):
        if producto.hay_stock(cantidad):
            producto.reducir_stock(cantidad)  # Reduce el stock del producto
            if producto in self._productos:
                self._productos[producto] += cantidad  # Suma la cantidad si ya existe
            else:
                self._productos[producto] = cantidad  # Agrega el producto al carrito
            print(f"\nProducto agregado al carrito: {producto._nombre} x {cantidad}.")  # Añadido \n para espacio
        else:
            print(f"No hay suficiente stock para {producto._nombre}. Solo hay {producto._stock} en stock.")

    def calcular_total(self):
        # Calcula el total de los productos en el carrito
        total = sum(producto.obtener_precio() * cantidad for producto, cantidad in self._productos.items())
        return total

    def mostrar_resumen(self):
        # Muestra un resumen de los productos en el carrito y el total
        resumen = "Resumen de compra:\n"
        for producto, cantidad in self._productos.items():
            resumen += (f"- {producto.mostrar_info()} || Cantidad: {cantidad}\n")
        resumen += f"Total a pagar: ${int(self.calcular_total())}"  # Muestra el total sin decimales
        return resumen
