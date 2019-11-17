import os
#imput
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cantidad=int(os.sys.argv[3])
precio=int(os.sys.argv[4])
#processing
total=(cantidad*precio)
#verificador
verificar=(total>=176)
#output
print("#################")
print(" boleta de compra ")
print("#################")
print("#")
print("cliente:        ",cliente,"    ")
print("producto:       ",producto,"   ")
print("cantidad:       ",cantidad,"   ")
print("precio:         ",precio  ,"   ")
#condicional multiple:
if(total>75):
    print("te ganaste un desodorante")
if(total<12):
    print("sigue intentando")
if(total>30):
    print("ganaste un juego")
