#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
num = 0
for num in range(0,101):
    print(num)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.
num = input("Ingrese un numero entero:")
digitos = len(num)
print("El numero ingresado tiene", digitos ,"digitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.
num1 = int(input("ingrese un numero:"))
num2 = int(input("ingrese otro numero:"))
suma = 0
if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux
contador = num1
for contador in range(num1+1,num2):
    suma += contador
    contador += 1
print(suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.
num = int(input("Ingrese un numero entero o si desea finalizar el programa ingrese un 0:"))
suma = 0
while num != 0:
    suma += num
    print("La suma de los numeros ingresados es igual a" , suma)
    num = int(input("Ingrese otro numero si desea seguir sumando o 0 para detener el programa:"))

print("El programa ha finalizado.")   

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num_aleatorio = random.randint(0, 9)
print(num_aleatorio)
num_adivinado = int(input("Intente adivinar el numero entre 0 y 9:"))
intentos = 1

while num_adivinado != num_aleatorio:
    intentos += 1
    num_adivinado = int(input("Lo siento, ese no es el numero correcto. Intente de nuevo:"))

print("Felicitaciones, ha adivinado el numero. Fueron necesarios", intentos, "intentos.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.
num=100
for num in range(100,0,-2):
    print(num)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

num_limite = int(input("Ingrese un numero entero positivo:"))
suma = 0
contador = 0
if num_limite <= 0:
    print("Lo siento, no ha ingresado un numero positivo.")
else:    
    for contador in range(0,num_limite+1):
        suma += contador
    print("la suma de los numeros es igual a", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cantidad_num = 100
contador = 0
pares = 0
impares = 0
neg = 0
positivos = 0
for contador in range(cantidad_num):
    print("ingrese el numero", contador+1)
    num = int(input())
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num <=0:
        neg += 1
    else:
        positivos +=1
print("La cantidad de numeros pares es:", pares)
print("La cantidad de numeros impares es:", impares)
print("La cantidad de numeros positivos es:", positivos)
print("La cantidad de numeros negativos es:", neg)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

cant_num = 100
contador = 0
suma = 0
for contador in range(cant_num):
    print("ingrese el numero", contador+1)
    num = int(input())
    suma += num
media = suma / cant_num
print("el promedio de los numeros ingresados es", media) 

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("ingrese un numero:"))
digito = 0
invertido = 0

while num != 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num = num // 10

print(invertido)