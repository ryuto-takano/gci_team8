#!/usr/bin/python
# -*- coding: utf-8 -*-

from gensim.models import word2vec
import cython
from sqlalchemy import *
import pandas as pd


# fetch taglist from DB
engine_my = create_engine('mysql+mysqldb://pass:user@IP:port/db?charset=utf8&use_unicode=0',echo=False)
connection = engine_my.connect()
cur = connection.execute("select distinct(name) from tag;")
tags = []
for row in cur:
    # need to decode into python unicode because db preserves strings as utf-8
    # need to treat character sets altogether in one format
    tags.append(row["name"].decode('utf-8'))

connection.close()

# Import text file and make a corpus
data = word2vec.Text8Corpus('text_morpho.txt')

# Train input data by Word2Vec(in option below, take CBOW method)
# Take about 5 min when training ~11000 documents
model = word2vec.Word2Vec(data, size=100, window=5, min_count=5, workers=2)

# Save temporary files
model.save("W2V.model")

# make similar word list (dict type)
similar_words = []
for tag in tags:
    try:
        similar_word = model.most_similar(positive=tag)
        for i in range(10):
            similar = {}
            similar['tag'] = tag
            similar['similar_tag'] = similar_word[i][0]
            similar['score'] = similar_word[i][1]
            similar_words.append(similar)
    except:
        pass


# Conver dict into DataFrame to filter data easily
df_similar = pd.DataFrame.from_dict(similar_words)
df_similar_filtered = df_similar[df_similar['similar_tag'].isin(tags)]
df_similar = df_similar.ix[:,['tag', 'similar_tag', 'score']]
