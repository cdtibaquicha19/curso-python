#i mprimir solo letras en a 
for letra in "holanda":
    if letra  =="a":
        print(letra)
        break
else:
    print("fin ciclo For")    
print("Continua el programa")


#imprimir solo numero pares
for pares in range(10):
    if pares%2 ==0:  
        print(pares)
        
#continue
for pares in range(10):
    if pares%2 !=0:  
       continue
    print(pares)
    
    
