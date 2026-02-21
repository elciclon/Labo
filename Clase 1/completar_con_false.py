#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 19:50:42 2026

@author: adrian
"""

import pandas as pd
import numpy as np

d = {'nombre':['Antonio', 'Brenda', 'Camila', 'David', 'Esteban', 'Felicitas'], 'apellido': ['Restrepo', 'Saenz', 'Torres', 'Urondo', 'Valdes', 'Wainstein'], 'lu': ['78/23', '449/22', '111/24', '1/21', '201/06', '47/20'], 'nota1': [9, 7, 7, 4, 3, np.nan], 'nota2': [10, 6, 7, 8, 5, np.nan], 'aprueba': [True, True, True, False, False, np.nan]}

df = pd.DataFrame(data = d) # creamos un df a partir de un diccionario
df.set_index('lu', inplace = True) # seteamos una columna como index

df.fillna(False)
df.replace({'nombre': {'David':'Daniel'}})
df['promedio'] = (df['nota1'] + df['nota2']) / 2
df['aprueba'].all()
df['aprueba'].any()
df.drop(['aprueba'], axis=1)
d2 = {'nombre':['Adrián', 'Patricio'], 'apellido':['Fernandez', 'Fazio'], 'lu':'938/24'}
df_nuevo = pd.DataFrame(data=d2) 
df_nuevo.set_index('lu', inplace = True) 
pd.concat([df, df_nuevo])
