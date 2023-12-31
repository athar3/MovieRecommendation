# -*- coding: utf-8 -*-
"""modeling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wmif6pSLzu7nrk3E_EzoNHaKsdX0_uon

# Movie Recommendation

link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

## import library
"""

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

"""## Load Dataset

Dataset ini terdiri dari 2 csv, yaitu `tmdb_5000_credits` dan `tmdb_5000_movies`
"""

dfc = pd.read_csv(r"datasiu\tmdb_5000_credits.csv")
dfm = pd.read_csv(r"datasiu\tmdb_5000_movies.csv")

"""## Data Understanding

### Exploratory Data Analysis
"""

dfc.head(5)

dfm.head(5)

dfm.isnull().sum()

dfc.isnull().sum()

print("Data Credits")
dfc.info()
print("\n\n====================================================================\n\n")
print("Data Movies")
dfm.info()

# nilai vote tertinggi
vote_terbesar = dfm["vote_average"].max()
dfm[dfm['vote_average'] == vote_terbesar]

# nilai vote terbanyak
vote_terbanyak = dfm["vote_count"].max()
dfm[dfm['vote_count'] == vote_terbanyak]

# paling populer
palingpopuler = dfm["popularity"].max()
dfm[dfm['popularity'] == palingpopuler]

# durasi paling lama
palinglama = dfm["runtime"].max()
dfm[dfm['runtime'] == palinglama]

# budget paling mahal
palingmahal = dfm["budget"].max()
dfm[dfm['budget'] == palingmahal]

# budget paling murah
palingmurah = dfm["budget"].min()
dfm[dfm['budget'] == palingmurah].head(3)

# paling menguntungkan
untung = dfm["revenue"].max()
dfm[dfm['revenue'] == untung]

dfm['original_language'].value_counts().plot(kind='pie')
plt.title('Bar Plot language')
plt.xlabel('language')
plt.ylabel('Jumlah')
plt.show()

"""## Data Preparation

### Menggabungkan 2 dataset
"""

dfc.columns = ['id','tittle','cast','crew']
df= dfm.merge(dfc,on='id')

df.head(5)

df.shape

"""### Drop Column"""

df.drop(["tittle", "keywords", "tagline", "homepage", "original_title", "spoken_languages"], inplace=True, axis=1)

df.nunique()

df.isnull().sum()

"""## Modelling"""

tfidf = TfidfVectorizer(stop_words='english')

#Replace NaN with an empty string
df['overview'] = df['overview'].fillna('')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(df['overview'])

#Output the shape of tfidf_matrix
tfidf_matrix.shape

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indicesf = pd.Series(df.index, index=df['title']).drop_duplicates()

def filmreq(title, cosine_sim=cosine_sim):
    print(f"hasil Rekomendasi berdasarkan film: {title}")
    # Get the index of the movie that matches the title
    idx = indicesf[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df['title'].iloc[movie_indices]

"""## Evaluation"""

judul = 'Avatar'
df[df['title'].eq(judul)]

filmreq(judul)