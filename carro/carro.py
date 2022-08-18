"""
    En esta clase trabajaremos las sesiones activas del usuario con los productos
    que se agregen a nuestro carrito de compras
"""
class Carro:
    def __init__(self, request):                # Constructor de la clase
        self.request = request                  # Variable request, para los elementos del template
        self.session = request.session          # Variable de sesion de navegador
        carro =  self.session.get('carro')      # Variable de sesion con el carro de compras

        # Validación de sesion de navegacion con datos de carrito de compras:
        if not carro:
            carro = self.session['carro'] = {}  # Si no hay carro, creamos un diccionario vacio
       
        self.carro = carro                      # De lo contrario dejaremos los datos del carro tal y como se encuentra
        
    # Métodos de la clase carro:
    def agregar(self, producto):
        # Validamos que el producto no exista en el el carito:
        if (str(producto.id) not in self.carro.keys()):         # Si el producto no se encuentra en el carro, agregar:
            self.carro[producto.id] = {                         # Creamos un diccionario con los atributos del producto, y este
                "producto_id": producto.id,                     # se guarda por id, es decir por cada producto creamos esta 
                "nombre": producto.nombre,                      # estructura
                "precio": str(producto.precio),                 # El campo precio lo pasamos como str, 
                "cantidad":1,
                "imagen": producto.imagen.url
            }
        # Si ya hay un producto actualizamos la cantidad de ese producto:
        else: 
            for key, value in self.carro.items():               # Recorremos todos los items del carrito
                if key == str(producto.id):                     # Si encontramos un producto que tiene ese id
                    value['cantidad'] = value['cantidad'] + 1   # Sumamos el valor de la clave cantidad
                    break                                       # Terminamos abruptamente el proceso
        # Guardamos en la funcion guardar carro:
        self.guardar_carro()                                    # Ahora debemos crear esta funcion.
    
    # Funcion para guardar datos en carro:
    def guardar_carro(self):                    
        self.session['carro'] = self.carro      # Guardamos en la variable session, el objeto carro
        self.session.modified = True            # Asignamos el cambio de modificacion.

    # Funcion para eliminar producto:
    def eliminar(self, producto):               
        producto.id = str(producto.id)          # Convertimos en string el producto id, porque es la clave de nuestro objeto
        if producto.id in self.carro:           # Si esta clave se encuentra en el objeto carro
            del self.carro[producto.id]         # Eliminamos esta clave del objeto
            self.guardar_carro()                # Actualizamos el carrito de compras

    # Funcion eliminar una cantidad de producto:
    def restar_producto(self, producto):
        for key, value in self.carro.items():               # Recorremos todos los items del carrito
            if key == str(producto.id):                     # Si encontramos un producto que tiene ese id
                value['cantidad'] = value['cantidad'] - 1   # Restamos el valor de la clave cantidad
                if value['cantidad'] < 1:                   # Si restamos todos los productos, 
                    self.eliminar(producto)                 # Eliminamos el producto completo con la función eliminar
                break                                       # Terminamos abruptamente el proceso
        self.guardar_carro()                                # Actualizamos el carrito de compras
    
    # Funcion Limpiar el carrito completo:
    def limpiar_carro(self):
        carro = self.session['carro'] = {}                  # Creamos un diccionario vacio
        self.session.modified = True                        # Actualizamos la sesion.