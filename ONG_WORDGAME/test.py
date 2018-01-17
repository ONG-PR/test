#-*- coding: utf-8 -*-

'''
#word=raw_input("input the word:")
word='가각나낙 다라마바'
print(word)
print(type(word))
print('\n')

k=0
for i in range( len(word) ):
    print("*", word[i], "*")

    if word[i]!=' ': k+=1
    else : print("-공백-")

    if k==3:
        print(word[i-2:i+1])
        k=0

print('\n',word[:])
'''
"""
wl={'abc':0,'def':1}

print('abc' in wl)

wl.update({'aaaa':23, 'bb':10})
print(wl)
B='bb'

if B in wl: wl.update({B:(wl[B]+1)})
print(wl)

#print( wl.viewitems() )

for i in wl.viewitems():
    print(i)

a=2342
b=253463
e = float(a)/b
ee = float(a)/float(b)
print(e)
print(ee)
"""

def count_word(): #count_word 함수를 정의
    text = open('blog-2016-sampled10p_1.txt', 'rb')
    word = text.read()

    word_frequency = 0
    cnt=0
    for w in word: #어떤 단어가 텍스트안에 있는지 for 문을 통해 감시
        print(w)
        if w in word: #어떤 단어가 텍스트 안에 있다면?
            word_frequency += 1  #word_frequency 는 1씩 증가
            print("frequency increase")
        else:
            word_frequency = 0  # 0 이다
        if cnt==10 : break
        cnt+=1

    print("단어별 빈도수는: %d" % word_frequency) #"단어의 빈도수는" word_frequency 를 출력


    text.close()

count_word()