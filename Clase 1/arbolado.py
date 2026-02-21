#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 19:46:33 2026

@author: adrian
"""
import pandas as pd
archivo = "arbolado-en-espacios-verdes.csv"
df = pd.read_csv(archivo)
df_jacaranda = df[df['nombre_com'] == 'Jacarandá']
df_palo_borracho = df[df['nombre_com'] == 'Palo borracho rosado']
cantidad_jacarandas = (df_jacaranda['id_especie'] == 11).sum()
cantidad_palos_borrachos = (df_palo_borracho['id_especie'] == 25).sum()
#%%
df_jacaranda['altura_tot'].max()
df_palo_borracho['altura_tot'].max()
df_jacaranda['altura_tot'].min()
df_palo_borracho['altura_tot'].min()
df_jacaranda['altura_tot'].mean()
df_palo_borracho['altura_tot'].mean()
df_jacaranda['altura_tot'].agg(['max', 'min', 'mean'])
df_palo_borracho['altura_tot'].agg(['max', 'min', 'mean'])
df_jacaranda['diametro'].max()
df_palo_borracho['diametro'].max()
df_jacaranda['diametro'].min()
df_palo_borracho['diametro'].min()
df_jacaranda['diametro'].mean()
df_palo_borracho['diametro'].mean()
df_jacaranda['diametro'].agg(['max', 'min', 'mean'])
df_palo_borracho['diametro'].agg(['max', 'min', 'mean'])
#%%
# df['espacio_ve'] == 'AVELLANEDA'

def cantidad_arboles(parque):
    return (df['espacio_ve'] == parque).sum()

print(cantidad_arboles('AVELLANEDA, NICOLÁS, Pres.'))
print(cantidad_arboles('DE LAS VICTORIAS'))
#%%
def cantidad_nativos(parque):
    return ((df['espacio_ve'] == parque) & (df['origen'] == 'Nativo/Autóctono')).sum()

print(cantidad_nativos('AVELLANEDA, NICOLÁS, Pres.'))
print(cantidad_nativos('DE LAS VICTORIAS'))
