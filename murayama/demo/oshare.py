# -*- coding: utf-8 -*-
#python oishii.py hogehoge.mpdel [search word]
#おしゃれ系と相関があるかをみてくれます

from gensim.models import word2vec
import sys

model   = word2vec.Word2Vec.load(sys.argv[1])
results = model.most_similar(positive=sys.argv[2], topn=1000)

#results = model.most_similar(positive=['美味しい'] , topn= 1000)
#oshare = [result for result in results if result[0]=="おしゃれ"]
#print(oshare)

for result in results:
	if result[0] == "おしゃれ":
		print(result[0], '\t', result[1])
	if result[0] == "オシャレ":
		print(result[0], '\t', result[1])
	if result[0] == "お洒落":
		print(result[0], '\t', result[1])
	else:
		pass