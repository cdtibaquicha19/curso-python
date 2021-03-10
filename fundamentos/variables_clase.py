class Miclase:
    variable_clase = "variable de clase"
    
    def  __init__(self , variable_instancia):
        self.variable_instancia = variable_instancia
        
print(Miclase.variable_clase)   
objeto1 = Miclase("variable de instancia")
Miclase.variable_instancia = "modificando instancia"
        

print(objeto1.variable_instancia)
print(Miclase.variable_clase)   

print(objeto1.variable_clase)
print(Miclase.variable_clase)

objeto1.variable_clase ="modificando variable de clase "    

print(objeto1.variable_clase)

objeto2 = Miclase("nuevo valor de variable de instancia")
print(objeto2.variable_clase)



    