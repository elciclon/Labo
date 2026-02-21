# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import randint

def generala_tirar():
    tirada = []
    for i in range(5):
        tirada.append(randint(1,6))
        
    apariciones = {}
    
    for numero in tirada:
        apariciones[numero] = tirada.count(numero)
        
    apariciones_ordenadas = sorted(apariciones.items(), key=lambda x: x[1], reverse=True)
    if apariciones_ordenadas[0][1] == 5:
        print("Generala!")
        return tirada
    if apariciones_ordenadas[0][1] == 4:
        print("Poker!")
        return tirada
    if apariciones_ordenadas[0][1] == 3 and tirada.count(tirada[3]) == 2:
        print("Full!")
        return tirada
    if tirada == [1,2,3,4,5] or tirada == [2,3,4,5,6]:
        print("Escalera!")
        return tirada
                
    return tirada

print(generala_tirar())