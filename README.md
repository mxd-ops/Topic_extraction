README
===========================


The is the code for paper "Disaster Damage Assessment Based on Fine-Grained Topics in Social Media ".


# Experimental environment
OS: Windows 7
Memory: 16G
IDE: Spyder 


# Dependencies

The code is written Python language and IDE is Spyder. When running code in Spyder,  the following dependent libraries are required:

Python 2.7 
sklearn
pandas
numpy
jieba
codecs
gensim

# Notes:
1. The code is written based on Python27. Python27 is available at: https://www.python.org/downloads/release/2.7/;
2. The data (i.e., tweet location, time, text) for the  fine-grained topic extraction are avaliable through Data. Following the Sina Developer Agreement Policy, we publish only part of location field. If you want to get full field of geolocation information, please contact us.
3. The main code include:
    1) DataPreprocessing.py, where you can preprocess the collected data, including remove stopwords, feature words extraction, etc.
    2) Word2Vec_Representation.py, where the texts were encoded into word vectors through word2vec model.
    3) NetworkConstruction, where the semantic similarity between words were calculated and then convert them into graph format.