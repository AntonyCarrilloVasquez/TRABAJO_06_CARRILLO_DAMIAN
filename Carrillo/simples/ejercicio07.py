import os
#imput
densidad=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
gravedad=float(os.sys.argv[3])
#processing
presion=(densidad*altura*gravedad)
#output
if (presion>42):
    print("presion en estado critico para el producto")
#fin_if

