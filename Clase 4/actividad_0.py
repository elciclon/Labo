#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:36:05 2026

@author: adrian
"""

def superanSalarioActividad01(M, umbral):
    matriz_filtrada = []
    for fila in M:
        if fila[3] > umbral:
            matriz_filtrada.append(fila)
            
    return matriz_filtrada
    

def superanSalarioActividad03(M, umbral):
    matriz_filtrada = []
    for fila in M:
        if fila[1] > umbral:
            matriz_filtrada.append([fila[0],fila[2],fila[3],fila[1]])

    return matriz_filtrada

def superanSalarioActividad04(M, umbral):
    matriz_cambiada = [[0 for _ in range(4)] for _ in range(5)]
    for i in range(4):
        for j in range(5):
            matriz_cambiada[j][i] = M[i][j]
    return superanSalarioActividad03(matriz_cambiada, 15000)

            
        
empleado_01 = [[20222333,45,2,20000],[33456234,40,0,25000],[45432345,41,1,10000]]
empleado_02 = [[20222333,45,2,20000],
               [33456234,40,0,25000],
               [45432345,41,1,10000],
               [43967304,37,0,12000],
               [42236276,36,0,18000]]

empleado_03 = [[20222333,20000, 45,2],
               [33456234,25000,40,0],
               [45432345,10000,41, 1],
               [43967304,12000,37,0],
               [42236276,18000, 6,0]]# la función ya no funciona

empleado_04 = [[20222333,33456234,45432345,43967304, 42236276],
               [20000,25000,10000,12000,18000],
               [45,40,41,37,36],
               [2,0,1,0,0]]
# Tardé 3 minutos
superanSalarioActividad01(empleado_03, 15000) #sigue funcionando
superanSalarioActividad03(empleado_03, 15000)
superanSalarioActividad04(empleado_04, 15000)

#1a nada
#1b Hubo que hacer cambios
#2 Hubo que restablecer la forma de la matriz para poder aplicar una función ya programada
#3 Puede reutilizarla todas las veces que quiera y no necesita saber cómo esta
#implementada 

