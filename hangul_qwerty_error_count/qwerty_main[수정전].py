#####################################
# 오타 교정을 위한 예상 교정단어 리스트
# 2017.10.27
#####################################

from separate.hangul_separate_m import separate_txt
from combination.possible_cases_m import pos_case
from assemble.hangul_assemble_m import han_assem
from count.ngram_m import *

f=open("utf8.txt", 'r', encoding='utf-8')
t01=f.read()
f.close()

word=input("단어를 입력해주세요 : ")
print('\n')
wc=word.count(' ')+2
ng=Ngram(t01,n=wc)
ng.ngram()


# 초성 중성 종성 분리==========================
word_sep = separate_txt(word)
word_sep.sep()


# 각 글자별 예상 교정어 목록=====================
pc = pos_case()

cho_p=[]   # 오타 교정 예상 초성
jung_p=[]  # 오타 교정 예상 중성
jong_p=[]  # 오타 교정 예상 종성

for i in word_sep.cho: cho_p.append( pc.possible_letter('cho',i) )
for j in word_sep.jung: jung_p.append( pc.possible_letter('jung',j) )
for k in word_sep.jong: jong_p.append( pc.possible_letter('jong',k) )


# 예상 교정어 조합 목록=========================
assume_list=[]

for i in range( len(word) ):
	cho_p[i] = pc.letter_index('cho',cho_p[i])
	jung_p[i] = pc.letter_index('jung',jung_p[i])
	jong_p[i] = pc.letter_index('jong',jong_p[i])
	
	a=pc.assume( cho_p[i]+[word_sep.cho[i]], [word_sep.jung[i]], [word_sep.jong[i]] )
	b=pc.assume( [word_sep.cho[i]], jung_p[i]+[word_sep.cho[i]], [word_sep.jong[i]] )
	c=pc.assume( [word_sep.cho[i]], [word_sep.jung[i]], jong_p[i]+[word_sep.jong[i]] )
	#print("a+b+c", a+b+c)
	assume_list.append( a+b+c )


# 단어 출력=================================
for i in range( len(word) ):
	print("%d번째 글자 오타" %(i+1) )
	
	rank_w=[]
	rank=[]
	
	for j in assume_list[i]:
		ass=han_assem(j)
		replace_char=ass.assemble_letter()
		if replace_char in t01:
			re_word = word[:i] + replace_char + word[i+1:]

			if re_word not in rank_w:             #re_word!=word and 
				rank_w.append( re_word )

				cn=0
				for k in ng.dik:
					if ' '+re_word+' ' in k and k.find(' '+re_word+' ')==0:
						cn+=ng.di[k]
						print(k,ng.di[k])
					else: pass

				rank.append( [cn, re_word] )
				print(re_word, cn)                #================================
				print('──────────────┚')          #================================
			else: pass
		else: continue

	rank.sort(reverse=True)
	print("가능성 있는 단어 : ", end='')
	for i in rank:
		if i[0]!=0: print( "(%s %s)" %(i[1], i[0]), end=' ' )

	print('\n'*2)
