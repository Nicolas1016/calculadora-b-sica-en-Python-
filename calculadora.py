"""
Realizar una calculadora usando sub-rutinas. Se introduce un número de 1 a 4.

Si es el número 1 se llama la subrutina de sumar.
Si es el número 2 se llama la subrutina de restar.
Si es el número 3 se llama la subrutina de multiplicar.
Si es el número 4 se llama la subrutina de dividir.
En los 4 casos se piden por pantalla 2 números.
El número de 1 a 4 para las operaciones, si es diferente, mostrar “número equivocado”

"""

def sumar():
    return num1 + num2

def restar():
    return num1 - num2

def multiplicar():
    return num1 * num2

def dividir():
    return num1 / num2

#codigo

datos = int(input("ingrese la opcion que desea operar 1- suma, 2-resta, 3-multiplicar , 4-dividir : "))

if datos == 1 :
    num1 = float(input("ingrese el primer digito:"))
    num2 = float(input("ingrese el segundo digito:"))
    operacion = sumar()
    print("el resultado de la suma es :", operacion )


elif datos == 2  :
    num1 = float(input("ingrese el primer digito:"))
    num2 = float(input("ingrese el segundo digito:"))
    operacion = restar()
    print("el resultado de la resta es :", operacion )

elif datos == 3  :
    num1 = float(input("ingrese el primer digito:"))
    num2 = float(input("ingrese el segundo digito:"))
    operacion = multiplicar()
    print("el resultado de la multiplicacion es :", operacion )    

elif datos == 4  :
    num1 = float(input("ingrese el primer digito:"))
    num2 = float(input("ingrese el segundo digito:"))
    operacion = dividir()
    print("el resultado de la division es :", operacion )

else:
    print("opcion no valida")