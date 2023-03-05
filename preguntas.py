"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    import csv
    with open('data.csv', newline='') as File:  
        Datos = csv.reader(File)
        suma = 0
        for columnas in Datos:
            suma += int(columnas[0][2])
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return suma

def pregunta_02():
    with open('data.csv', newline='') as file: 
        Datos = file.readlines()
        Datos = [row.replace("\n", "") for row in Datos]
        Datos = [row.replace("\t", ",") for row in Datos]
        Datos = [row.replace("\r", "") for row in Datos]
        Datos = [row.split(",") for row in Datos]
        Datos = [row[0:2] for row in Datos]
        Datos.sort(key=lambda x: x[0])
        tuplas = [(tuple(lista)) for lista in Datos]
        suma = {}
        for letras, numero in Datos:
            if letras in suma:
                suma[letras] += 1
            else:
                suma[letras] = 1
        tuplas.clear()
        for clave, numero in suma.items():
            tuplas += [(clave,numero)]
      

    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return tuplas

def pregunta_03():
    with open('data.csv', newline='') as file: 
        Datos = file.readlines()
        Datos = [row.replace("\n", "") for row in Datos]
        Datos = [row.replace("\t", ",") for row in Datos]
        Datos = [row.replace("\r", "") for row in Datos]
        Datos = [row.split(",") for row in Datos]
        Datos = [row[0:2] for row in Datos]
        Datos.sort(key=lambda x: x[0])
        suma = {}
        for letras, numero in Datos:
            if letras in suma:
                suma[letras] += int(numero)
            else:
                suma[letras] = int(numero)
        Datos = [(key,value) for key , value in suma.items()]

            

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return Datos



def pregunta_04():
    import datetime
    with open('data.csv', newline='') as file: 
        Datos = file.readlines()
        Datos = [row.replace("\n", "") for row in Datos]
        Datos = [row.replace("\t", ",") for row in Datos]
        Datos = [row.replace("\r", "") for row in Datos]
        Datos = [row.split(",") for row in Datos]
        Datos = [row[2] for row in Datos]
        Datos = [(fechas[5:7]) for fechas in Datos]
        suma = {}
        for mes in Datos:
            if mes in suma:
                suma[mes] += 1
            else:
                suma[mes] = 1
        Datos = [(key,value) for key , value in suma.items()]
        Datos.sort(key=lambda x: x[0])
        
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return Datos

def pregunta_05():
    with open('data.csv', newline='') as file: 
        Datos = file.readlines()
        Datos = [row.replace("\n", "") for row in Datos]
        Datos = [row.replace("\t", ",") for row in Datos]
        Datos = [row.replace("\r", "") for row in Datos]
        Datos = [row.split(",") for row in Datos]
        Datos = [row[0:2] for row in Datos]
        maximo = {}
        minimo = {}
        for letras , valores in Datos:
            if letras not in maximo:
                maximo[letras] = int(valores) 
            else:
                max = maximo[letras]
                if int(valores) > max:
                    maximo[letras] = int(valores)
            if letras not in minimo:
                minimo[letras] = int(valores) 
            else:
                min = minimo[letras]
                if int(valores) < min:
                    minimo[letras] = int(valores)     
        Datos = [(letra,int(m),int(minimo[letra])) for letra, m in maximo.items()] 
        Datos.sort(key=lambda x: x[0])             
                


    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return Datos



def pregunta_06():
    import csv
    with open('data.csv', newline='') as file: 
        Datos = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        reader = csv.reader(file, Datos)
        Datos = [filas for filas in reader]
        Datos = [row[4] for row in Datos]
        Datos = [row.split(",") for row in Datos]
        maximo = {}
        minimo = {}
        for listas in Datos:
            for dict in listas:
                if dict[:3] not in maximo:
                    maximo[dict[0:3]] = int(dict[4:])
                else:
                    if int(dict[4:]) > maximo[dict[0:3]]:
                        maximo[dict[0:3]] = int(dict[4:])
                if dict[:3] not in minimo:
                    minimo[dict[0:3]] = int(dict[4:])
                else:
                    if int(dict[4:]) < minimo[dict[0:3]]:
                        minimo[dict[0:3]] = int(dict[4:])
        Datos = [(letra,int(minimo[letra]),int(m)) for letra, m in maximo.items()] 
        Datos.sort(key=lambda x: x[0]) 
        
        

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return Datos


