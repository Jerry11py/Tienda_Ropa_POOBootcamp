class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre  # Nombre del producto
        self._precio = precio  # Precio del producto
        self._stock = stock  # Stock del producto

    def obtener_precio(self):
        return self._precio  # Retorna el precio del producto

    def obtener_stock(self):
        return self._stock  # Retorna el stock del producto

    def hay_stock(self, cantidad):
        return self._stock >= cantidad  # Verifica si hay suficiente stock

    def reducir_stock(self, cantidad):
        self._stock -= cantidad  # Reduce el stock cuando se realiza una compra

    def mostrar_info(self):
        return f"Producto: {self._nombre} || Precio: ${self._precio} || Stock: {self._stock}"


class Ropa(Producto):
    def __init__(self, nombre, precio, stock, talla, tipo_tela):
        super().__init__(nombre, precio, stock)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        return f"{super().mostrar_info()} || Talla: {self._talla} || Tipo de Tela: {self._tipo_tela}"


class Camisa(Ropa):
    def __init__(self, nombre, precio, stock, talla, tipo_tela, tipo_cuello):
        super().__init__(nombre, precio, stock, talla, tipo_tela)
        self._tipo_cuello = tipo_cuello

    def mostrar_info(self):
        return f"{super().mostrar_info()} || Tipo de Cuello: {self._tipo_cuello}"


class Pantalon(Ropa):
    def __init__(self, nombre, precio, stock, talla, tipo_tela, largo):
        super().__init__(nombre, precio, stock, talla, tipo_tela)
        self._largo = largo

    def mostrar_info(self):
        return f"{super().mostrar_info()} || Largo: {self._largo}"


class Zapato(Ropa):
    def __init__(self, nombre, precio, stock, talla, tipo_material):
        super().__init__(nombre, precio, stock, talla, tipo_material)

    def mostrar_info(self):
        return super().mostrar_info()
