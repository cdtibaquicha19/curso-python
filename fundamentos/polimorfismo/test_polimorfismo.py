from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto), end="\n\n")
    if isinstance(objeto,Gerente):
        print(objeto.departamento)
        

    
empleado = Empleado("Juan" , 100.000)
imprimir_detalles(empleado)


empleado= Gerente("karla" , 200.000, "Sistemas")
imprimir_detalles(empleado)


