import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# FONTOS: Az els� feladat�ltal visszaadott DataFrame-et kell haszn�lni a tov�bbi feladatokhoz. 
# A f�ggv�nyeken bel�l mindig k�sz�ts egy m�solatot a bemen� df-r�l, (new_df = df.copy() �s ezzel dolgozz tov�bb.)



# K�sz�ts egy f�ggv�nyt, ami egy string �tvonalat v�r param�terk�nt, �s egy DataFrame ad visszat�r�si �rt�kk�nt.
# Egy p�lda a bemenetre: 'test_data.csv'
# Egy p�lda a kimenetre: df_data
# return type: pandas.core.frame.DataFrame
# f�ggv�ny neve: csv_to_df


def csv_to_df(path):
    performance_df = pd.read_csv(path)
    return performance_df



# K�sz�ts egy f�ggv�nyt, ami egy DataFrame-et v�r param�terk�nt, 
# �s �talak�tja azoknak az oszlopoknak a nev�t nagybet�sre amelyiknek neve nem tartalmaz 'e' bet�t.
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: df_data_capitalized
# return type: pandas.core.frame.DataFrame
# f�ggv�ny neve: capitalize_columns


def capitalize_columns(df_data):
    df_data_capitalized = df_data.copy()
    df_data_capitalized.columns = [col.upper() if 'e' not in col and 'E' not in col else col for col in df_data_capitalized.columns]
    return df_data_capitalized


# K�sz�ts egy f�ggv�nyt, ahol egy sz�m form�j�ban vissza adjuk, hogy h�ny darab di�knak siker�lt teljes�teni a matek vizsg�t.
# (legyen az �tmen� ponthat�r 50).
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: 5
# return type: int
# f�ggv�ny neve: math_passed_count



def math_passed_count(df_data) -> int:
    df_copy = df_data.copy()
    count = 0
    for score in df_copy["math score"]:
        if score >= 50:
            count += 1
    return count



# K�sz�ts egy f�ggv�nyt, ahol Dataframe k�nt vissza adjuk azoknak a di�koknak az adatait (sorokat), akik v�geztek el�zetes gyakorl� kurzust.
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: df_did_pre_course
# return type: pandas.core.frame.DataFrame
# f�ggv�ny neve: did_pre_course


def did_pre_course(df_data):
    df_copy = df_data.copy()
    df_did_pre_course = df_copy[df_copy['test preparation course'] == "completed"] 

    return df_did_pre_course


# K�sz�ts egy f�ggv�nyt, ahol a bemeneti Dataframet a di�kok sz�lei v�gzetts�gi szintjei alapj�n csoportos�t�sra ker�l,
# majd aggreg�ci�k�nt vegy�k, hogy �tlagosan milyen pontsz�mot �rtek el a di�kok a vizsg�kon.
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: df_average_scores
# return type: pandas.core.frame.DataFrame
# f�ggv�ny neve: average_scores



def average_scores(df_data):
    df_copy = df_data.copy()
    df_average_scores = df_copy.groupby("parental level of education")["math score", "reading score", "writing score"].mean()

    return df_average_scores



# K�sz�ts egy f�ggv�nyt, ami a bementeti Dataframet kieg�sz�ti egy 'age' oszloppal, t�lts�k fel random 18-66 �v k�z�tti �rt�kekkel.
# A random.randint() f�ggv�nyt haszn�ld, a random sorsol�s legyen seedleve, ennek �rt�ke legyen 42.
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: df_data_with_age
# return type: pandas.core.frame.DataFrame
# f�ggv�ny neve: add_age



def add_age(df_data: pd.DataFrame)->pd.DataFrame:
    df_copy=df_data.copy()
    np.random.seed(42)
    ages=np.random.randint(18,67,size=len(df_copy))
    df_copy['age']=ages
    return df_copy



# K�sz�ts egy f�ggv�nyt, ami vissza adja a legjobb teljes�tm�nyt el�r� n�i di�k pontsz�mait.
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: (99,99,99) #math score, reading score, writing score
# return type: tuple
# f�ggv�ny neve: female_top_score



def female_top_score(df_data) -> tuple:
    df_copy = df_data.copy()
    df_sortByScores = df_copy.sort_values(["math score", "reading score", "writing score"], ascending = [False, False, False])
    topScoredFemale = df_sortByScores[df_sortByScores.gender == "female"].iloc[0]
    bestFameleScores = (topScoredFemale["math score"], topScoredFemale["reading score"], topScoredFemale["writing score"])
    return bestFameleScores




