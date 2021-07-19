__author__= "Andres Franetovich"

#Declaro mis variables
numero = int(input("Ingrese el numero de la sucesion"))
orbita = []
#Inserto el numero inicial de la sucesion en la lista
orbita.append(numero)
operador = numero
acumulador = sumatoria = promedio = 0
#Igualo la variable may al numero ingresado para luego buscar el mayor dentro de la orbita
may = numero
#Informo el numero seleccionado 
print("*"*50)
print(f"Usted selecciono el numero {numero} para la sucesion")
print("*"*50)

#Utilizo el while para generar la orbita hasta que la sucesion llegue a 1
while numero != 1:
    if (numero%2)==0:
        #Caso par
        numero =int( numero/2)
        orbita.append(numero)    
    else:
        numero = int((3*numero) + 1)
        orbita.append(numero)

#Iteramos la orbita para calcular su promedio y buscamos el valor mayor
for i in orbita:
    acumulador += 1
    sumatoria += i
    if may <i:
        may = i
promedio = sumatoria/acumulador
#Finalmente imprimimos por consola los datos requeridos
print("*"*50)
print(f"La longitud de orbita de la sucesion es {len(orbita)}")
print(f"El mayor de los numeros en la sucesion es {may}")
print(f"El promedio de los valores que constituyen la orbita es de {promedio}")
print(f"La orbita consiste en los siguientes valores {orbita}")
print("*"*50)
