#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

def calcular_factoriales(desde, hasta):
    for num in range(desde, hasta + 1):
        print(f"Factorial {num}! es {factorial(num)}")

if len(sys.argv) < 2:
    num = int(input("Debe informar un número: "))
    rango = input("Debe informar un rango (desde-hasta): ")
else:
    num = int(sys.argv[1])
    rango = sys.argv[2] if len(sys.argv) > 2 else ""

print("Factorial", num, "! es", factorial(num))

try:
    if "-" in rango:
        partes = rango.split('-')
        desde = int(partes[0]) if partes[0] else 1  # Si falta 'desde', usa 1
        hasta = int(partes[1]) if partes[1] else 60  # Si falta 'hasta', usa 60
        
        if desde > hasta:
            print("El valor 'desde' debe ser menor o igual al valor 'hasta'")
        else:
            calcular_factoriales(desde, hasta)
    else:
        print("Formato inválido. Use el formato desde-hasta (ej. 4-8, -10, 5-)")
except ValueError:
    print("Formato inválido. Use el formato desde-hasta (ej. 4-8, -10, 5-)")

#comentario de prueba 