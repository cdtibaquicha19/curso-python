
from numeros_identicos_exception import NumerosIdenticosEx
resultado = None 

try:
    a = int(input("Primer numero :"))
    b = int(input("Segundo numero :"))
    if a == b:
        raise NumerosIdenticosEx("los valores son identicos ")
    resultado=a/b
    
    
except ZeroDivisionError as e :
    
    resultado= "error division por cero no es posible"
    print("Ocurrio un error",e)
    
except TypeError as e :
    
    print("Ocurrio un error con los valores",e)
    resultado= "no se pueden operar los valores "
    
except Exception as e :
    print("error general",e)
    print(type(e))

else:
    print("no hubo ningun error")
    
finally:
    print("se validaron errores")
    
print("resultado de la division es : "+ str(resultado))
