from producto import Camisa, Pantalon, Zapato
from carrito import Carrito

class Tienda:
    def __init__(self):
        self._productos_disponibles = [
            Camisa("Camisa de Algodón", 20.00, 10, "M", "Algodón", "Clásico"),
            Pantalon("Pantalón de Mezclilla", 30.00, 5, "L", "Denim", "Corto"),
            Zapato("Zapato de Cuero", 50.00, 7, "42", "Cuero")
        ]

    def mostrar_productos(self):
        for i, producto in enumerate(self._productos_disponibles):
            print(f"{i + 1}. {producto.mostrar_info()}")

    def seleccionar_productos(self):
        carrito = Carrito()
        while True:
            self.mostrar_productos()
            seleccion = input("\nSeleccione el número del producto a agregar al carrito (o 'q' para finalizar): ")
            if seleccion.lower() == 'q':
                break
            try:
                indice = int(seleccion) - 1
                if 0 <= indice < len(self._productos_disponibles):
                    cantidad = int(input("Ingrese la cantidad: "))
                    carrito.agregar_producto(self._productos_disponibles[indice], cantidad)
                    print("Producto agregado al carrito.\n")
                else:
                    print("Selección no válida. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        print(carrito.mostrar_resumen())
