print("*************************************************** PLAN DE MEJORAMIENTO ******************************************************\n")

#ejercicio4
#construir un programa que simule el funcionamiento de una calculadore que pueda realizar las cuatro operaciones aritmeticas basica (suma , resta,multiplicacion y divicion) el usuario debe especificar la operacion con el primer caracter del nombre de la operacion
# S, s- suma
# R,r
# P,p,M,m-multiplicacion
# D,d-divicion
num1 = float("digite un numero :")
num2 = float("digite un numero :")
operacion= input("digite la operacion :").upper
if operacion == "S":
    suma=num1+num2
    print(f"\nla suma es : {suma}")
elif operacion == "R":
    resta=num1-num2
    print(f"\nla resta es : {resta}")
elif operacion == "P":
    multiplicacion=num1*num2
    print(f"\nla multiplicacion es : {multiplicacion}")

elif operacion == "D":
    divicion=num1/num2
    print(f"\nla divicion es : {divicion}")
else :
    print("\nse equivoco de operacion")
