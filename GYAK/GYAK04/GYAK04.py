import pandas as pd
import matplotlib.pyplot as plt


'''
FONTOS: Az elsõ feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenõ df-rõl, (new_df = df.copy() és ezzel dolgozz tovább.)
'''


'''
Készíts egy függvényt ami a bemeneti dictionary-bõl egy DataFrame-et ad vissza.
Egy példa a bemenetre: test_dict
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: dict_to_dataframe
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
Készíts egy függvényt ami a bemeneti DataFrame-bõl vissza adja csak azt az oszlopot amelynek a neve a bemeneti string-el megegyezõ.
Egy példa a bemenetre: test_df, 'area'
Egy példa a kimenetre: test_df
return type: pandas.core.series.Series
függvény neve: get_column
'''


def get_column(input: pd.core.frame.DataFrame, tag:str) -> pd.core.series.Series:
    series = input[tag]
    return series



'''
Készíts egy függvényt ami a bemeneti DataFrame-bõl vissza adja a két legnagyobb területû országhoz tartozó sorokat.
Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: get_top_two
'''


def get_top_two(input: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    topDf = input[input['area'].isin(input['area'].nlargest(2))]
    return topDf




'''
Készíts egy függvényt ami a bemeneti DataFrame-bõl kiszámolja az országok népsûrûségét és eltárolja az eredményt egy új oszlopba ('density').
(density = population / area)
Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: population_density
'''


def population_density(input: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    new_Df = input.copy()
    new_Df['density'] = new_Df['population'] / new_Df['area'] 
    return new_Df


'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlopdiagramot (bar plot),
ami vizualizálja az országok népességét.
Az oszlopdiagram címe legyen: 'Population of Countries'
Az x tengely címe legyen: 'Country'
Az y tengely címe legyen: 'Population (millions)'
Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_population
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
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja az országok területét. Minden körcikknek legyen egy címe, ami az ország neve.
Az kördiagram címe legyen: 'Area of Countries'
Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_area
'''


def plot_area(df: pd.DataFrame) -> plt.Figure:
    new_df = df.copy()
    fig, ax = plt.subplots()
    ax.pie(new_df['area'], labels=new_df['country'])
    ax.set_title('Area of Countries')

    return fig
