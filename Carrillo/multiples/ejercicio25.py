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
#condicionales multiple:
if(fuerza<12):
    print("eres muy debil")
if(fuerza>12):
    print("sigue asi")
if(fuerza>=50):
    print("eres fuerte")
