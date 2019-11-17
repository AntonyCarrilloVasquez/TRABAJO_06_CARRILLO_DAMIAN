import os
#imput
costo_fijo=int(os.sys.argv[1])
produccion=int(os.sys.argv[2])
#processing
costo_fijo_medio=(costo_fijo*produccion)
#output
if(costo_fijo_medio>45):
    print("vamos por buen camino sigamos asi")
else:
    print("tenemos problemas")
