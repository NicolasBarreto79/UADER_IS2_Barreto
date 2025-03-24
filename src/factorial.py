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
    rango = input("Debe informar un rango (desde-hasta): ")
else:
    rango = sys.argv[1]

try:
    desde, hasta = map(int, rango.split('-'))
    if desde > hasta:
        print("El valor 'desde' debe ser menor o igual al valor 'hasta'")
    else:
        calcular_factoriales(desde, hasta)
except ValueError:
    print("Formato inválido. Use el formato desde-hasta (ej. 4-8)")
