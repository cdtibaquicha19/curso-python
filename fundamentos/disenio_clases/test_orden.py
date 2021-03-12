from producto import Producto
from orden import Orden

producto1 = Producto("Camisa" , 100 )
producto2 = Producto("Pantalon" , 500 )
producto3 = Producto("Chaqueta" , 200 )


productos = [producto1,producto2]

orden1 = Orden(productos)

print(orden1)
print(orden1.calcular_total())

# agrego un elemnto producto mas a la lista 

orden1.agregar_producto(producto3)
orden2 = Orden(productos)
print(orden2) 

print(orden2.calcular_total())




