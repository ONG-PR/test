#-*- coding: utf-8 -*-
##x = redis.keys("idx3"),y = redis.hmget(x, idx3)
#하려고 했던 방법은 단어 첫 글자를 key로 두고 값은 그 글자로 시작하는 단어들의 [list]

import random

def load_wordfile(filename):
    data = dict()
    with open(filename) as f:
        for word in f:
            i = word[:3] #단어의 첫 글자
            if i in data:
                data[i].append(word.strip())
            else:
                data[i] = [word.strip()]
    f.close()

    return data

def find_next_word_for(data):
    print("한글 끝말잇기를 시작해볼까요?")
    print("----------------------------------------------")

    prev_word = None

    while True:
        user_word = raw_input("단어입력: ")

        if user_word == "--":
            if prev_word == None:
                print("왜~ 놀다 가지..")
            else:
                print("유 루저 ㅋㅋ")
            return

        end = user_word[-3:]

        answer = None

        print("  prev_word=%s" % prev_word)

        if prev_word == None:
            answer = data[end][0] if end in data else None

            if answer == None:
                print("당신 이겼어요! 컴퓨터를 이기다니 대단한데요?!")
                return

            print(answer)
        else:
            print("  prev_word=<%s>, prev_word[-3:]=<%s>, user_word=<%s>, user_word[:3]=<%s>" % (prev_word, prev_word[-3:], user_word, user_word[:3]))

            if prev_word[-3:] == user_word[:3]:
                answer = data[end][0] if end in data else None

                if answer == None:
                    print("당신 이겼어요! 컴퓨터를 이기다니 대단한데요?!")
                    return

                print(answer)
            else:
                print("틀렸어 다시 말해주세요.")

        if answer != None:
            prev_word = answer

datafilename = "wordfile.txt"
data = load_wordfile(datafilename)
find_next_word_for(data)