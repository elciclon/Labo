#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 20:23:37 2026

@author: adrian
"""


import pandas as pd
import duckdb as db
#%%
departamento = pd.read_csv('departamento.csv')
query = """SELECT descripcion FROM departamento;"""
db.sql(query)
#%%
query = """SELECT DISTINCT descripcion FROM departamento;"""
db.sql(query)
#%%
query = """SELECT DISTINCT id, descripcion FROM departamento;"""
db.sql(query)
#%%
query = """SELECT DISTINCT * FROM departamento;"""
db.sql(query)
#%%
query = """DESCRIBE departamento;"""
db.sql(query)
#%%
query = """SELECT DISTINCT id AS codigo_depto , descripcion AS nombre_depto FROM departamento;"""
db.sql(query)
#%%
query = """SELECT DISTINCT * FROM departamento WHERE id_provincia = 54;"""
db.sql(query)
#%%
query = """SELECT DISTINCT * FROM departamento WHERE id_provincia IN (22,78,86);"""
db.sql(query)
#%%
query = """SELECT DISTINCT * FROM departamento WHERE id_provincia BETWEEN 50 AND 59;"""
db.sql(query)
#%%
query = """SELECT DISTINCT * FROM departamento WHERE id_provincia >= 50 AND id_provincia <= 59;"""
db.sql(query)