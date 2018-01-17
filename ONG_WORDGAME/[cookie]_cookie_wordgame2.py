# coding=utf-8
def end():
    sys.exit()

print("Setup progream ...")
dicdata = [] #사전목록
usedata = [] #이미 사용된 단어 저장
import sys, os, time, random
time.sleep(1)
print("Setup progream  [ OK ]")

print("Loading system.txt ...")
try:
    f = open("krwords.txt","r")
except:
    print("ERROR! systemkr.txt file not found!")
    print("Loading systemkr.txt  [ FAULT ]")
    time.sleep(3)
    end() #오류를 발생시켜 프로그램 종료.

while True:
    data = f.readline().rstrip('\r\n')
    dicdata.append(data)
    if data == "":
        break

f.close()

print("Loading systemkr.txt  [ OK ]")
print("Start ...")
time.sleep(1)

print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-""")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class humanKr():
    @staticmethod
    def humanInput(lastChar):
        humanwords = raw_input("Human : %s" % lastChar)
        return humanwords

    @staticmethod
    def humanConnectChar(humanInputword,plusChar):
        humanwords = str(plusChar) + str(humanInputword)
        return humanwords

    @staticmethod
    def humanwordsDefine(hmword,dicdata):
        for dicword in dicdata:
           if dicword == hmword:
                return False
        return True

    @staticmethod
    def humanUseword(hmword,usedata):
        for useword in usedata:
            if hmword == useword:
                print("이미 사용한 단어입니다.")
                return True
        return False

class computerKr():
    @staticmethod
    def useword(lastChar,dicdata):
        #마지막 글자와 첫번째 글자가 같은 것들을 리스트로 묶기
        canUse = []
        for dicword in dicdata:
            try:
                firstChar = dicword[:3]
            except:
                pass
            if firstChar == lastChar:
                canUse.append(dicword)
            else:
                continue
        return canUse

    @staticmethod
    def useAgain(word,usedata):
        for use in usedata:
            try:
                word.remove(use)
            except:
                pass
        return word

    @staticmethod
    def selectword(canUse):
        wordLen = len(canUse)-1
        useword = canUse[random.randint(0, wordLen)]
        return useword

    @staticmethod
    def usedataJoin(word,usedata):
        usedata = usedata.append(word)
        return usedata

class defaultKr():
    @staticmethod
    def getLastChar(word):
        #맨 마지막 단어 구하기
        ret = word[-3:]
        return ret

    @staticmethod
    def getFisrtChar(word):
        return word[:3]

#스타트 엔진
lastChar = ""

#스타트 루프
while True:
    hmword = humanKr.humanInput(lastChar) #사람이 단어를 입력함
    if hmword == "--":
        print("Goodbye, You loose.")
        break
    hmword = humanKr.humanConnectChar(hmword,lastChar) #사람이 입력한 단어를 가공함
    hmCanUse = humanKr.humanwordsDefine(hmword,dicdata) #사람이 입력한 단어가 있는지 확인
    if hmCanUse:
        print("이 단어는 없는거 같습니다..")
        continue
    isuse = humanKr.humanUseword(hmword,usedata)
    if isuse:
        continue
    else:
        usedata.append(hmword)

    #사람이 입력할 것이 완료됨
    #컴퓨터의 시작
    lastChar = defaultKr.getLastChar(hmword)
    comword = computerKr.useword(lastChar,dicdata)
    if comword == []:
        print("끄악! 컴퓨터가 졌습니다.[1]")
        print("다시 시작하려면 프로그램을 다시 시작하십시오.")
        time.sleep(5)
        end()
    comword = computerKr.useAgain(comword,usedata)
    if comword == []:
        print("끄악! 컴퓨터가 졌습니다.[2]")
        print("다시 시작하려면 프로그램을 다시시작하십시오.")
        time.sleep(5)
        end()

    #comword  변수에 총 사용가능한 단어들이 모여있습니다.
    computerUse = computerKr.selectword(comword)
    sys.stdout.write("Computer : %s\n" % computerUse)
    usedata.append(computerUse)
    lastChar = defaultKr.getLastChar(computerUse)
    #엔진구동 완료. 다시 시작