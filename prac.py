canttemperatura=0
canttempmayores=0
tempmin=200
nombremin=0
sumatemperatutas=0

nombre=input("ingrese el nombre de la ciudad ")
temperatura=int(input("ingrese la temperatura "))
while(temperatura!=-50):
    while(temperatura<-50):
        print("la temperatura es invalida")
        temperatura=int(input("ingrese la temperatura "))
    canttemperatura=canttemperatura+1
    sumatemperatutas=sumatemperatutas+temperatura
    if (temperatura>30):
            canttempmayores=canttempmayores+1
    if (temperatura<tempmin):
            tempmin=temperatura
            nombremin=nombre
    nombre=input("ingrese el nombre de la ciudad ")
    temperatura=int(input("ingrese la temperatura "))
promedio=sumatemperatutas/canttemperatura
porcentaje=canttempmayores/canttemperatura*100

print("la cantidad de registrso ingresasdo es", canttemperatura)
print("el promedio de temperaturas es", promedio)
print("el porcentaje de ciudades con temperaturas superiores a 30°C es", porcentaje, "%")
print("el nombre de la ciudad con la temperatura más baja es", nombremin)