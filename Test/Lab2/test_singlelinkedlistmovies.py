import pytest
import config
from DataStructures import listiterator as it
from ADT import list as lt


#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'


def cmpfunction (element1, element2):
    if element1['id'] == element2['id']:
        return 0
    elif element1['id'] < element2['id']:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    lst = lt.newList('SINGLE_LINKED', cmpfunction)
    #lst = lt.newList('ARRAY_LIST', cmpfunction)
    return lst


@pytest.fixture
def movies ():
    movies = movies.append({'id':'1','budget':'1','genres':'genere 1','imdb_id':'1','original_language':'language 1','original_title':'Title 1','overview':'Overview 1','popularity':'1','production_companies':'production company 1','production_countries':'product contry 1','release_date':'1','revenue':'1','runtime':'1','spoken_languages':'language 1','status': 'status 1','tagline': 'tagline 1','title': 'title 1','vote_average': '1','vote_count':'1','production_companies_number':'1','production_countries_number':'1','spoken_languages_number':'1','actor1_name':'actor name 11','actor1_gender':'actor gender 11','actor2_name':'actor name 21','actor2_gender':'actor gender 21','actor3_name':'actor name 31','actor3_gender':'actor gender 31','actor4_name':'actor name 41','actor4_gender':'actor gender 41','actor5_name':'actor name 51','actor5_gender':'actor gender 51','actor_number':'actor number 1','director_name':'director number 1','director_gender': 'director gender 1', 'director_number':'director number 1','producer_name':'producer name 1','producer_number':'producer number 1','screeplay_name':'screenplay name 1','editor_name':'editor name 1'})
    movies = movies.append({'id':'2','budget':'2','genres':'genere 2','imdb_id':'2','original_language':'language 2','original_title':'Title 2','overview':'Overview 2','popularity':'2','production_companies':'production company 2','production_countries':'product contry 2','release_date':'2','revenue':'2','runtime':'2','spoken_languages':'language 2','status': 'status 2','tagline': 'tagline 2','title': 'title 2','vote_average': '2','vote_count':'2','production_companies_number':'2','production_countries_number':'2','spoken_languages_number':'2','actor1_name':'actor name 12','actor1_gender':'actor gender 12','actor2_name':'actor name 22','actor2_gender':'actor gender 22','actor3_name':'actor name 32','actor3_gender':'actor gender 32','actor4_name':'actor name 42','actor4_gender':'actor gender 42','actor5_name':'actor name 52','actor5_gender':'actor gender 52','actor_number':'actor number 2','director_name':'director number 2','director_gender': 'director gender 2', 'director_number':'director number 2','producer_name':'producer name 2','producer_number':'producer number 2','screeplay_name':'screenplay name 2','editor_name':'editor name 2'})
    movies = movies.append({'id':'3','budget':'3','genres':'genere 3','imdb_id':'3','original_language':'language 3','original_title':'Title 3','overview':'Overview 3','popularity':'3','production_companies':'production company 3','production_countries':'product contry 3','release_date':'3','revenue':'3','runtime':'3','spoken_languages':'language 3','status': 'status 3','tagline': 'tagline 3','title': 'title 3','vote_average': '3','vote_count':'3','production_companies_number':'3','production_countries_number':'3','spoken_languages_number':'3','actor1_name':'actor name 13','actor1_gender':'actor gender 13','actor2_name':'actor name 23','actor2_gender':'actor gender 23','actor3_name':'actor name 33','actor3_gender':'actor gender 33','actor4_name':'actor name 43','actor4_gender':'actor gender 43','actor5_name':'actor name 53','actor5_gender':'actor gender 53','actor_number':'actor number 3','director_name':'director number 3','director_gender': 'director gender 3', 'director_number':'director number 3','producer_name':'producer name 3','producer_number':'producer number 3','screeplay_name':'screenplay name 3','editor_name':'editor name 3'})
    movies = movies.append({'id':'4','budget':'4','genres':'genere 4','imdb_id':'4','original_language':'language 4','original_title':'Title 4','overview':'Overview 4','popularity':'4','production_companies':'production company 4','production_countries':'product contry 4','release_date':'4','revenue':'4','runtime':'4','spoken_languages':'language 4','status': 'status 4','tagline': 'tagline 4','title': 'title 4','vote_average': '4','vote_count':'4','production_companies_number':'4','production_countries_number':'4','spoken_languages_number':'4','actor1_name':'actor name 14','actor1_gender':'actor gender 14','actor2_name':'actor name 24','actor2_gender':'actor gender 24','actor3_name':'actor name 34','actor3_gender':'actor gender 34','actor4_name':'actor name 44','actor4_gender':'actor gender 44','actor5_name':'actor name 54','actor5_gender':'actor gender 54','actor_number':'actor number 4','director_name':'director number 4','director_gender': 'director gender 4', 'director_number':'director number 4','producer_name':'producer name 4','producer_number':'producer number 4','screeplay_name':'screenplay name 4','editor_name':'editor name 4'})
    movies = movies.append({'id':'5','budget':'5','genres':'genere 5','imdb_id':'5','original_language':'language 5','original_title':'Title 5','overview':'Overview 5','popularity':'5','production_companies':'production company 5','production_countries':'product contry 5','release_date':'5','revenue':'5','runtime':'5','spoken_languages':'language 5','status': 'status 5','tagline': 'tagline 5','title': 'title 5','vote_average': '5','vote_count':'5','production_companies_number':'5','production_countries_number':'5','spoken_languages_number':'5','actor1_name':'actor name 15','actor1_gender':'actor gender 15','actor2_name':'actor name 25','actor2_gender':'actor gender 25','actor3_name':'actor name 35','actor3_gender':'actor gender 35','actor4_name':'actor name 45','actor4_gender':'actor gender 45','actor5_name':'actor name 55','actor5_gender':'actor gender 55','actor_number':'actor number 5','director_name':'director number 5','director_gender': 'director gender 5', 'director_number':'director number 5','producer_name':'producer name 5','producer_number':'producer number 5','screeplay_name':'screenplay name 5','editor_name':'editor name 5'})   
    print (movies[0])
    return movies


