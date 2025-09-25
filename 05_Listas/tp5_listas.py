#1) Crear una lista con las notas de 10 estudiantes.
notas=[9,10,5,3,8,9,8,6,8,10]

#reccorre uno por uno los elementos de notas
for n in notas:
    print(n)

#promedio
promedio= sum(notas) / len(notas)
print(f"El promedio de notas es: {promedio}")

#nota mas alta y mas baja
mayor=0
menor=11
for n in notas:
    if n>mayor:
        mayor=n
    else:
        if n<menor:
            menor=n
print(f"La nota mas alta es {mayor} y la nota mas baja es {menor}")

#2) Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabéticamente.
# Preguntar al usuario qué producto desea eliminar y actualizar la lista.
aux=input("Ingrese 5 productos:")
productos=[aux]

for cont in range(4):
    aux=input("")
    productos.append(aux)

print(productos)

#orden alfabetico
productos.sort()
print(productos)

eliminar=input("¿Que elemento de la lista desea eliminar? ")
print(eliminar)

while (eliminar in productos) == False:   
    print("Ese producto no existe, intente de nuevo.")
    eliminar=input("¿Que elemento de la lista desea eliminar? ")

if (eliminar in productos) == True:
    productos.remove(eliminar)
    print("Elemento eliminado de forma exitosa. La lista ahora se ve de la siguiente manera:")
    print(productos)

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
import random 
pares=0
impares=0
numeros=[]
pares=[]
impares=[]

for i in range(15):
    num_aleatorio=random.randint(1, 100)
    numeros.append(num_aleatorio)
    if num_aleatorio%2==0:
        pares.append(num_aleatorio)
    else:
        impares.append(num_aleatorio)

long_pares= len(pares)
long_impares= len(impares)

print(f"La lista pares tiene {long_pares} numeros y la lista impares tiene {long_impares} numeros.")

#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

datos=[1,3,5,3,7,1,9,5,3]
sin_repetidos=[]

#recorrer los valores de mi lista
for i in datos:
    if i not in sin_repetidos:
        sin_repetidos.append(i)
    else:
        pass

print(f"La lista sin numeros repetidos es {sin_repetidos}")

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

presentes=["Jose","Ana","Paula","Pedro","Agostina","Silvia","Elias","Jorge"]
opcion=0

while opcion != "3":
    print("Eliga una opcion:")
    print("1.Si desea agregar un estudiante a la lista.")
    print("2.Si desea eliminar un estudiante de la lista.")
    print("3.Si desea finalizar")
    opcion=input()

    if opcion=="1":
        nombre=input("¿Que estudiante desea agregar?")
        presentes.append(nombre)
        print(f"Se ha agregado exitosamente a {nombre} a la lista")
    elif opcion=="2":
        nombre=input("¿Que estudiante desea eliminar?").title()
        if nombre in presentes:
            presentes.remove(nombre)
            print(f"Se ha eliminado exitosamente el nombre de {nombre} de la lista")
        else:
            print("Ese nombre no se encuentra en la lista.")

print(f"La nueva lista es {presentes}.")

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

numeros=[1,2,3,4,5,6,7]
print(numeros)

indice=6
ultimo=numeros[-1]

for i in numeros:
    if indice>0:
        numeros[indice]=numeros[indice-1]
    indice-=1

numeros[0]=ultimo

print(numeros)

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

temp=[[16,27],[17,28],[16,30],[20,28],[19,27],[20,27],[15,24]]

minima=[fila[0] for fila in temp]
promedio_min=sum(minima)//7

maxima=[fila[1] for fila in temp]
promedio_max=sum(maxima)//7

print(f"El promedio de las temperaturas minimas es de {promedio_min} y el de las temperaturas maximas es de {promedio_max}")

amplitud_max=0
indice=0
dia=0
for i in temp:
    amplitud=temp[indice][1]-temp[indice][0]
    if amplitud>amplitud_max:
        amplitud_max=amplitud
        dia=indice+1
    indice+=1

print(f"La maxima amplitud termica fue de {amplitud_max} y se registro el dia {dia}.")

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.

notas=[[5,8,9],[10,8,8],[6,8,4],[9,7,10],[3,6,5]]
aux=1
for i in notas:
    print(i)
    promedio_estu=sum(i)//3
    print(f"El promedio del estudiante {aux} es {promedio_estu}.")
    aux+=1

materia1=[fila[0] for fila in notas]
promedio_mat1=sum(materia1)//5
materia2=[fila[1] for fila in notas]
promedio_mat2=sum(materia2)//5
materia3=[fila[2] for fila in notas]
promedio_mat3=sum(materia3)//5

print(f"El promedio de la primera materia es {promedio_mat1}, el de la segunda {promedio_mat2} y el de la tercera {promedio_mat3}")

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

tateti=[
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
cant_filas=len(tateti)
cant_columnas=len(tateti[0])

for i in range(cant_filas):
    print(tateti[i])

while any('-' in fila for fila in tateti):
    print("Jugador 1, ingrese la pocision donde desea colocar una X:")
    fila=int(input("Fila: "))
    columna=int(input("Columna: "))

    tateti[fila-1][columna-1]="X"

    for i in range(cant_filas):
        print(tateti[i])

    print("Jugador 2, ingrese la pocision donde desea colocar un 0:")
    fila=int(input("Fila: "))
    columna=int(input("Columna: "))
    
    tateti[fila-1][columna-1]="0"
    
    for i in range(cant_filas):
        print(tateti[i])

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

ventas=[[10,5,3,7],
        [8,8,4,9],
        [9,5,6,7],
        [15,7,9,5],
        [6,11,7,3],
        [9,8,1,8],
        [4,7,13,3]]

#total de ventas por productos
producto1=[fila[0] for fila in ventas]
total1=sum(producto1)
producto2=[fila[1] for fila in ventas]
total2=sum(producto2)
producto3=[fila[2] for fila in ventas]
total3=sum(producto3)
producto4=[fila[3] for fila in ventas]
total4=sum(producto4)

total_productos=[total1,total2,total3,total4]

aux=0
for i in total_productos:
    print(f"El total de ventas para el producto {aux+1} fue de {total_productos[aux]}.")
    aux+=1

mas_vendido=0
indice_mas_vendido=0
for i in range(4):
    if total_productos[i]>mas_vendido:
        mas_vendido=total_productos[i]
        indice_mas_vendido=i+1

print(f"El producto mas vendido fue el {indice_mas_vendido} con {mas_vendido} ventas.")

#dia con mayores ventas
max_ventas=0
aux=0
for i in ventas:
    total_dia=sum(i)
    aux+=1
    if total_dia>max_ventas:
        max_ventas=total_dia
        dia=aux

print(f"El dia que mas se vendio fue el {dia} con {max_ventas} ventas.")