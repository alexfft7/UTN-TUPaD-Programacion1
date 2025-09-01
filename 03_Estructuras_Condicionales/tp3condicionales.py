#1)Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = input("Ingrese su edad:")
edad = int(edad)
if edad > 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad o ha ingresado un numero negativo.")

#2)
nota=input("Ingrese su nota:")
nota=int(nota)
if nota >= 6 and nota <= 10:
    print("aprobado")
elif nota < 6 and nota > 0:
    print("desaprobado")
else:
    print("no valido, ingrese otro numero")

#3)
num=input("Ingrese un numero par:")
num=int(num)
if num%2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor ingrese un numero par.")

#4)
edad = input("ingrese su edad:")
edad = int(edad)
if edad>0 and edad<12:
    print("Pertenece a la categoria Niño")
elif edad>=12 and edad<18:
    print("Pertenece a la categoria Adolescente")
elif edad>=18 and edad<30:
    print("Pertenece a la categoria Adulto Joven")
elif edad>30 and edad<100:
    print("Pertenece a la categoria Adulto.")

#5)
contraseña=input("Ingrese una contraseña de entre 8 y 14 caracteres:")
longitud=len(contraseña)
if longitud<=14 and longitud>=8:
    print("Ha ingresado una contraseña correcta.")
else:
    ("Por favor, ingrese una co ntraseña de entre 8 y 14 caracteres.")

#6)
#crea una lista con 50 numeros aleatorios entre 1 y 100
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#trae las funciones media mediana y modo
from statistics import mode, median, mean
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if moda == mediana == media:
    print("No hay sesgo")
elif media > mediana and mediana > moda:
    print("Hay un sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Hay un sesgo negativo o hacia la izquierda") 

#7)
frase=input("Ingrese una frase o palabra:").lower()
ultima_letra=frase[-1]
if ultima_letra == "a" or ultima_letra=="e" or ultima_letra=="i" or ultima_letra=="o" or ultima_letra=="u":
    print(frase,"!")
else:
    print(frase)

#8)
nombre=input("ingrese su nombre:")
escritura_nombre=input("Ingrese 1. Su nombre se escribira en mayusculas, 2.Su nombre se escribira en minusculas o 3.su nombre tendra la primera letra en mayuscula, segun lo desee:")
if escritura_nombre=="1":
    nombre=nombre.upper()
    print(nombre)
elif escritura_nombre=="2":
    nombre=nombre.lower()
    print(nombre)
elif escritura_nombre=="3":
    nombre=nombre.title()

#9)
magnitud_terremoto = input("Ingrese la magnitud del terremoto:")
magnitud_terremoto = float(magnitud_terremoto)
if magnitud_terremoto < 3:
	print("El terremoto ha sido muy leve o imperceptible.")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
	print("El terremoto ha sido leve o ligeramente perceptible.")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
	print("El terremoto ha sido Moderado o sentido por personas, pero generalmente no causa daños.")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
	print("El terremoto ha sido fuerte, ha causado daños en estructuras debiles.")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
	print("El terremoto ha sido muy fuerte, pudo causar daños significativos.")
elif magnitud_terremoto >= 7:
	print("El terremoto ha sido extremo, pudo causar daños graves a gran escala.")

#10)
hemisferio = input("¿En que hemisferio se encuentra, norte o sur?").lower()
dia = int(input("Ingrese el dia de hoy:"))
mes = input("ingrese el nombre del mes en el que se encuentra:").lower()

if (mes == "enero" or mes ==  "febrero") or (mes == "diciembre" and dia >=21) or (mes == "marzo" and dia <= 20):
    if hemisferio == "norte":
        estacion = "invierno"
    else:
        estacion = "verano"

elif (mes == "abril" or mes ==  "mayo") or (mes == "marzo" and dia >=21) or (mes == "junio" and dia <= 20):
    if hemisferio == "norte":
        estacion = "primavera"
    else:
        estacion = "otoño"

elif (mes == "julio" or mes ==  "agosto") or (mes == "junio" and dia >=21) or (mes == "septiembre" and dia <= 20):
    if hemisferio == "norte":
        estacion = "verano"
    else:
        estacion = "invierno"

elif (mes == "octubre" or mes ==  "noviembre") or (mes == "septiembre" and dia >=21) or (mes == "diciembre" and dia <= 20):
    if hemisferio == "norte":
        estacion = "otoño"
    else:
        estacion = "primavera"

print("La estacion es", estacion)