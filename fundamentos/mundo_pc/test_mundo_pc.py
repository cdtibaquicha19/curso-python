from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado


teclado_hp = Teclado("hp" , "usb")
raton_hp = Raton("hp" , "usb")
monitor_hp  = Monitor("hp" , "14 pulgadas")

teclado_asus = Teclado("hp" , "usb")
raton_asus = Raton("hp" , "usb")
monitor_asus  = Monitor("hp" , "14 pulgadas")

computador_hp = Computadora("hp" , monitor_hp , teclado_hp  ,raton_hp)
computador_asus = Computadora("asus" , monitor_asus , teclado_asus  ,raton_asus)
computador_gamer = Computadora("gamer" , monitor_hp, teclado_asus  ,raton_asus)


computadoras1 = [computador_hp , computador_asus , computador_gamer]
computadoras2 = [computador_asus , computador_gamer]
orden1 =Orden(computadoras1)
orden1.agregar_computadora(computador_hp)

orden2=Orden(computadoras2)
print(orden1)
print(orden2)





