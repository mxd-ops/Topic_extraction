# coding=utf-8 

import pandas as pd
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
import numpy as np
import csv

#构造网络 construct network

data0 = pd.read_csv('Result\\Jiebafenci_key_all_DRW.csv')
keyss = data0.ix[:,0:1]
keyss =  keyss["word"].values.tolist()

keys = []
for i in keyss:
	i = i.decode("gbk")
	keys.append(i)

list11 = keys
model_file_name =  "Result\\w2v_taifengDRW.model" #10w2v_sougou_taifeng_fenci1    10w2v_taifeng_fenci1  10w2v_taifengDRW_fenci1

model = word2vec.Word2Vec.load(model_file_name)  # 3个文件放在一起：Word60.model   Word60.model.syn0.npy   Word60.model.syn1neg.npy
print("read model successful")


csvfile = open("Result\\graph_edge.csv",'wb')
csv_writer = csv.writer(csvfile,dialect='excel')
csv_writer.writerow(["Source","Target","Weight"])
		
idDict = {}
node_list = []

j = 0
for i in keys:
	idDict[i] = j
	j = j +1 


t = 0 
for i in list11: 
	# print i
	for j in list11:
		# print chardet.detect(i)
		# print i 
		# print j
		# break
		sim = model.similarity(i, j)
		if sim > 0.4:
			if list11.index(i) >= list11.index(j):
				pass
			else:
				# t = t + 1 
				# print t 
				# print i
				node_list.append(idDict[i])
				node_list.append(idDict[j])
				temp = []
				temp.append(idDict[i])
				temp.append(idDict[j])
				temp.append(sim)
				csv_writer.writerow(temp)
							
csvfile.close()

node_list = list(set(node_list))
csvfile = open("Result\\graph_node.csv",'wb')
csv_writer = csv.writer(csvfile,dialect='excel')
csv_writer.writerow(["Id","Label"])


for key, value in idDict.items():
	temp = []
	if value in node_list:
		temp.append(value)
		temp.append(key.encode("gbk"))
		csv_writer.writerow(temp)
csvfile.close()

