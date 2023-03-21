import numpy as np


#FONTOS!!!

# CSAK OTT LEHET HASZN�LNI FOR LOOP-OT AHOL A FELADAT K�L�N K�RI!
# [1,2,3,4] --> ezek az �rt�kek np.array-ek. Ahol list�t k�rek param�terk�nt ott k�l�n ki fogom emelni!
# Ha v�gezt�l a feladatokkal, akkor notebook-ot alak�tsd �t .py.
# A F�JLBAN CSAK A F�GGV�NYEK LEGYENEK! (KOMMENTEK MARADHATNAK)


# �rj egy olyan f�gv�nyt, ami megford�tja egy 2d array oszlopait. Bemenetk�nt egy array-t v�r.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()


def column_swap(np_arr: np.array):
    return np_arr[:, ::-1]


# K�sz�ts egy olyan f�ggv�nyt ami �sszehasonl�t k�t array-t �s adjon vissza egy array-ben, hogy hol egyenl�ek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenl� elemsz�m�akra kell csak hogy m�k�dj�n


def compare_two_array(array1, array2):
    equal_indices = np.where(array1 == array2)[0]
    return equal_indices


# K�sz�ts egy olyan f�ggv�nyt, ami vissza adja string-k�nt a megadott array dimenzi�it:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel m�g m�k�dnie kell!, 


def get_array_shape(arr):
    shape = arr.shape
    
    if len(shape) == 1:
        return f"sor: {shape[0]}, oszlop: 1, melyseg: 1"
    elif len(shape) == 2:
        return f"sor: {shape[0]}, oszlop: {shape[1]}, melyseg: 1"
    elif len(shape) == 3:
        return f"sor: {shape[0]}, oszlop: {shape[1]}, melyseg: {shape[2]}"
    else:
        return f"{len(shape)} dimenzi�s array"


# K�sz�ts egy olyan f�ggv�nyt, aminek seg�ts�g�vel el� tudod �ll�tani egy neur�lis h�l�zat tan�t�s�hoz sz�ks�ges pred-et egy numpy array-b�l. 
# Bementk�nt add meg az array-t, illetve hogy mennyi class-od van. Kimenetk�nt pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden null�kkal teli legyen �s csak ott �lljon egyes, ahol a bementi t�mb megjel�li. 
# Pl. ha 1 van a bemeneten �s 4 classod van, akkor az adott sorban az array-ban a [1] helyen �lljon egy 1-es, a t�bbi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()


def encode_Y(arr:np.array, num_classes) ->np.array:
    encoded_arr = np.zeros((len(arr), num_classes))
    for i in range(len(arr)):
        encoded_arr[i][arr[i]] = 1
    return encoded_arr


# A fenti feladatnak val�s�tsd meg a ki�rt�kel�s�t. Adj meg a 2d array-t �s adj vissza a decodolt v�ltozat�t
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()


def decode_Y(y:np.array) ->np.array:
    decoded_y = np.argmax(y, axis=1)
    return decoded_y


# K�sz�ts egy olyan f�ggv�nyt, ami k�pes ki�rt�kelni egy neur�lis h�l� eredm�ny�t! Bemenetk�nt egy list�t �s egy array-t �s adja vissza azt az elemet, aminek a legnagyobb a val�sz�n�s�ge(�rt�ke) a list�b�l.
# Be: ['alma', 'k�rte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'k�rte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()


def eval_classification(class_names, probabilities):
    return class_names[np.argmax(probabilities)]


# K�sz�ts egy olyan f�ggv�nyt, ahol az 1D array-ben a p�ratlan sz�mokat -1-re cser�li
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()


def replace_odd_numbers(arr):
    arr[arr % 2 != 0] = -1
    return arr


# K�sz�ts egy olyan f�ggv�nyt, ami egy array �rt�keit -1 �s 1-re v�ltoztatja, att�l f�gg�en, hogy az adott elem nagyobb vagy kisebb a param�terk�nt megadott sz�mn�l.
# Ha a sz�m kisebb mint a megadott �rt�k, akkor -1, ha nagyobb vagy egyenl�, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()


def replace_by_value(arr, value):
    arr[arr < value] = -1
    arr[arr >= value] = 1
    return arr


# K�sz�ts egy olyan f�ggv�nyt, ami egy array �rt�keit �sszeszorozza �s az eredm�nyt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha t�bb dimenzi�s a t�mb, akkor az eg�sz t�mb elemeinek szorzat�val t�rjen vissza


import numpy as np

def array_multi(arr):
    return np.prod(arr)


# K�sz�ts egy olyan f�ggv�nyt, ami egy 2D array �rt�keit �sszeszorozza �s egy olyan array-el t�r vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()


def array_multi_2d(arr):
    return np.prod(arr, axis=1)


# K�sz�ts egy olyan f�ggv�nyt, amit egy megl�v� numpy array-hez k�sz�t egy bordert null�sokkal. Bementk�nt egy array-t v�rjon �s kimenetk�nt egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()



def add_border(arr):
    m, n = arr.shape
    bordered_arr = np.zeros((m+2, n+2))
    bordered_arr[1:m+1, 1:n+1] = arr
    return bordered_arr


# A K�TVETKEZ� FELADATOKHOZ N�ZZ�TEK MEG A NUMPY DATA TYPE-J�T!


# K�sz�ts egy olyan f�ggv�nyt ami k�t d�tum k�z�tt felsorolja az �sszes napot �s ezt adja vissza egy numpy array-ben. A fgv k�nt str v�r param�terk�nt 'YYYY-MM' form�ban.
# Be: '2023-03', '2023-04'  # mind a kett� param�ter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()



from datetime import datetime, timedelta

def list_days(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m')
    end = datetime.strptime(end_date, '%Y-%m')
    num_days = (end - start).days + 1
    days = np.array([start + timedelta(days=i) for i in range(num_days)])
    return np.char.array(days.astype(str))


# �rj egy f�gv�nyt ami vissza adja az aktu�lis d�tumot az al�bbi form�ban: YYYY-MM-DD. T�rjen vissza egy 'numpy.datetime64' t�pussal.
# Be:
# Ki: 2017-03-24


def get_act_date():
    return np.datetime64('today')


# �rj egy olyan f�ggv�nyt ami visszadja, hogy mennyi m�sodperc telt el 1970 janu�r 01. 00:02:00 �ta. Int-el t�rjen vissza
# Be: 
# Ki: m�sodpercben az id�, int-� kasztolva
# sec_from_1970()


def sec_from_1970():
    epoch = np.datetime64('1970-01-01T00:02:00')
    now = np.datetime64('now')
    delta = now - epoch
    return int(delta / np.timedelta64(1, 's'))
