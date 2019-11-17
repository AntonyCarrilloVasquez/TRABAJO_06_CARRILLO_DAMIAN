import os
#imput
masa=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
#processing
peso=(masa*gravedad)
#output
if(peso<=45):
    print("debes comer mas")
if(peso<=52):
    print("estas algo delgado")
if(peso>=95):
    print("estas gordito")
