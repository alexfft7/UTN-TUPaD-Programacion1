#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    return print("Hola, Mundo!")

imprimir_hola_mundo()

#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return print(f"Hola, {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre,apellido,edad,residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese el lugar donde vive: ")
informacion_personal(nombre,apellido,edad,residencia)

#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
#y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
#como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
#llamar ambas funciones para mostrar los resultados.

import math
pi = math.pi
def calcular_area_circulo(radio):
    area = pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

radio = int(input("Ingrese un radio de un circulo: "))
print(f"El area del circulo es de {calcular_area_circulo(radio)} y su perimetro es de {calcular_perimetro_circulo(radio)}")

#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y 
#mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos // 3600

segundos = int(input("Ingrese una cantidad de segundos: "))
print(f"Hay {segundos_a_horas(segundos)} horas en {segundos} segundos.")

#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        multiplicacion = numero * i 
        print(f"{numero} x {i} = {multiplicacion} ")

numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado 
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los 
#resultados de forma clara.

def operacion_basicas(a,b):
    suma = a + b
    resta = a - b
    multi = a * b
    if b!=0:
        division = a / b
    else:
        division = None
    
    return(suma,resta,multi,division)

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro: "))

suma,resta,multi,division = operacion_basicas(a,b)

print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} x {b} = {multi}")
if division == None:
    print("No se puede dividir por cero.")
else:
    print(f"{a} % {b} = {division}")

#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
#función para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    imc = peso / (altura**2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso,altura)

print(f"Su indice de masa corporal es {imc:.2f}")

#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

celsius = float(input("Ingrese una temperatura en Celsius: "))
print(f"{celsius} grados Celsius es igual a {celsius_a_fahrenheit(celsius)} grados Fahrenheit.")

#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a,b,c):
    return (a + b + c) / 3

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

print(f"El promedio de los numeros ingresado es {calcular_promedio(a,b,c)}")






