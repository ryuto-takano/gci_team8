# -*- coding: utf-8 -*-
#python posi_nega.py hogehoge.model [positive word] [negative word]

from gensim.models import word2vec
import sys

model   = word2vec.Word2Vec.load(sys.argv[1])
#results = model.most_similar(positive=sys.argv[2], topn=100)
results = model.most_similar(positive=sys.argv[2], negative=sys.argv[3], topn= 100)

for result in results:
    print(result[0], '\t', result[1])