# K�sz�ts egy f�ggv�nyt, ami a bementeti Dataframet kieg�sz�ti egy 'grade' oszloppal. 
# Sz�moljuk ki hogy a di�kok h�ny sz�zal�kot ((math+reading+writing)/300) �rtek el a vizsg�n, �s oszt�lyozzuk �ket az al�bbi szempontok szerint:
# 90-100%: A
# 80-90%: B
# 70-80%: C
# 60-70%: D
# <60%: F
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: df_data_with_grade
# return type: pandas.core.frame.DataFrame
# f�ggv�ny neve: add_grade



def add_grade(df_data) -> tuple:
    df_data_with_grade = df_data.copy()
    df_data_with_grade["score percentage"] = (df_data_with_grade["math score"] + df_data_with_grade["reading score"] + df_data_with_grade["writing score"]) / 300
    df_data_with_grade["grade"] = df_data_with_grade["score percentage"].apply(lambda score: "A" if score >= 0.9 else "B" if score >= 0.8 else "C" if score >= 0.7 else "D" if score >= 0.6 else "F")
    del df_data_with_grade["score percentage"] 

    return df_data_with_grade


# K�sz�ts egy f�ggv�nyt, ami a bemeneti Dataframe adatai alapj�n elk�sz�t egy olyan oszlop diagrammot,
# ami vizualiz�lja a nemek �ltal el�rt �tlagos matek pontsz�mot.
# Oszlopdiagram c�me legyen: 'Average Math Score by Gender'
# Az x tengely c�me legyen: 'Gender'
# Az y tengely c�me legyen: 'Math Score'
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: fig
# return type: matplotlib.figure.Figure
# f�ggv�ny neve: math_bar_plot



def math_bar_plot(df_data):
    gender_scores  = df_data.copy().groupby("gender")["math score"].mean()
    fig, ax = plt.subplots()
    ax.bar(gender_scores.index, gender_scores.values)
    ax.set_xlabel("Gender")
    ax.set_ylabel("Math Score")
    plt.title("Average Math Score by Gender")

    return fig



# K�sz�ts egy f�ggv�nyt, ami a bemeneti Dataframe adatai alapj�n elk�sz�t egy olyan histogramot,
# ami vizualiz�lja az el�rt �r�sbeli pontsz�mokat.
# A histogram c�me legyen: 'Distribution of Writing Scores'
# Az x tengely c�me legyen: 'Writing Score'
# Az y tengely c�me legyen: 'Number of Students'
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: fig
# return type: matplotlib.figure.Figure
# f�ggv�ny neve: writing_hist



def writing_hist(df_data: pd.DataFrame)->plt.figure:
    df_copy=df_data.copy()
    fig, ax = plt.subplots()
    fig=df_copy.plot.hist(column='writing score'
                          ,xlabel='Writing Score',
                          ylabel='Number of Students',
                          title='Distribution of Writing Scores',
                          ax=ax,fig = fig)

    return fig


# K�sz�ts egy f�ggv�nyt, ami a bemeneti Dataframe adatai alapj�n elk�sz�t egy olyan k�rdiagramot,
# ami vizualiz�lja a di�kok etnikum csoportok szerinti eloszl�s�t sz�zal�kosan.
# �rdemes megsz�molni a di�kok sz�m�t, etnikum csoportonk�nt,majd a sz�zal�kos kirajzol�st az autopct='%1.1f%%' param�terrel megadhat�.
# Mindegyik k�r szelethez tartozzon egy c�mke, ami a csoport nev�t tartalmazza.
# A diagram c�me legyen: 'Proportion of Students by Race/Ethnicity'
# Egy p�lda a bemenetre: df_data
# Egy p�lda a kimenetre: fig
# return type: matplotlib.figure.Figure
# f�ggv�ny neve: ethnicity_pie_chart

def ethnicity_pie_chart(test_df):
    ethnicities = test_df.groupby("race/ethnicity")["race/ethnicity"].count()
    fig, ax = plt.subplots()
    ax.pie(ethnicities.values, labels = ethnicities.index, autopct="%0.01f%%")
    plt.title("Proportion of Students by Race/Ethnicity")

    return fig


