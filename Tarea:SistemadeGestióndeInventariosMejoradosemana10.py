# class Inventario:
    def guardar_inventario(self):
        with open('inventario.txt', 'w') as file:
            for producto in self.productos:
                file.write(f"{producto.id}, {producto.nombre}, {producto.cantidad}, {producto.precio}\n")
                
                class Inventario:
    def _init_(self):
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open('inventario.txt', 'r') as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split(',')
                    producto = Producto(id, nombre, cantidad, precio)
                    self.productos.append(producto)
        except FileNotFoundError:
            print("El archivo de inventario no existe. Creando uno nuevo.")
            open('inventario.txt', 'w').close()
        except PermissionError:
            print("No se tienen permisos para acceder al archivo de inventario.")
            
            class Inventario:
    def guardar_inventario(self):
        try:
            with open('inventario.txt', 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.id}, {producto.nombre}, {producto.cantidad}, {producto.precio}\n")
        except FileNotFoundError:
            print("Error: Archivo de inventario no encontrado.")
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo de inventario.")
            
            class Inventario:
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto añadido exitosamente al inventario.")

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.id != id]
        self.guardar_inventario()
        print("Producto eliminado del inventario correctamente.")
        
