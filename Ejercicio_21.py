print("*************************************************** PLAN DE MEJORAMIENTO ******************************************************\n")

#ejercicio2
#hacer un programa que pida 3 numeros y determine cual es el mayor 
num1=int(input("digite num 1: "))
num2=int(input("digite num 2: ") ) 
num3=int(input("digite num 3: "))
if num1>=num2 and num1>num3:
    print(f"el numero mayor es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"el numero mayor es {num2}")
elif num3>=num1 and num3>=num2:
    print(f"el numero mayor es {num3}")
    