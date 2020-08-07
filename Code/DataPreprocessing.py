# -*- coding: utf-8 -*-
"""
本段程序主要是对输入到10word2vec_1程序中的数据进行预处理操作。主要的步骤就是合并原始的数据到一个文件夹中，同时进行分词处理
"""


import codecs
import jieba


def read_tingyongci():
    path = "Data\\stop_words.txt"   #停用词分析，加载停用词
    stop_words = []
    csv_reader = codecs.open(path,"r", "gbk")
    for row in csv_reader:
        row = row.strip( '\r\n' ).encode("utf-8")
        stop_words.append(row)
    return stop_words

 
    

def read_draw():#提取原始数据微博文本
    list_date = ['0822','0823','0824','0825','0826','0827','0828','0829','0830','0902','0903','0904','0905']
    path = os.path.abspath('..')
    csvfile = codecs.open("Data\\all_data_content.txt", 'wb', 'utf-8')
    for i in list_date:
        read_csv = open("\\Data\\"+ i + ".txt",'r')
        lines = read_csv.readlines()
        for line in lines:
            temp_list = line.strip().split("$")[4]
            csvfile.write(temp_list.decode("utf-8"))
            csvfile.write("\n")
        read_csv.close()
    csvfile.close()




def yichutingyongci_fenci():#对微博文本进行分词处理
    stop_words = read_tingyongci()
    path = "Data\\all_data_content.txt"#1_ALL_DATA
    csv_reader = open(path)

    filepath0 = "Data\\all_data_content_fenci.txt"
    txtfile = open(filepath0, 'wb')

    for row0 in csv_reader:
        wordList = row0.strip().split(" ")
        for i in wordList:
            if i in stop_words:
                pass
            else:
                txtfile.write(i)
                txtfile.write(" ")
        txtfile.write("\r\n")    
    txtfile.close()
    csv_reader.close()



def main():
    yichutingyongci_fenci()
if __name__ == '__main__':
    main()

 