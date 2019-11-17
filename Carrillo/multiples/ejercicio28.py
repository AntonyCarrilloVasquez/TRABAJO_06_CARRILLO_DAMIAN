import os
#imput
pi=float(os.sys.argv[1])
radio=float(os.sys.argv[2])
#processing
area_circunferencia=(pi*radio)
#output
if(area_circunferencia<=24):
    print("esta pequeño")
if(area_circunferencia>30 and area_circunferencia<60):
    print("esta mediano")
if(area_circunferencia>65):
    print("es grande")
