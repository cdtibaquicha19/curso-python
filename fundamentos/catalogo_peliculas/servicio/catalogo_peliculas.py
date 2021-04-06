import os
class CatalogoPeliculas:
    ruta_archivo  = "Peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            # "a" - modo append ya que permite sobre escribir el archivo al abrirlo 
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__()+ "\n")
            
        except Exception as e :
            print("ocurrio un error al agregar :" , e )
            
        finally:
            #cierro el archivo abierto " peliculas .txt " 
            archivo.close()
    @staticmethod 
    
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catalogo peliculas : ")
            print(archivo.read())
        except Exception as e :
            print ("Ocurrio un error al listar peliculas " , e )
        finally:
         archivo.close()
         
    @staticmethod
    
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("archivo eliminado : " ,CatalogoPeliculas.ruta_archivo)        
        except Exception as e : 
            print (" a ocurrido un error al eliminar ",e)