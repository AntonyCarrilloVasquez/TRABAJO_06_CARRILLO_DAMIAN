import os
#imput
velocidad1=int(os.sys.argv[1])
velocidad2=int(os.sys.argv[2])
distancia=int(os.sys.argv[3])
#processing
tiempo_encuentro=distancia/(velocidad1*velocidad2)
#verificador
verificar=(tiempo_encuentro<=127)
#output
print("#####################")
print(" Tiempo de encuentro de dos autos ")
print("#####################")
print("#")
print("velocidad1:            ",velocidad1," ")
print("velocidad2:            ",velocidad2," ")
print("distancia:             ",distancia," ")
print("tiempo de encuentro    ",tiempo_encuentro," ")
print("#####################")
#condicionales simples
if (verificar==True):
    print("casi se chocan :'v")
