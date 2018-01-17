# -*- coding: utf-8 -*-
'''
text = "who are you?"
sep_text = text.split(' ')
print(sep_text)

import shlex
'''

from __future__ import print_function
#==================================================================================#
def check_word_correct(word):    # 단어안에 초중성으로 완성된 한글 이외의 글자가 포함되어있는지 확인
    for k in unicode(word, 'utf8'):
        if not 0xAC00 <= ord(k) <= 0xD7A3:  # 초중종성 조립완성형 한글 유니코드 범위 AC00 - D7A3  (44032 - 55203)
            #print("공백없이 한글만으로 이루어진 올바른 단어를 입력해주세요")
            return 0
    return 1
#==================================================================================#
def sep_word():
    file = open('blog-2016-sampled10p_1.txt', 'rb')
    text = file.read()
    file.close()

    txt=''
    t=0
    for c in text:
        if t==1:
            txt+=c
        if c=='\t':
            t=1
        if c=='\n':
            t=0

    return txt
#==================================================================================#
def count_word(txt):
    txt_l=txt.split()
    txt_d={}

    for w in txt_l:
        if '/N' in w:
            noun=w.replace('/N', '')
            if noun in txt_d :
                txt_d.update({noun:(txt_d[noun]+1)})
            elif check_word_correct(noun) and len(noun) != 3 :
                txt_d.update({noun:1})
            else: pass
        else: pass

    rank = list(txt_d.items())
    rank.sort(key=lambda rank:rank[1],reverse=True)

    return rank
'''
    cn = 0
    cn2 = 0
    cn3 = 0
    cn4 = 0
    cn59 = 0

    for r in rank:
        if r[1]!=1 :
            print(r[0], end=' : ')
            print(r[1])
            cn+=1
        if r[1]>2 :
            cn2+=1
        if r[1]>3 :
            cn3+=1
        if r[1]>4 :
            cn4+=1
        if r[1]>59 :
            cn59+=1
    print(len(rank))
    print(float(cn)/len(rank), "2 이상")
    print(float(cn2) / len(rank), "3 이상")
    print(float(cn3) / len(rank), "4 이상")
    print(float(cn4) / len(rank), "5 이상")
    print(float(cn59) / len(rank), "59 이상")
'''
#==================================================================================#


t = sep_word()
rnk = count_word(t)

cn = 0
cn2 = 0
cn3 = 0
cn4 = 0
cn59 = 0

for r in rnk:
    if r[1] != 1:
        print(r[0], end=' : ')
        print(r[1])
        cn += 1
    if r[1] > 2:
        cn2 += 1
    if r[1] > 3:
        cn3 += 1
    if r[1] > 4:
        cn4 += 1
    if r[1] > 59:
        cn59 += 1
print(len(rnk))
print(float(cn) / len(rnk), "2 이상")
print(float(cn2) / len(rnk), "3 이상")
print(float(cn3) / len(rnk), "4 이상")
print(float(cn4) / len(rnk), "5 이상")
print(float(cn59) / len(rnk), "59 이상")


'''
import sys

f = open(sys.argv[1], 'r')
lines = f.readline()
for line in lines:
    item = line.split(" ")

print(item)


def sep_word(f):

    blog_word = []


    for word in f:
        word = blog_word.split(' ')
        blog_word.append(word)

    f.close()

    return blog_word


sep_word(file)


def getBook():

    file = open("./file.txt")
    [str(word) for word in file.read().split()]
    return

getBook()


import os.sys

def main(argv):
    dirpath = argv[0]
    files = os.listdir(dirpath)

    lineCount = 0
    wordCount = 0

    blog_word = ()

    splitdir = "%s/split" % (dirpath)
    if not os.path.exists(splitdir):
        os.makedirs(splitdir)

    for idx, file in enumerate(files):
        print("%d:%s" % (idx + 1, file))

        fullpath = "%s/%s" % (dirpath, file)

        if not os.path.isfile(fullpath):
            print("  It's a directory.")
            continue

        f = open(fullpath, "rb")

        lineCountFile = 0
        wordCountFile = 0
        title = None
        blogno = 0

        for line in f:
            line = line.strip()

            if line == "":
                continue

            if line.startswith("TITLE:"):
                title = line[len("TITLE:"):].strip()
            else:
                if title == None:
                    continue
                else:
                    # blog_20160101.txt
                    datestring = file.split(".")[0].split("_")[1]
                    fname = "%s/split/%s-%05d.txt" % (dirpath, datestring, blogno + 1)
                    f2 = open(fname, "wb")
                    f2.write("TITLE: %s\n" % title)
                    f2.write("%s\n" % line)
                    f2.close()

                    title = None
                    blogno += 1

            lineCountFile += 1
            words = line.split()
            for w in words:
                wordCountFile += 1
                uniq.add(w)

                if w in wcnt:
                    wcnt[w] += 1
                else:
                    wcnt[w] = 1

        f.close()
'''

#import shlex
#shlex.split()