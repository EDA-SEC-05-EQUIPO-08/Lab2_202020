"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este1 módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import insertionsort as insort
from Sorting import selectionsort as sort
from Sorting import shellsort
from time import process_time 

def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
   
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def loadCSVFile_2_at_once (file,file_1, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
   
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            with open(file_1, encoding="utf-8") as csvfile2:
                countrdr = csv.DictReader(csvfile, dialect=dialect)
                totalrows = 0
                for row in countrdr:
                    totalrows += 1
                csvfile.seek(0)
                spamreader1 = csv.DictReader(csvfile2, dialect=dialect)
                for i in range(0,totalrows): 
                    lt.addLast(lst,{**next(spamreader),**next(spamreader1)})
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst




     

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar operacion 5")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    
    Retorna el numero de películas buenas o con votación positiva y el promedio de la votación  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    
    if lt.isEmpty(lst):
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        prom=0 #Promedio de votos por director
        iterator = it.newIterator(lst)
        size=lt.size(lst)
        res=lt.newList("ARRAY_LIST")
        res1=lt.newList("ARRAY_LIST")
        for i in range (0,size):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por director  
                    counter+=1
                    lt.addLast(res1,element['title'])
                    prom+=float(element["vote_average"])
        prom*=1/counter
        lt.addLast(res,prom)
        lt.addLast(res,counter)
        lt.addLast(res,res1)
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return res

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        #Organiza la lista 
        #usa insertion sort
        #insort.insertionSort(lst, function,column)
        #usa selection sort
        #sort.selectionSort(lst,function,column)
        #usa shell sort
        shellsort.shellSort(lst,function,column)
        iterator = it.newIterator(lst)
        
        res=lt.newList()
        for i in range (0,elements):
            element = it.next(iterator)
            res1=lt.newList()
            lt.addLast(res1,element[column])
            lt.addLast(res1,element['title'])
            lt.addLast(res,res1)
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return res



def less(element1, element2,criterio='vote_count'):
    if criterio=='vote_count':
        if int(element1['vote_count']) < int(element2['vote_count']):
          return True
        return False
        
    elif criterio=='vote_average':
        if float(element1['vote_average']) < float(element2['vote_average']):
          return True
        return False
    else: False

def greater(element1, element2,criterio='COUNT'):
    if criterio=='vote_count':
        if int(element1['vote_count']) > int(element2['vote_count']):
          return True
        return False
        
    elif criterio=='vote_average':
        if float(element1['vote_average']) > float(element2['vote_average']):
          return True
        return False
    else: False

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista=lt.newList('ARRAY_LIST')
                lista_casting=lt.newList()
                lista_details=lt.newList()
                t1_start=process_time()
                lista=loadCSVFile_2_at_once("Data/Kaggle/AllMoviesDetailsCleaned.csv","Data/Kaggle/AllMoviesCastingRaw.csv")
                #lista=loadCSVFile_2_at_once("Data/Kaggle/SmallMoviesDetailsCleaned.csv","Data/Kaggle/MoviesCastingRaw-small.csv")
                """
                lista_details= loadCSVFile("Data/Kaggle/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                lista_casting= loadCSVFile("Data/Kaggle/MoviesCastingRaw-small.csv") #llamar funcion cargar datos
                 #unir dicionarios.
                for i in range(0,lt.size(lista_casting)):
                     details=lt.getElement(lista_details,i)
                     casting=lt.getElement(lista_casting,i)
                     lt.addLast(lista,{**lt.getElement(lista_details,i), **lt.getElement(lista_casting,i)})
                """
                t1_stop = process_time() #tiempo final
                print("Tiempo de ejecución union de datos",t1_stop-t1_start," segundos")
                print("Datos cargados, "+str(lt.size(lista))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                criteria =input('Ingrese el nombre del director\n')
                datos=countElementsByCriteria(criteria, "director_name", lista) #filtrar una columna por criterio  
                print("Hay %r peliculas buenas del director %r ; el promedio del director es %r " % (datos[1],criteria,datos[0]))
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    res=lt.newList()
                    res=countElementsByCriteria(criteria,'director_name',lista)
                    title=lt.lastElement(res)
                    print("El director %s ha filmado %i peliculas y tiene una calificacion promedio de %f " % (criteria,lt.getElement(res,2),lt.getElement(res,1)))
                    for i in range (1,lt.size(title)+1):
                        print("-%s"%lt.getElement(title,i))
                
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    res=lt.newList()
                    print("Criterio de busqueda:  \n 1-Votos \n 2-Promedio")
                    criteria =input('Ingrese el criterio de búsqueda\n:')
                    if criteria=='1':
                        column='vote_count' 
                        criteria='conteo'
                        print("Criterio de busqueda:  \n 1-Peores peliculas segun %s \n 2-Mejores peliculas segun %s" %(criteria,criteria))
                        criteria =input('Ingrese el criterio de búsqueda\n:')
                        if criteria=='1':
                            function='less'
                            criteria =input('Cuantas peliculas desea ver: ')
                            if int(criteria) >=10:
                                numero_de_peliculas=int(criteria)
                                res=orderElementsByCriteria(less, column, lista, numero_de_peliculas)
                                for i in range (1,numero_de_peliculas+1): 
                                    res2=lt.getElement(res,i)
                                    title=lt.getElement(res2,2)
                                    count=lt.getElement(res2,1)
                                    print("-%s con un conteo de votos de %s" %(title,count))
                            else:
                                print('Debe ser un numero mayor a 10')
                        elif criteria=='2':
                            function='greater'
                            criteria =input('Cuantas peliculas desea ver: ')
                            if int(criteria) >=10:
                                numero_de_peliculas=int(criteria)
                                res=orderElementsByCriteria(greater, column, lista, numero_de_peliculas)
                                for i in range (1,numero_de_peliculas+1): 
                                    res2=lt.getElement(res,i)
                                    title=lt.getElement(res2,2)
                                    count=lt.getElement(res2,1)
                                    print("-%s con un conteo de votos de %s" %(title,count))
                            else:
                                print('Debe ser un numero mayor a 10')
                        else:
                            print ('Opción invalida') 
                                      
                    elif criteria=='2':
                        column='vote_average'
                        print("Criterio de busqueda:  \n 1-Peores peliculas segun %s \n 2-Mejores peliculas segun %s"%(column,column))
                        criteria =input('Ingrese el criterio de búsqueda\n:')
                        if criteria=='1':
                            function='less'   
                            criteria =input('Cuantas peliculas desea ver: ')
                            if int(criteria) >=10:
                                numero_de_peliculas=int(criteria)
                                res=orderElementsByCriteria(less, column, lista, numero_de_peliculas)
                                for i in range (1,numero_de_peliculas+1): 
                                    res2=lt.getElement(res,i)
                                    title=lt.getElement(res2,2)
                                    count=lt.getElement(res2,1)
                                    print("-%s con un promedio de %s" %(title,count))
                            else:
                                print('Debe ser un numero mayor a 10')         
                        elif criteria=='2':
                            function='greater'
                            criteria =input('Cuantas peliculas desea ver: ')
                            if int(criteria) >=10:
                                numero_de_peliculas=int(criteria)
                                res=orderElementsByCriteria(greater, column, lista, numero_de_peliculas)
                                for i in range (1,numero_de_peliculas+1): 
                                    res2=lt.getElement(res,i)
                                    title=lt.getElement(res2,2)
                                    count=lt.getElement(res2,1)
                                    print("-%s con un promedio de %s" %(title,count))
                            else:
                                print('Debe ser un numero mayor a 10')
                        else:
                            print ('Opción invalida')   
                    else:
                        print ('Opción invalida')
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
if __name__ == "__main__":
    main()