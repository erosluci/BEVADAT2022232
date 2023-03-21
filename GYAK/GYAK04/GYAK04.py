import pandas as pd
import matplotlib.pyplot as plt


'''
FONTOS: Az els� feladat�ltal visszaadott DataFrame-et kell haszn�lni a tov�bbi feladatokhoz. 
A f�ggv�nyeken bel�l mindig k�sz�ts egy m�solatot a bemen� df-r�l, (new_df = df.copy() �s ezzel dolgozz tov�bb.)
'''


'''
K�sz�ts egy f�ggv�nyt ami a bemeneti dictionary-b�l egy DataFrame-et ad vissza.
Egy p�lda a bemenetre: test_dict
Egy p�lda a kimenetre: test_df
return type: pandas.core.frame.DataFrame
f�ggv�ny neve: dict_to_dataframe
'''


stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }


def dict_to_dataframe(input: dict) -> pd.core.frame.DataFrame:
    df = pd.DataFrame(input)
    return df

df = dict_to_dataframe(stats)


'''
K�sz�ts egy f�ggv�nyt ami a bemeneti DataFrame-b�l vissza adja csak azt az oszlopot amelynek a neve a bemeneti string-el megegyez�.
Egy p�lda a bemenetre: test_df, 'area'
Egy p�lda a kimenetre: test_df
return type: pandas.core.series.Series
f�ggv�ny neve: get_column
'''


def get_column(input: pd.core.frame.DataFrame, tag:str) -> pd.core.series.Series:
    series = input[tag]
    return series



'''
K�sz�ts egy f�ggv�nyt ami a bemeneti DataFrame-b�l vissza adja a k�t legnagyobb ter�let� orsz�ghoz tartoz� sorokat.
Egy p�lda a bemenetre: test_df
Egy p�lda a kimenetre: test_df
return type: pandas.core.frame.DataFrame
f�ggv�ny neve: get_top_two
'''


def get_top_two(input: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    topDf = input[input['area'].isin(input['area'].nlargest(2))]
    return topDf




'''
K�sz�ts egy f�ggv�nyt ami a bemeneti DataFrame-b�l kisz�molja az orsz�gok n�ps�r�s�g�t �s elt�rolja az eredm�nyt egy �j oszlopba ('density').
(density = population / area)
Egy p�lda a bemenetre: test_df
Egy p�lda a kimenetre: test_df
return type: pandas.core.frame.DataFrame
f�ggv�ny neve: population_density
'''


def population_density(input: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    new_Df = input.copy()
    new_Df['density'] = new_Df['population'] / new_Df['area'] 
    return new_Df


'''
K�sz�ts egy f�ggv�nyt, ami a bemeneti Dataframe adatai alapj�n elk�sz�t egy olyan oszlopdiagramot (bar plot),
ami vizualiz�lja az orsz�gok n�pess�g�t.
Az oszlopdiagram c�me legyen: 'Population of Countries'
Az x tengely c�me legyen: 'Country'
Az y tengely c�me legyen: 'Population (millions)'
Egy p�lda a bemenetre: test_df
Egy p�lda a kimenetre: fig
return type: matplotlib.figure.Figure
f�ggv�ny neve: plot_population
'''


def plot_population(df: pd.DataFrame) -> plt.Figure:
    new_df = df.copy()
    fig, ax = plt.subplots()
    ax.bar(new_df['country'], new_df['population'])
    ax.set_title('Population of Countries')
    ax.set_xlabel('Country')
    ax.set_ylabel('Population (millions)')

    return fig
    



'''
K�sz�ts egy f�ggv�nyt, ami a bemeneti Dataframe adatai alapj�n elk�sz�t egy olyan k�rdiagramot,
ami vizualiz�lja az orsz�gok ter�let�t. Minden k�rcikknek legyen egy c�me, ami az orsz�g neve.
Az k�rdiagram c�me legyen: 'Area of Countries'
Egy p�lda a bemenetre: test_df
Egy p�lda a kimenetre: fig
return type: matplotlib.figure.Figure
f�ggv�ny neve: plot_area
'''


def plot_area(df: pd.DataFrame) -> plt.Figure:
    new_df = df.copy()
    fig, ax = plt.subplots()
    ax.pie(new_df['area'], labels=new_df['country'])
    ax.set_title('Area of Countries')

    return fig
