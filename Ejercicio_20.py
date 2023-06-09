print("*************************************************** PLAN DE MEJORAMIENTO ******************************************************\n")

#ejecicio1:
#hacer un programa que pida dos numeros y se de cuenta cual de ellos es par o si ambos lo son
num1=int(input("num1-> :"))
num2=int(input("num2-> :"))
if num1%2==0 and num2%2==0:
    print("ambos son pares ")
elif num1%2==0 and num2%2!=0:
    print("num1 es par")
elif num1%2!=0 and num2%2==0:
    print("num2 es par")
else:
    print("ambos numeron impares")
    