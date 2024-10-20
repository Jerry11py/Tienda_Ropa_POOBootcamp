# Sistema de Compra de Ropa con Stock y Carrito de Compras

Este proyecto es un sistema de compra de ropa basado en consola, que permite a los usuarios seleccionar productos, agregarlos a un carrito, gestionar el stock y mostrar un resumen de la compra. El sistema está diseñado utilizando Programación Orientada a Objetos (POO) en Python.

---

## Estructura del Proyecto

El proyecto está organizado en las siguientes clases:

### 1. **Producto (producto.py)**

Clase base que define los atributos básicos y métodos comunes para todos los productos.

- **Atributos:**
  - `nombre`: Nombre del producto.
  - `precio`: Precio del producto.
  - `stock`: Cantidad disponible en inventario.

- **Métodos:**
  - `obtener_precio()`: Retorna el precio del producto.
  - `mostrar_info()`: Muestra la información del producto (nombre, precio, stock).
  - `hay_stock(cantidad)`: Verifica si hay suficiente stock.
  - `reducir_stock(cantidad)`: Reduce el stock cuando se realiza una compra.

### 2. **Ropa (producto.py)**

Clase derivada de `Producto`, específica para productos de ropa, con atributos adicionales como la `talla` y el `tipo de tela`.

### 3. **Camisa, Pantalon, Zapato (producto.py)**

Clases derivadas de `Ropa`, que añaden características adicionales:

- **Camisa**: Atributo adicional `tipo_cuello`.
- **Pantalon**: Atributo adicional `largo`.
- **Zapato**: Atributo adicional `tipo_material`.

### 4. **Carrito (carrito.py)**

Clase encargada de gestionar los productos seleccionados por el usuario.

- **Atributos:**
  - `productos`: Diccionario que almacena los productos seleccionados y sus cantidades.

- **Métodos:**
  - `agregar_producto(producto, cantidad)`: Añade productos al carrito, verificando stock.
  - `calcular_total()`: Calcula el total de la compra.
  - `mostrar_resumen()`: Muestra el resumen de la compra (productos, cantidad, precio total).

### 5. **Tienda (tienda.py)**

Clase que representa la tienda, mostrando los productos disponibles y gestionando la selección.

- **Atributos:**
  - `productos_disponibles`: Lista de productos que están a la venta en la tienda.

- **Métodos:**
  - `mostrar_productos()`: Muestra el catálogo de productos.
  - `seleccionar_productos()`: Permite al usuario seleccionar productos y agregarlos al carrito.

---

## Ejecución del Proyecto

1. Clonar el repositorio en el entorno local.
2. Verificar que se tiene instalada la última versión disponible de Python.
3. Abrir una terminal o símbolo del sistema y navegar hasta el directorio donde se clonó el repositorio.
4. Ejecutar el archivo main.py para iniciar el programa.

```bash
python tienda.py
