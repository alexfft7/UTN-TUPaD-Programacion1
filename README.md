# UTN-TUPaD-Programacion1
TP2 Programacion

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

 #2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input("Escribe tu nombre:")
print(f"Hola, {nombre}!")
    
    #3)  Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
lugar = input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")
    
    #4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
radio = input("Ingrese el radio de un circulo:")
radio = float(radio)
import math
pi = math.pi
area = math.pi * radio**2
print(f"El area del circulo es {area}.")

    #5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos = input("Ingrese una cantidad de segundos:")
segundos = int(segundos)
horas = segundos // 3600
print(f"Hay {horas} horas en {segundos} segundos.")

    #6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero = input("Ingrese un numero:")
numero = int(numero)
print(f"{numero}x1 =" , numero*1) 
print(f"{numero}x2 =" , numero*2) 
print(f"{numero}x3 =" , numero*3) 
print(f"{numero}x4 =" , numero*4) 
print(f"{numero}x5 =" , numero*5) 
print(f"{numero}x6 =" , numero*6) 
print(f"{numero}x7 =" , numero*7) 
print(f"{numero}x8 =" , numero*8) 
print(f"{numero}x9 =" , numero*9) 
print(f"{numero}x10 =" , numero*10) 

    #7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = input("Ingrese un numero:")
num2 = input("Ingrese otro numero:")
num1 = int(num1)
num2 = int(num2)
suma = num1 + num2
division = num1 / num2
multi = num1 * num2 
resta = num1 - num2 
print(f"{num1} + {num2} = {suma}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} x {num2} = {multi}")
print(f"{num1} - {num2} = {resta}")

    #8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. 
altura = input("Ingrese su altura:")
peso = input("Ingrese su peso:")
altura = float(altura)
peso = float(peso)
imc = peso / altura**2
print(f"Su indice de masa corporal es de {imc}")

    #9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.
celsius = input("Ingrese la temperatura en grados celsius:")
celsius = float(celsius)
fahren = 1.8 * celsius + 32
print(f"El equivalente en grados Fahrenheit es de {fahren}")

    #10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
num1 = input("A continuacion ingrese un numero:")
num2 = input("Ingrese otro numero:")
num3 = input("Ingrese un numero mas:")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los numeros ingresados es {promedio}")

