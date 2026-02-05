# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase. 
Autor  : Pablo Turjanski
Fecha  : 2025-02-03
"""

# Importamos bibliotecas
import pandas as pd
import duckdb as dd


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = "/home/Estudiante/Descargas/Clases 06-08 - SQL - Archivos clase (template script + datos)-20260205/"

# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv(carpeta+"empleado.csv")
# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv(carpeta+"se_inscribe_en.csv")
materia       =pd.read_csv(carpeta+"materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
reserva    = pd.read_csv(carpeta+"reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv(carpeta+"examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv(carpeta+"examen03.csv")



#%%===========================================================================
# Ejemplo inicial
#=============================================================================

print(empleado)

consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-PROJECT <-> SELECT
#=============================================================================
# a.- Listar DNI y Salario de empleados 
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Listar Sexo de empleados 
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
#c.- Listar Sexo de empleados (sin DISTINCT)
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios AR-SELECT <-> WHERE
#=============================================================================
# a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
#b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios AR-RENAME <-> AS
#=============================================================================
#a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 01
#=============================================================================
# Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.2.- ¿Qué retorna 
#                       SELECT DISTINCT Ciudad AS City 
#                       FROM aeropuerto 
#                       WHERE Codigo='ORY' OR Codigo='CDG'; ?
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
#=============================================================================
# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT
#=============================================================================
# a1.- Listar a los alumnos que cursan BDs o TLENG

consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% -----------
# a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)

consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG

consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# c.- Listar a los alumnos que cursan BDs y no cursan TLENG 

consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#=============================================================================
#  EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 02
#=============================================================================
# Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)
consultaSQL = """
            SELECT DISTINCT numero
            FROM vuelo
        INTERSECT
            SELECT DISTINCT nrovuelo
            FROM reserva

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas
consultaSQL = """
                SELECT DISTINCT numero
                FROM vuelo
            EXCEPT
                SELECT DISTINCT nrovuelo
                FROM reserva

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos
consultaSQL = """

              """
              
dataframeResultado = dd.sql(consultaSQL).df()



#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#=============================================================================
# Ejercicios AR-... JOIN <-> ... JOIN
#=============================================================================
# a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades

consultaSQL = """
                SELECT DISTINCT *
                FROM persona
                CROSS JOIN nacionalidades

              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)

consultaSQL = """SELECT DISTINCT *
                FROM persona
                CROSS JOIN nacionalidades

              """

dataframeResultado = dd.query(consultaSQL).df()


#%% --------------------------------------------------------------------------------------------
# Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
# ----------------------------------------------------------------------------------------------
persona        = pd.read_csv(carpeta+"persona_ejemplosJoin.csv")
#%%
# ----------------------------------------------------------------------------------------------
# b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN

consultaSQL = """SELECT DISTINCT *
                FROM persona
                INNER JOIN nacionalidades
                ON Nacionalidad=IDN

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)

consultaSQL = """
                SELECT DISTINCT * 
                FROM persona, nacionalidades
                WHERE nacionalidad=IDN
              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN

consultaSQL = """
                SELECT DISTINCT *
                FROM persona
                LEFT OUTER JOIN nacionalidades
                ON nacionalidad = IDN

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - ¿Mismos Nombres?
#=============================================================================
# a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia

consultaSQL = """
                SELECT DISTINCT Lu, Nombre
                FROM se_inscribe_en AS i
                INNER JOIN materia AS m
                ON i.codigo_materia = m.codigo_materia

              """

dataframeResultado = dd.query(consultaSQL).df()

    
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 03
#=============================================================================
# Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165

consultaSQL = """
                SELECT DISTINCT ciudad
                FROM aeropuerto
                INNER JOIN vuelo
                ON codigo=origen
                WHERE numero=165

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200

