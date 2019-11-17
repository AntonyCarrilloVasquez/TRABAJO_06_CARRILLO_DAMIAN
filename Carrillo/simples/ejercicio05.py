import os
#imput
masa=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])
#processing
fuerza=(masa*aceleracion)
#output
print("#####################")
print(" fuerza de una persona ")
print("#####################")
print("#")
print("masa:                ",masa," ")
print("aceleracion:         ",aceleracion," ")
print("fuerza               ",fuerza," ")
print("#####################")
#condicionales simples
if(fuerza<12):
    print("eres muy debil")
#fin_if
