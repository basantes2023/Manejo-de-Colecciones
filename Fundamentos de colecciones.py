#Este programa utiliza las clases Producto e Inventario para representar los productos y el inventario de una tienda.
#El inventario se almacena en un diccionario, donde la clave es el ID del producto y el valor es una instancia de la clase Producto.
#El programa permite realizar operaciones como agregar productos, eliminar productos, actualizar la cantidad y el precio de los productos, buscar productos por nombre, mostrar todos los productos, guardar el inventario en un archivo y cargar el inventario desde un archivo.
#El inventario se guarda en un archivo utilizando el módulo pickle, que permite serializar y deserializar objetos.
# Al guardar el inventario, se serializa el diccionario de productos y se guarda en un archivo binario. Al cargar el inventario, se lee el archivo binario y se deserializa el diccionario de productos.
import pickle

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].set_cantidad(cantidad)

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].set_precio(precio)

    def buscar_producto(self, nombre):
        resultados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

    def guardar_inventario(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self, archivo):
        with open(archivo, 'rb') as f:
            self.productos = pickle.load(f)

# Crear instancia de Inventario
inventario = Inventario()

# Funciones de interacción con el usuario
def mostrar_menu():
    print("=== Sistema de Gestión de Inventarios ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad de producto")
    print("4. Actualizar precio de producto")
    print("5. Buscar producto por nombre")
    print("6. Mostrar todos los productos")
    print("7. Guardar inventario")
    print("8. Cargar inventario")
    print("9. Salir")

def agregar_producto():
    print("=== Agregar producto ===")
    id = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    producto = Producto(id, nombre, cantidad, precio)
    inventario.agregar_producto(producto)
    print("Producto agregado correctamente.")

def eliminar_producto():
    print("=== Eliminar producto ===")
    id = input("Ingrese el ID del producto a eliminar: ")
    inventario.eliminar_producto(id)
    print("Producto eliminado correctamente.")

def actualizar_cantidad():
    print("=== Actualizar cantidad de producto ===")
    id = input("Ingrese el ID del producto a actualizar: ")
    cantidad = int(input("Ingrese la nueva cantidad del producto: "))
    inventario.actualizar_cantidad(id, cantidad)
    print("Cantidad de producto actualizada correctamente.")

def actualizar_precio():
    print("=== Actualizar precio de producto ===")
    id = input("Ingrese el ID del producto a actualizar: ")
    precio = float(input("Ingrese el nuevo precio del producto: "))
    inventario.actualizar_precio(id, precio)
    print("Precio de producto actualizado correctamente.")

def buscar_producto():
    print("=== Buscar producto por nombre ===")
    nombre = input("Ingrese el nombre del producto a buscar: ")
    resultados = inventario.buscar_producto(nombre)
    if len(resultados) == 0:
        print("No se encontraron productos con ese nombre.")
    else:
        print("Resultados de la búsqueda:")
        for producto in resultados:
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

def mostrar_productos():
    print("=== Mostrar todos los productos ===")
    inventario.mostrar_productos()

def guardar_inventario():
    archivo = input("Ingrese el nombre del archivo para guardarel inventario: ")
    inventario.guardar_inventario(archivo)
    print("Inventario guardado correctamente.")

def cargar_inventario():
    archivo = input("Ingrese el nombre del archivo para cargar el inventario: ")
    inventario.cargar_inventario(archivo)
    print("Inventario cargado correctamente.")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        actualizar_cantidad()
    elif opcion == "4":
        actualizar_precio()
    elif opcion == "5":
        buscar_producto()
    elif opcion == "6":
        mostrar_productos()
    elif opcion == "7":
        guardar_inventario()
    elif opcion == "8":
        cargar_inventario()
    elif opcion == "9":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