consultaSQL = """
                SELECT DISTINCT nombre
                FROM pasajero AS p
                INNER JOIN reserva AS r
                ON p.DNI=r.DNI
                WHERE precio<200
                

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid

vuelosAMadrid = dd.query("""SELECT DISTINCT *
                       FROM vuelo 
                       WHERE origen = 'MAD' 

              """).df()

dniPersonasDesdeMadrid = dd.query("""
                                SELECT DISTINCT dni, destino, fecha
                                FROM vuelosAMadrid AS p
                                INNER JOIN reserva AS r
                                ON numero=NroVuelo
                                
                                
                                

               """).df()

consultaSQL = """SELECT Nombre, fecha, destino
                FROM dniPersonasDesdeMadrid AS d
                INNER JOIN pasajero as p
                ON d.DNI=p.DNI
               """

dataframeResultado = dd.query(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
#%%===========================================================================
# Ejercicios SQL - Join de varias tablas en simultáneo
#=============================================================================
# a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero.
    
consultaSQL = """
                SELECT DISTINCT r.Fecha, v.Salida, p.Nombre
                FROM reserva AS r, vuelo AS v, pasajero AS p
                WHERE r.DNI=p.DNI AND r.NroVuelo=v.numero
              """

dataframeResultado = dd.query(consultaSQL).df()

    
#%%===========================================================================
# Ejercicios SQL - Tuplas espúreas
#=============================================================================
# a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto
    
consultaSQL = """
                SELECT DISTINCT e.empleado, e.rol, r.proyecto
                FROM empleadoRol AS e
                INNER JOIN rolProyecto AS r
                ON e.rol=r.rol
              """

dataframeResultado = dd.query(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Funciones de agregación
#=============================================================================
# a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)
    
consultaSQL = """
                SELECT count(*) AS cantidadDeExamenes
                FROM examen
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia
    
