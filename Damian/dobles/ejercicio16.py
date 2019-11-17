import os
precio_de_lapiceros, precio_de_cuaderno, precio_lapices= 0 , 0 , 0
#INPUT
precio_de_lapiceros = int(os.sys.argv[ 1 ])
precio_de_cuaderno = int(os.sys.argv[ 2 ])
precio_lapices = int(os.sys.argv[ 3 ])
# Processing
total = (precio_de_lapiceros + precio_de_cuaderno + precio_lapices)
#Verificador
comprobando = ( total >=20 )
#OUPUT
print( "#####################################")
print( "#     Bazar - ANALUCIA               ")
print( "#####################################")
print( "#")
print( "#variables:   cantidad")
print( "precio de lapiceros:", precio_de_lapiceros)
print( "precio de cuadernos:", precio_de_cuaderno)
print( "precio de lapices:", precio_lapices)
print( "precio total: s/. ", total)
print( "#####################################")

#condicion simple
# Si el total supera los 20, entra al sorteo de un canasta
if ( comprobando == True ):
    print(" usted entro al sorteo de una canasta ")
#fin_if
