# -*- coding: utf-8 -*-
#python oshare.py hogehoge.mpdel [search word]
#おいしい系と相関があるかをみてくれます

from gensim.models import word2vec
import sys

model   = word2vec.Word2Vec.load(sys.argv[1])
results = model.most_similar(positive=sys.argv[2], topn=100)
#results = model.most_similar(positive=['おしゃれ','オシャレ'] , topn= 1000)

for result in results:
	if result[0] == "美味しい":
		print(result[0], '\t', result[1])
	if result[0] == "おいしい":
		print(result[0], '\t', result[1])
	else:
		pass