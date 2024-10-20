
# Sistema de Gestión de Productos de Ropa

Este proyecto es una simulación de una tienda de ropa, donde puedes seleccionar productos como camisas, pantalones, y zapatos, agregarlos a un carrito y obtener un resumen con el total a pagar.

## Descripción

El sistema está construido utilizando clases y conceptos de Programación Orientada a Objetos (POO) en Python. Permite crear diferentes tipos de productos de ropa con sus respectivas características, gestionar el stock y realizar compras.

## Archivos Principales

- **producto.py**: Define las clases base para los productos y sus atributos.
- **carrito.py**: Contiene la lógica para gestionar el carrito de compras.
- **tienda.py**: Simula el flujo de una tienda física, permitiendo al usuario seleccionar productos y procesar la compra.
- **main.py**: Este archivo es el punto de entrada principal del programa. Ejecuta la tienda y permite interactuar con el sistema de selección de productos.

## Requisitos

- **Python 3.x** debe estar instalado en tu sistema.

## Instalación en Visual Studio

1. Abre Visual Studio.
2. Crea un nuevo proyecto de tipo **Python Application**.
3. Añade los archivos `producto.py`, `carrito.py`, `tienda.py`, y `main.py` a la carpeta del proyecto.
4. Asegúrate de que `main.py` sea el archivo principal ejecutable del proyecto.

## Ejecución del Proyecto

1. Abre el archivo `main.py` en Visual Studio.
2. Presiona **F5** para ejecutar el programa.
3. Sigue las instrucciones en la terminal para seleccionar productos y finalizar la compra.

### Alternativa: Ejecución desde la terminal

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta el siguiente comando:

```bash
python main.py
```

## Uso

1. **Visualización de productos**: Al ejecutar el programa, se te mostrarán los productos disponibles en la tienda.
2. **Selección de productos**: Ingresa el número del producto que deseas agregar al carrito.
3. **Cantidad**: Se te pedirá que indiques la cantidad de productos a agregar.
4. **Finalizar compra**: Ingresa 'q' para terminar la selección y recibir el resumen de la compra con el total a pagar.

## Ejemplo de ejecución

```bash
1. Producto: Camisa de Algodón || Precio: $20 || Stock: 10 || Talla: M || Tipo de Tela: Algodón || Tipo de Cuello: Clásico
2. Producto: Pantalón de Mezclilla || Precio: $30 || Stock: 5 || Talla: L || Tipo de Tela: Denim || Largo: Corto
3. Producto: Zapato de Cuero || Precio: $50 || Stock: 7 || Talla: 42 || Tipo de Tela: Cuero

Seleccione el número del producto a agregar al carrito (o 'q' para finalizar): 1
¿Cuántas unidades de Camisa de Algodón desea agregar? 2
Producto agregado al carrito: Camisa de Algodón x 2.

Total a pagar: $40
```

---