@pytest.fixture
def lstmovies(movies):
    #lst = lt.newList('ARRAY_LIST', cmpfunction)
    lst = lt.newList('SINGLE_LINKED', cmpfunction)
    for i in range(0,5):    
        lt.addLast(lst,movies[i])    
    return lst


def test_empty (lst):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0




def test_addFirst (lst, movies):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addFirst (lst, movies[1])
    assert lt.size(lst) == 1
    lt.addFirst (lst, movies[2])
    assert lt.size(lst) == 2
    movie = lt.firstElement(lst)
    assert movie == movies[2]




def test_addLast (lst, movies):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addLast (lst, movies[1])
    assert lt.size(lst) == 1
    lt.addLast (lst, movies[2])
    assert lt.size(lst) == 2
    movie = lt.firstElement(lst)
    assert movie == movies[1]
    movie = lt.lastElement(lst)
    assert movie == movies[2]




def test_getElement(lstmovies, movies):
    movie = lt.getElement(lstmovies, 1)
    assert movie == movies[0]
    movie = lt.getElement(lstmovies, 5)
    assert movie == movies[4]




def test_removeFirst (lstmovies, movies):
    assert lt.size(lstmovies) == 5
    lt.removeFirst(lstmovies)
    assert lt.size(lstmovies) == 4
    movie = lt.getElement(lstmovies, 1)
    assert movie  == movies[1]



def test_removeLast (lstmovies, movies):
    assert lt.size(lstmovies) == 5
    lt.removeLast(lstmovies)
    assert lt.size(lstmovies) == 4
    movie = lt.getElement(lstmovies, 4)
    assert movie  == movies[3]



