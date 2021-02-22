valor  = float(input("Proporciona un valor entre 0 y 10:"))
nota = None
if(valor>=9 and valor<=10):
    nota= "A"
elif (valor>=8 and valor<9):
    nota ="B"
elif (valor>=7 and valor<8):
    nota ="C"
elif (valor>=6 and valor<7):
    nota ="D"
elif (valor>=0 and valor<6):
    nota ="F"
else:
    nota=0
if (nota==0):
    print("Valor desconocido")
else:      
    print("su nota es :", nota )
    


    