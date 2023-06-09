print("*************************************************** PLAN DE MEJORAMIENTO ******************************************************\n")

#condicionales combinados
edad= int("digite su edad: ")
# if edad>=18:
#     print ("es mayor de edad")
# else:
#     print ("no es mayor de edad")
if edad>0 and edad<=100:
    print("edad correcta")
    if edad>=18:
        print("es mayor de edad")
else :
    print("edad incorrecta")
    