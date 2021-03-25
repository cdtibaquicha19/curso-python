try:
    archivo = open("prueba.txt","w")
    archivo.write("agregamos informacion al archivo \n")
    archivo.write("adios")
    
except Exception as e :
    print(e)
finally : 
    archivo.close()