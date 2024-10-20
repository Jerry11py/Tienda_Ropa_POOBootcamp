# tienda.py

from producto import Camisa, Pantalon, Zapato
from carrito import Carrito

class Tienda:
    def __init__(self):
        # Lista de productos disponibles en la tienda
        self._productos_disponibles = [
            Camisa("Camisa de Algodón", 20.00, "M", "Algodón", "Clásico", 10),  # Stock inicial
            Pantalon("Pantalón de Mezclilla", 30.00, "L", "Denim", "Corto", 5),  # Stock inicial
            Zapato("Zapato de Cuero", 50.00, "42", "Cuero", 7),                 # Stock inicial
        ]

    def mostrar_productos(self):
        # Muestra los productos disponibles en la tienda
        for i, producto in enumerate(self._productos_disponibles):
            print(f"{i + 1}. {producto.mostrar_info()}\n")  # Añadido \n para el espacio en blanco

    def seleccionar_productos(self):
        carrito = Carrito()  # Crea un nuevo carrito
        while True:
            self.mostrar_productos()  # Muestra los productos disponibles
            seleccion = input("\nSeleccione el número del producto a agregar al carrito (o 'q' para finalizar): ")
            if seleccion.lower() == 'q':
                break  # Termina la selección si el usuario ingresa 'q'
            try:
                indice = int(seleccion) - 1
                if 0 <= indice < len(self._productos_disponibles):
                    cantidad = int(input(f"¿Cuántas unidades de {self._productos_disponibles[indice]._nombre} desea agregar? "))
                    carrito.agregar_producto(self._productos_disponibles[indice], cantidad)  # Agrega el producto al carrito
                else:
                    print("Selección no válida. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        print(carrito.mostrar_resumen())  # Muestra el resumen de la compra
