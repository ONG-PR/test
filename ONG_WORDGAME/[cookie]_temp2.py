# -*- coding: utf-8 -*-
'''
text = "who are you?"
sep_text = text.split(' ')
print(sep_text)

import shlex
'''

def sep_word(file):
    file = open('blog-2016-sampled10p_1.txt', 'rb')
    text = file.read()
    words = text.split(" ")
    my_list = []  # make empty list
    for current_word in words:
        dot_splitted = current_word.split(".")
        print(current_word)


        for w in dot_splitted:
            my_list.append(w)

    file.close()

sep_word("")



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