def pregunta_07():
    import csv
    with open('data.csv', newline='') as file: 
        Datos = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        reader = csv.reader(file, Datos)
        Datos = [filas for filas in reader]
        Datos = [row[:2] for row in Datos]
        tuplas = {}
        for listas in Datos:
            if int(listas[1]) not in tuplas:
                tuplas[int(listas[1])] = [listas[0]]
            else:
                tuplas[int(listas[1])] += [listas[0]]
        Datos = list(tuplas.items())
        Datos = sorted(Datos, key=lambda x: (x[0], x[1]))


    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return Datos


def pregunta_08():
    import csv
    with open('data.csv', newline='') as file: 
        Datos = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        reader = csv.reader(file, Datos)
        Datos = [filas for filas in reader]
        Datos = [row[:2] for row in Datos]
        tuplas = {}
        for listas in Datos:
            if int(listas[1]) not in tuplas:
                tuplas[int(listas[1])] = [listas[0]]
            else:
                if listas[0] not in tuplas[int(listas[1])]:
                    tuplas[int(listas[1])] += [listas[0]]
        Datos = list(tuplas.items())
        Datos = sorted(Datos, key=lambda x: (x[0]))
        datos_ordenados = [(tupla[0], sorted(tupla[1])) for tupla in Datos]
        
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return datos_ordenados

def pregunta_09():

    import csv
    with open('data.csv', newline='') as file: 
        Datos = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        reader = csv.reader(file, Datos)
        Datos = [filas for filas in reader]
        Datos = [row[4] for row in Datos]
        Datos = [row.split(",") for row in Datos]
        contar = {}
        for listas in Datos:
            for dict in listas:
                if dict[:3] not in contar:
                    contar[dict[0:3]] = 1
                else:
                    contar[dict[0:3]] += 1
        retornar = {}
        for claves in sorted(contar.keys()):
            retornar[claves] = contar[claves]
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return retornar
def pregunta_10():
    import csv
    with open('data.csv', newline='') as file: 
        Datos = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        reader = csv.reader(file, Datos)
        Datos = [filas for filas in reader]
        Datos = [[row[0],row[3].split(","),row[4].split(",")] for row in Datos]
        Datos = [(row[0],len(row[1]),len(row[2])) for row in Datos]
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return Datos

def pregunta_11():
    import csv
    with open('data.csv', newline='') as file: 
        Datos = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        reader = csv.reader(file, Datos)
        Datos = [filas for filas in reader]
        Datos = [[int(row[1]),row[3].split(",")] for row in Datos]
        diccionario = {}
        for listas in Datos:
            for letras in listas[1]:
                if letras not in diccionario:
                    diccionario[letras] = listas[0]
                else:
                    diccionario[letras] += listas[0]
        retornar = {}
        for claves in sorted(diccionario.keys()):
            retornar[claves] = diccionario[claves]

        
        
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return retornar

def pregunta_12():
    import csv
    with open('data.csv', newline='') as file: 
        Datos = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        reader = csv.reader(file, Datos)
        Datos = [filas for filas in reader]
        Datos = [[row[0],row[4].split(",")] for row in Datos]
        D = {}
        for listas in Datos:
            if listas[0] not in D:
                D[listas[0]] = sum([int(elementos[4:]) for elementos in listas[1]])
            else:
                D[listas[0]] += sum([int(elementos[4:]) for elementos in listas[1]])
                retornar = {}
        for claves in sorted(D.keys()):
            retornar[claves] = D[claves]
    

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return retornar