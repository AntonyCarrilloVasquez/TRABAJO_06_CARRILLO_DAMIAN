import os
#imput

#IMPRESION TIPO BOLETA

#INPUT
cliente=os.sys.argv[1]
entrega1=int(os.sys.argv[2])
entrega2=int(os.sys.argv[3])
entrega3=int(os.sys.argv[4])
pu1=float(os.sys.argv[5])
pu2=float(os.sys.argv[6])
pu3=float(os.sys.argv[7])
IGV=float(os.sys.argv[8])
#PROCESSING
total=(entrega1*pu1+entrega2*pu2+entrega3*pu3)+IGV
#VERIFICADOR
verificar=(total>=562)
#OUTPUT
print("##########################")
print(" BOLETA DE VENTA : PEPITO ")
print("##########################")
print("#")
print("#cliente:            ",cliente,"      ")
print("#zapatillas:         ",entrega1,"     ")
print(" pu polos:           ",pu1,"          ")
print("#polos:              ",entrega2,"     ")

#condicional simple:
if(verificar==True):
    print("ganaste en chupetin por comprar aqui")
