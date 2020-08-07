#!/usr/bin/python
# coding=utf-8
# 采用Word2Vec获取文本词向量表示

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')  # 忽略警告
import sys, codecs
import pandas as pd
import numpy as np
import jieba
import jieba.posseg
import gensim
from gensim.models import word2vec
import chardet
import codecs

# 返回特征词向量
def getWordVecs(wordList, model):
    name = []
    vecs = []
    for word in wordList:
        if word in model:  # 模型中存在该词的向量表示
            print word
            name.append(word.encode("gbk"))
            vecs.append(model[word])
        else:
            print
    a = pd.DataFrame(name, columns=['word'])
    b = pd.DataFrame(np.array(vecs, dtype='float'))
    return pd.concat([a, b], axis=1)


 # 数据预处理操作：分词，去停用词，词性筛选
 def dataPrepos(text, stopkey):
     l = []
     pos = ['n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd']  # 定义选取的词性
     seg = jieba.posseg.cut(text)  # 分词
     for i in seg:
         if i.word not in l and i.word not in stopkey and i.flag in pos:  # 去重 + 去停用词 + 词性筛选
             # print i.word
             l.append(i.word)
     return l
 

# 根据数据获取候选关键词词向量
def buildAllWordsVecs(model):
    path = "Result\\keyextract_word2vec_DRW.csv"
    read_csv = codecs.open(path,"r", "gbk")
    lines = read_csv.readlines()
    words = []
    for line in lines:
        temp_list = line.strip().split(",")[0].encode("utf-8")
        temp_list = temp_list.decode("utf-8")
        words.append(temp_list)
        print len(words)
    wordvecs = getWordVecs(words, model)  # 获取候选关键词的词向量表示
    # 词向量写入csv文件，每个词400维
    data_vecs = pd.DataFrame(wordvecs)
    data_vecs.to_csv('Result\\Jiebafenci_key_all_DRW.csv', index=False)
    print "document ", " well done."
    

def main():
    model_file_name = "Result\\w2v_taifengDRW.model"  #词向量存储
    model = word2vec.Word2Vec.load(model_file_name) 
    buildAllWordsVecs(model)

if __name__ == '__main__':
    main()
    # -