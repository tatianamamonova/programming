import re
import os

def count_sentence(file):
    sentences = 0
    f = open (file,'r')
    lines = f.readlines()
    for line in lines:
        if re.search('<se>',line):
            sentences = sentences + 1
    return sentences

def write_count_sentence():
    cw = open ('count_sentence.txt','w',encoding='utf-8')
    for root, dirs, files in os.walk('news'):
        for f in files:
            cw.write(f+'\t'+str(count_sentence(os.path.join(root, f)))+'\n')

write_count_sentence()

def get_meta(filepath):
    f = open(filepath,'r')
    lines = f.readlines()
    for line in lines:
        if line[:5]=="<meta" and re.search('author',line):
            meta=re.search('content="(.*?)"',line).group(1)
    meta+=","
    for line in lines:
        if line[:5]=="<meta" and re.search('topic',line):
            meta+=re.search('content="(.*?)"',line).group(1)
    return meta
        

def get_data():
    d=open ('data.csv','w',encoding='utf-8')
    d.write("Название файла,Автор,Тематика текста\n")
    for root, dirs, files in os.walk('news'):
        for f in files:
            d.write(f+','+get_meta(str(os.path.join(root, f)))+'\n')

get_data()



