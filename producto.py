# producto.py

class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre  # Nombre del producto
        self._precio = precio   # Precio del producto
        self._stock = stock     # Stock disponible del producto

    def obtener_precio(self):
        return self._precio  # Retorna el precio del producto

    def mostrar_info(self):
        # Muestra información básica del producto en un solo renglón
        return f"Producto: {self._nombre} || Precio: ${int(self._precio)} || Stock: {self._stock}"

    def hay_stock(self, cantidad):
        return self._stock >= cantidad  # Verifica si hay suficiente stock

    def reducir_stock(self, cantidad):
        if self.hay_stock(cantidad):
            self._stock -= cantidad  # Reduce el stock
            return True
        return False


class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela, stock):
        super().__init__(nombre, precio, stock)  # Inicializa atributos de Producto
        self._talla = talla                     # Talla de la ropa
        self._tipo_tela = tipo_tela             # Tipo de tela de la ropa

    def mostrar_info(self):
        # Muestra información de la ropa en un solo renglón
        return (f"{super().mostrar_info()} || Talla: {self._talla} || Tipo de Tela: {self._tipo_tela}")


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_cuello, stock):
        super().__init__(nombre, precio, talla, tipo_tela, stock)  # Inicializa atributos de Ropa
        self._tipo_cuello = tipo_cuello                           # Tipo de cuello de la camisa

    def mostrar_info(self):
        # Muestra información específica de la camisa en un solo renglón
        return (f"{super().mostrar_info()} || Tipo de Cuello: {self._tipo_cuello}")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, largo, stock):
        super().__init__(nombre, precio, talla, tipo_tela, stock)  # Inicializa atributos de Ropa
        self._largo = largo                                       # Largo del pantalón

    def mostrar_info(self):
        # Muestra información específica del pantalón en un solo renglón
        return (f"{super().mostrar_info()} || Largo: {self._largo}")


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_material, stock):
        super().__init__(nombre, precio, talla, tipo_material, stock)  # Inicializa atributos de Ropa

    def mostrar_info(self):
        # Muestra información específica del zapato en un solo renglón
        return f"{super().mostrar_info()}"