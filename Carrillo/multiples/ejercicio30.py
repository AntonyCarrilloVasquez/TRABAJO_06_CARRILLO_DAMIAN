import os
#imput
masa=int(os.sys.argv[1])
volumen=int(os.sys.argv[2])
#processing
densidad=(masa/volumen)
#output
print("#####################")
print(" densidad de un cuerpo ")
print("#####################")
print("#")
print("masa:              ",masa," ")
print("volumen:           ",volumen," ")
print("densidad           ",densidad," ")
print("#####################")
#condicionales multiple
if (densidad<=39):
    print("la densidad es aceptable")
if(densidad>40 and densidad<50):
    print("la densidad esta anormal")
if(densidad>60):
    print("esta demasiado espeso")
