import os
#imput
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])
#processing
promedio=(nota1+nota2+nota3)/3
#output
if (promedio> 15):
    print("estudia más")
if(promedio<=27):
    print("muy bien")
if(promedio==20):
    print("excelente")
#fin_if