def test_insertElement (lst, movies):
    assert lt.isEmpty(lst) is True
    assert lt.size(lst) == 0
    lt.insertElement (lst, movies[0], 1)
    assert lt.size(lst) == 1
    lt.insertElement (lst, movies[1], 2)
    assert lt.size(lst) == 2
    lt.insertElement (lst, movies[2], 1)
    assert lt.size(lst) == 3
    movie = lt.getElement(lst, 1)
    assert movie == movies[2]
    movie = lt.getElement(lst, 2)
    assert movie == movies[0]



def test_isPresent (lstmovies, movies):
    movie =  {'id':'10','budget':'10','genres':'genere 10','imdb_id':'10','original_language':'language 10','original_title':'Title 10','overview':'Overview 10','popularity':'10','production_companies':'production company 10','production_countries':'product contry 10','release_date':'10','revenue':'10','runtime':'10','spoken_languages':'language 10','status': 'status 10','tagline': 'tagline 10','title': 'title 10','vote_average': '10','vote_count':'10','production_companies_number':'10','production_countries_number':'10','spoken_languages_number':'10','actor1_name':'actor name 110','actor1_gender':'actor gender 110','actor2_name':'actor name 210','actor2_gender':'actor gender 210','actor3_name':'actor name 310','actor3_gender':'actor gender 310','actor4_name':'actor name 410','actor4_gender':'actor gender 410','actor5_name':'actor name 510','actor5_gender':'actor gender 510','actor_number':'actor number 10','director_name':'director number 10','director_gender': 'director gender 10', 'director_number':'director number 10','producer_name':'producer name 10','producer_number':'producer number 10','screeplay_name':'screenplay name 10','editor_name':'editor name 10'}
    assert lt.isPresent (lstmovies, movies[2]) > 0
    assert lt.isPresent (lstmovies, movie) == 0
    


def test_deleteElement (lstmovies, movies):
    pos = lt.isPresent (lstmovies, movies[2])
    assert pos > 0
    movie = lt.getElement(lstmovies, pos)
    assert movie == movies[2]
    lt.deleteElement (lstmovies, pos)
    assert lt.size(lstmovies) == 4
    movie = lt.getElement(lstmovies, pos)
    assert movie == movies[3]



def test_changeInfo (lstmovies):
    movie10 ={'id':'10','budget':'10','genres':'genere 10','imdb_id':'10','original_language':'language 10','original_title':'Title 10','overview':'Overview 10','popularity':'10','production_companies':'production company 10','production_countries':'product contry 10','release_date':'10','revenue':'10','runtime':'10','spoken_languages':'language 10','status': 'status 10','tagline': 'tagline 10','title': 'title 10','vote_average': '10','vote_count':'10','production_companies_number':'10','production_countries_number':'10','spoken_languages_number':'10','actor1_name':'actor name 110','actor1_gender':'actor gender 110','actor2_name':'actor name 210','actor2_gender':'actor gender 210','actor3_name':'actor name 310','actor3_gender':'actor gender 310','actor4_name':'actor name 410','actor4_gender':'actor gender 410','actor5_name':'actor name 510','actor5_gender':'actor gender 510','actor_number':'actor number 10','director_name':'director number 10','director_gender': 'director gender 10', 'director_number':'director number 10','producer_name':'producer name 10','producer_number':'producer number 10','screeplay_name':'screenplay name 10','editor_name':'editor name 10'}
    lt.changeInfo (lstmovies, 1, movie10)
    movie = lt.getElement(lstmovies, 1)
    assert movie10 == movie


def test_exchange (lstmovies, movies):
    movie10 = lt.getElement(lstmovies, 1)
    movie5 = lt.getElement(lstmovies, 5)
    lt.exchange (lstmovies, 1, 5)
    assert lt.getElement(lstmovies, 1) == movie5
    assert lt.getElement(lstmovies, 5) == movie10
