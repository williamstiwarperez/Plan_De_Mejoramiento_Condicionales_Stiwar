print("*************************************************** PLAN DE MEJORAMIENTO ******************************************************\n")

#ejercicio 4
#hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circuferencia 
import math # utilice el import match, como el ejemplo cuando utilizamos pi:3,1416
radio=float(input("radio -> "))
area= math.pi * radio**2
longitud =2*math.pi * radio
print(f"el area es :{area}")
print(f"la de la circuferencia es :{longitud}")
