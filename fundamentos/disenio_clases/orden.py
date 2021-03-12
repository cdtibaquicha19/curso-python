class Orden : 
    contador_ordenes = 0 
    def __init__(self,productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos
        
    def agregar_producto(self,producto):
        self.__productos.append(producto)
    
    def calcular_total(self):
        total = 0 
        for producto in self.__productos :
            total+= producto.get_precio()
        return "El total es : "+str(total)

    def __str__(self):
        productos_srt = ""
        # Recorre el arreglo con los datos ingresados en productos 
        for productos in self.__productos : 
            #imprime llamando la misma funcion str y agrega el valor a una variable para poder imprimir 
            productos_srt +=  productos.__str__()+"  |  "
        #imprime el id de la orden y el str anterior para mostrar el listado de productos en la orden 
        return  "Orden : " + str(self.__id_orden) + " Productos: " +     productos_srt
  
  