consultaSQL = """
                SELECT Instancia, count(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)
    
consultaSQL = """SELECT Instancia, count(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
                ORDER BY Instancia DESC

              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes
    
consultaSQL = """SELECT Instancia, count(*) AS Asistieron
                FROM examen
                GROUP BY Instancia
                HAVING Asistieron < 4
                ORDER BY Instancia ASC

              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen
    

consultaSQL = """SELECT Instancia, avg(Nota) AS PromedioNota
                FROM examen
                GROUP BY Instancia
                HAVING Instancia LIKE 'Parcial%'
                ORDER BY Instancia ASC

              """

              

dataframeResultado = dd.query(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - LIKE")
#=============================================================================
# a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial.
    
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE.
    
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Eligiendo
#=============================================================================
# a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4).
    
consultaSQL = """
                SELECT Nombre,
                       Nota,
                       CASE WHEN Nota >= 4
                           THEN 'APROBÓ'
                           ELSE 'NO APROBÓ'
                       END AS Estado,
                       'Revisado x mi' AS chequeado
                FROM examen
                WHERE Instancia='Parcial-01'
                ORDER BY nombre

              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia.
    
consultaSQL = """
                SELECT Instancia,
                       CASE WHEN Nota >= 4
                           THEN 'APROBÓ'
                           ELSE 'NO APROBÓ'
                       END AS Estado,
                       count(*) AS Cantidad
                FROM examen
                GROUP BY Instancia, Estado
                ORDER BY Instancia, Estado

              """

dataframeResultado = dd.query(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Subqueries
#=============================================================================
#a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia

consultaSQL = """
                SELECT e1.nombre, e1.instancia, e1.nota
                FROM examen AS e1
                WHERE e1.Nota > (
                    SELECT AVG(e2.Nota)
                    FROM examen As e2
                    WHERE e2.instancia = e1.instancia)
                ORDER BY Instancia ASC, Nota DESC;
                
                
              """


dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia

consultaSQL = """
                SELECT e1.nombre, e1.instancia, e1.nota
                FROM examen AS e1
                WHERE e1.Nota >= ALL(
                    SELECT e2.Nota
                    FROM examen As e2
                    WHERE e2.instancia = e1.instancia)
                ORDER BY Instancia ASC, Nota DESC;
                              
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio

consultaSQL = """
                SELECT DISTINCT e1.nombre
                FROM examen AS e1
                WHERE e1.nombre NOT IN(
                    SELECT e2.nombre
                    FROM examen As e2
                    WHERE e2.instancia LIKE 'Recuperatorio%')
                ORDER BY nombre ASC
                              
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Integrando variables de Python
#=============================================================================
# a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota

umbralNota = 7

consultaSQL = """
                SELECT DISTINCT nombre, instancia, nota
                FROM examen
                WHERE nota > """ + str(umbralNota)
                

dataframeResultado = dd.query(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Manejo de NULLs
#=============================================================================
# a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9

consultaSQL = """
                SELECT DISTINCT *
                FROM examen03 
                WHERE nota < 9
              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9

consultaSQL = """
                SELECT DISTINCT *
                FROM examen03 
                WHERE nota >= 9
              """


dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9

consultaSQL = """
                SELECT DISTINCT *
                FROM examen03 
                WHERE nota >= 9 OR nota < 9
              """


dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# d1.- Obtener el promedio de notas

consultaSQL = """
                SELECT AVG(nota) AS PromedioNota
                FROM examen03

              """


dataframeResultado = dd.query(consultaSQL).df()


#%%-----------
# d2.- Obtener el promedio de notas (tomando a NULL==0)

consultaSQL = """
                SELECT AVG(CASE WHEN nota IS NULL THEN 0 ELSE Nota END) AS PromedioNota
                FROM examen03

              """


dataframeResultado = dd.query(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Mayúsculas/Minúsculas
#=============================================================================
# a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula

consultaSQL = """SELECT empleado, UPPER(rol) as rol
                FROM empleadoRol;
              """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula

consultaSQL = """SELECT empleado, LOWER(rol) as rol
                FROM empleadoRol;
              """

dataframeResultado = dd.query(consultaSQL).df()




#%%===========================================================================
# Ejercicios SQL - Reemplazos
#=============================================================================
# a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni

consultaSQL = """SELECT empleado, REPLACE(REPLACE(rol, 'ñ', 'ni'),'dor/a','dore') as rol
                FROM empleadoRol;
              """

dataframeResultado = dd.query(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Desafío
#=============================================================================
# a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, C

# ... Paso 1: Obtenemos los datos de los estudiantes
consultaSQL = """SELECT DISTINCT nombre, sexo, edad
               FROM examen         
           """
           
datosEstudiantes = dd.query(consultaSQL).df()   

consultaSQL = """SELECT DISTINCT de.*, nota As Parcial_01
                FROM datosEstudiantes AS de
                LEFT OUTER JOIN examen AS e
                ON de.Nombre=e.Nombre AND instancia='Parcial-01'
                """
                
auxParcial01 = dd.query(consultaSQL).df()

consultaSQL = """SELECT DISTINCT aux.*, nota As Parcial_01
                FROM auxParcial01 AS aux
                LEFT OUTER JOIN examen AS e
                ON aux.Nombre=e.Nombre AND instancia='Parcial-02'
                """
auxParcial02 = dd.query(consultaSQL).df()

consultaSQL = """SELECT DISTINCT aux.*, nota As Recuperatorio_01
                FROM auxParcial02 AS aux
                LEFT OUTER JOIN examen AS e
                ON aux.Nombre=e.Nombre AND instancia='Recuperatorio-01'
                """
auxRecu01= dd.query(consultaSQL).df()

consultaSQL = """SELECT DISTINCT aux.*, nota As Recuperatorio_02
                FROM auxRecu01 AS aux
                LEFT OUTER JOIN examen AS e
                ON aux.Nombre=e.Nombre AND instancia='Recuperatorio-02'
                """
auxRecu02= dd.query(consultaSQL).df()
# desafio_01 = dd.query(consultaSQL).df()



#%% -----------
# b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4.

consultaSQL = """SELECT DISTINCT *,
                CASE WHEN Nota >= 4
                THEN 'APROBÓ'
                ELSE 'NO APROBÓ'
                END AS Estado,
                FROM examen
                 
              """

desafio_02 = dd.query(consultaSQL).df()



#%% -----------
# c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior.

consultaSQL = """

              """

desafio_03 = dd.sql(consultaSQL).df()
