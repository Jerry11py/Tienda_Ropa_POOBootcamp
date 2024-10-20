# producto.py

class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Nombre del producto
        self._precio = precio   # Precio del producto

    def obtener_precio(self):
        return self._precio  # Retorna el precio del producto

    def mostrar_info(self):
        # Muestra información básica del producto, sin decimales
        return f"Producto: {self._nombre}, Precio: ${int(self._precio)}"


class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)  # Inicializa atributos de Producto
        self._talla = talla                 # Talla de la ropa
        self._tipo_tela = tipo_tela         # Tipo de tela de la ropa

    def mostrar_info(self):
        # Muestra información de la ropa, incluyendo atributos específicos
        return f"{super().mostrar_info()}, Talla: {self._talla}, Tipo de Tela: {self._tipo_tela}"


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_cuello):
        super().__init__(nombre, precio, talla, tipo_tela)  # Inicializa atributos de Ropa
        self._tipo_cuello = tipo_cuello                     # Tipo de cuello de la camisa

    def mostrar_info(self):
        # Muestra información específica de la camisa
        return f"{super().mostrar_info()}, Tipo de Cuello: {self._tipo_cuello}"


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, largo):
        super().__init__(nombre, precio, talla, tipo_tela)  # Inicializa atributos de Ropa
        self._largo = largo                                 # Largo del pantalón

    def mostrar_info(self):
        # Muestra información específica del pantalón
        return f"{super().mostrar_info()}, Largo: {self._largo}"


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_material):
        super().__init__(nombre, precio, talla, tipo_material)  # Inicializa atributos de Ropa

    def mostrar_info(self):
        # Muestra información específica del zapato
        return f"{super().mostrar_info()}"
