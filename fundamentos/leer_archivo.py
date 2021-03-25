
try:

    archivo = open("C:\\Cursos\\curso-python\\fundamentos\\prueba.txt","r")
    #print(archivo.read())
    archivo2 = open("nuevo2.txt","a")
    archivo2.write(archivo.read())
    
except Exception as e :
    
    print(e)
    
finally :  
    
    archivo.close()
    archivo2.close() 