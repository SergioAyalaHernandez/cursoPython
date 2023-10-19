import math

numeros=int(input("escriba un número"))

while numeros<0:
    print("Ingrese un número positivo")
    numeros=int(input("escriba un número"))

print(f"El resultado de la raiz cuadrada es: {math.sqrt(numeros)}")
print(f"El resultado de la raiz cuadrada sin decimales: {math.sqrt(numeros):.0f}")

numero=0
while numero < 20:
    print(numero)
    numero+=1

