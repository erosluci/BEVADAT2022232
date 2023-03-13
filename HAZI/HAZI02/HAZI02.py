import numpy as np


#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)


# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()


def column_swap(np_arr: np.array):
    return np_arr[:, ::-1]


# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlõek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlõ elemszámúakra kell csak hogy mûködjön


def compare_two_array(array1, array2):
    equal_indices = np.where(array1 == array2)[0]
    return equal_indices


# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még mûküdnie kell!, 


def get_array_shape(arr):
    shape = arr.shape
    
    if len(shape) == 1:
        return f"sor: {shape[0]}, oszlop: 1, melyseg: 1"
    elif len(shape) == 2:
        return f"sor: {shape[0]}, oszlop: {shape[1]}, melyseg: 1"
    elif len(shape) == 3:
        return f"sor: {shape[0]}, oszlop: {shape[1]}, melyseg: {shape[2]}"
    else:
        return f"{len(shape)} dimenziós array"


# Készíts egy olyan függvényt, aminek segítségével elõ tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-bõl. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()


def encode_Y(arr:np.array, num_classes) ->np.array:
    encoded_arr = np.zeros((len(arr), num_classes))
    for i in range(len(arr)):
        encoded_arr[i][arr[i]] = 1
    return encoded_arr


# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()


def decode_Y(y:np.array) ->np.array:
    decoded_y = np.argmax(y, axis=1)
    return decoded_y


# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()


def eval_classification(class_names, probabilities):
    return class_names[np.argmax(probabilities)]


# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()


def replace_odd_numbers(arr):
    arr[arr % 2 != 0] = -1
    return arr


# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függõen, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlõ, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()


def replace_by_value(arr, value):
    arr[arr < value] = -1
    arr[arr >= value] = 1
    return arr


# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza


import numpy as np

def array_multi(arr):
    return np.prod(arr)


# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()


def array_multi_2d(arr):
    return np.prod(arr, axis=1)


# Készíts egy olyan függvényt, amit egy meglévõ numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()



def add_border(arr):
    m, n = arr.shape
    bordered_arr = np.zeros((m+2, n+2))
    bordered_arr[1:m+1, 1:n+1] = arr
    return bordered_arr


# A KÖTVETKEZÕ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!


# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettõ paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()



from datetime import datetime, timedelta

def list_days(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m')
    end = datetime.strptime(end_date, '%Y-%m')
    num_days = (end - start).days + 1
    days = np.array([start + timedelta(days=i) for i in range(num_days)])
    return np.char.array(days.astype(str))


# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24


def get_act_date():
    return np.datetime64('today')


# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()


def sec_from_1970():
    epoch = np.datetime64('1970-01-01T00:02:00')
    now = np.datetime64('now')
    delta = now - epoch
    return int(delta / np.timedelta64(1, 's'))
