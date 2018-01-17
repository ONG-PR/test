#-*- coding: utf-8 -*-
##x = redis.keys("idx3"),y = redis.hmget(x, idx3)
#하려고 했던 방법은 단어 첫 글자를 key로 두고 값은 그 글자로 시작하는 단어들의 [list]

from random import *

#=============================================================================================================#

def load_wordfile (filename):
    data = dict()    # 빈 딕셔내리 생성 [ key = 단어 첫글자 / value = key를 첫글자로 갖는 단어들의 list ]
    with open (filename,"r") as f:
        for word in f:
            i = word[:3]    # 단어의 첫 글자
            if i in data:
                data[i].append(word.strip())
            else:
                data[i] = [word.strip()]
    f.close()

    return data

#=============================================================================================================#

def check_word_correct(word):    # 단어안에 초중성으로 완성된 한글 이외의 글자가 포함되어있는지 확인
    for k in unicode(word, 'utf8'):
        if not 0xAC00 <= ord(k) <= 0xD7A3:  # 초중종성 조립완성형 한글 유니코드 범위 AC00 - D7A3  (44032 - 55203)
            print("공백없이 한글만으로 이루어진 올바른 단어를 입력해주세요")
            return 0
    return 1

#=============================================================================================================#

# 여기서 사용자가 입력한 단어가 게임 규칙에 부합하는지 확인
# 1. 자료에있는지 확인
# 2. 끝말 이어지는지 확인 (첫 시작단어는 끝말 일치 확인 안함)
# 3. 중복되는지 확인

def check_user_word(user_word, prev_word):    # 자료에서 끝말잇기 조건에 부합하는 단어 검색
    for i in data:
        for j in data[i]:
            if user_word == j:    # 자료에 있을 때
                if prev_word == [''] or (prev_word[-1][-3:] == user_word[:3]):    # 끝말 이어질 때
                    if user_word in prev_word:    # 중복확인
                        print("이미 입력한 단어입니다. 다시 말해주세요.")
                        return False  # 중복 될 경우
                    return True    # 중복 안될 경우
                print("-끝말 이어지지 않았다")  ########################## 검토용
                return False  # 끝말 이어지지 않을 때
    print("-자료에 없다")  ############################################ 검토용
    return False  # 자료에 없을 때


#=============================================================================================================#

# 여기서 컴퓨터가 말하는 정답을 이전에 나온 단어와 겹치지 않도록 랜덤으로 고르는 기능 수행
# 끝말이 이어져도 이미 나온 단어들과 겹친다면 answer = None 으로 저장

def search_ans(end, prev_word):    # 자료에서 끝말잇기 조건에 부합하는 단어 검색
    if end in data:
        N=[]
        for word in data[end]:
            if word not in prev_word: N.append(word)
        if not N:
            print("-전부 다 겹친다") ################################## 검토용
            return None    # 자료 중에 이미 나온 단어와 겹치지 않는 단어가 없을 경우
        return choice(N)
    else:
        print("-자료에 없다") ######################################## 검토용
        return None    # 자료 중에 단어가 없을 경우

#=============================================================================================================#

def find_next_word_for(data):
    # =========== 초기값 선언 =========== #
    prev_word = ['']    # 사용된 단어들을 list로 저장
    end = ''    # 단어의 마지막 글자
    answer = None  # 이어질 단어
    # ==================================== #
    print("한글 끝말잇기를 시작해볼까요?")
    print("게임을 끝내려면 --를 입력하세요.")
    print("----------------------------------------------")

    while True:
        user_word = raw_input("단어입력: ")
        if user_word == "--":    ### -- 입력시 게임 중단
            if prev_word == ['']: print("왜~ 놀다 가지..")    # 게임을 하지않고 포기했을 때
            else: print("유 루저 ㅋㅋ")    # 게임 도중 포기했을 때
            return

        if not check_word_correct(user_word): continue    ### 초중종성으로 완성된 한글 이외의 글자가 포함된 경우 다시 입력받음

        end = user_word[-3:] # 입력받은 단어의 마지막 글자 저장

        print("  prev_word=<%s>, user_word=<%s>" % (prev_word[-1], user_word))

        if check_user_word(user_word, prev_word):    # 끝말잇기 조건에 부합하지 확인

            prev_word.append(user_word)    # 입력받은 단어가 끝말잇기 조건에 부합 & 중복되지 않으면 list에 저장

            answer = search_ans(end, prev_word)    # 자료에서 끝말잇기 조건에 부합하는 단어 검색

            if answer == None:    # 자료에서 끝말잇기 조건에 부합하는 단어가 없을 경우 게임 중단
                print("당신 이겼어요! 컴퓨터를 이기다니 대단한데요?!")
                return

            prev_word.append(answer)    # 자료에 끝말잇기 조건에 부함 & 중복되지 않는 단어가 있을 경우 list에 저장
            print("컴퓨터: %s" %answer)    # 자료에서 찾은 끝말잇기 조건에 부함하는 단어 출력

        else: print("틀렸어 다시 말해주세요.")    # 끝말잇기 조건에 부합하지 않은 경우


#=============================================================================================================#
# main 함수 시작 #

datafilename = "wordfile.txt"    # 참조할 단어목록
data = load_wordfile (datafilename)    # 검색용 딕셔내리 생성
find_next_word_for (data)    # 게임시작

#=============================================================================================================#