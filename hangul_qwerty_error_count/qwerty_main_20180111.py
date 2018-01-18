#####################################
# 오타 교정을 위한 예상 교정단어 리스트
# 2018.01.11
#####################################

from separate.hangul_separate_m import separate_txt
from combination.possible_cases_m import pos_case
from assemble.hangul_assemble_m import han_assem
from count.ngram_m import *

f=open("C:/Users/USER/Documents/__CODES/말뭉치파일/utf8_FINAL.txt", 'r', encoding='utf-8')
#f=open("C:/Users/USER/Documents/__CODES/corpus_pre_process/utf8_p_short.txt", 'r', encoding='utf-8')
t01=f.read()
f.close()
f2=open("C:/Users/USER/Documents/__CODES/말뭉치파일/syl-1.txt", 'r')
t02=f2.read()
f2.close()

word=input("단어를 입력해주세요 : ")
print('\n')
wc=word.count(' ')+1
ng=Ngram(t01,n=wc)
ng.ngram()

word_l = word.split()

for w_i in range( len(word_l) ):    # 어절별로 LOOP 돌림
	print("===교정 어절 : %s / 맞다고 가정한 어절 : %s===" % (word_l[w_i], ''.join( word_l[:w_i]+word_l[w_i+1:])))
	# 초성 중성 종성 분리==========================
	word_sep = separate_txt(word_l[w_i])
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
	assume_list=[]    # 글자별로 가능한 글자들 리스트로 묶어 assume_list에 저장 assume_list[1]은 두번째 글자가 틀린 경우

	for i in range( len(word_l[w_i]) ):
		cho_p[i] = pc.letter_index('cho',cho_p[i])    # 초성, 중성, 종성을 각각의 index로 바꾸어 저장
		jung_p[i] = pc.letter_index('jung',jung_p[i])
		jong_p[i] = pc.letter_index('jong',jong_p[i])
		
		a=pc.assume( cho_p[i]+[word_sep.cho[i]], [word_sep.jung[i]], [word_sep.jong[i]] )    # 초성이 오타라고 가정한 경우
		b=pc.assume( [word_sep.cho[i]], jung_p[i]+[word_sep.jung[i]], [word_sep.jong[i]] )    # 중성이 오타라고 가정한 경우
		c=pc.assume( [word_sep.cho[i]], [word_sep.jung[i]], jong_p[i]+[word_sep.jong[i]] )    # 종성이 오타라고 가정한 경우
		
		assume_list.append( a+b+c )

		
	rank_w=[]    # 빈도 조회할 단어들 저장 (중복되지 않도록)
	chk_unvs_set=0    # 전체집합 빈도 확인 유무
	# 단어 출력=================================
	for i in range( len(word_l[w_i]) ):
		print("%d번째 글자 오타" %(i+1) )
		rank=[]    # 검색어와 그에 해당하는 빈도 수 저장
		cn1=0  # query_1 출현 빈도 초기화
		
		for j in assume_list[i]:
			ass=han_assem(j)
			replace_char=ass.assemble_letter()    # 초,중,종성 합쳐서 한글자로 저장
			if replace_char in t02:    # 음절빈도자료에서 조회, 없는 음절은 제외
				re_word = word_l[w_i][:i] + replace_char + word_l[w_i][i+1:]

				if re_word not in rank_w:    # 중복되지 않도록 rank_w에 없을 경우에만 진행
					rank_w.append( re_word )    # 중복되지 않으면 rank_w에 추가
					
					temp_l = word_l+[]
					temp_l[w_i]=re_word
					query_2 = ' '.join(temp_l)    # 교정어 + 나머지 어절
					del temp_l[w_i]
					query_1 = ' '.join(temp_l)    # 교정어 제외한 나머지

					cn2=0  # query_2 출현 빈도 초기화
					for k in ng.dik:
						if chk_unvs_set==0:
							if not query_1=='':	   # 2어절 이상 검색한 경우
								if ' '+query_1+' ' in k:
									if k.split().index(query_1)==word_l.index(query_1) :
										cn1+=ng.di[k]    # re_word_' '가 포함된 key에 해당하는 value(빈도)를 cn에 누적
								else: pass
							else: cn1=-1    # 1어절짜리 검색한 경우

						if k==' '+query_2+' ':
							cn2+=ng.di[k]

					if not cn1==-1:	   # 2어절 이상 검색한 경우
						if cn1!=0: rank.append( [query_2, cn2/cn1] )
						if cn1==0: rank.append( [query_2, 0] )    # 
					else: rank.append( [query_2, cn2] )    # 1어절짜리 검색한 경우
					
					print(rank[-1][0], end=' ')
					print(cn2)
					
					if i==0: chk_unvs_set=1    # query_1 빈도 확인 완료
					#print('──────────────┚')
				else: pass
			else: continue

		rank.sort(key=lambda rank:rank[1],reverse=True)
		print("가능성 있는 단어 : ", end='')

		for m in rank:
			if m[1]!=0: print( "%s %.2f" %(m[0], m[1]), end=' ' )

		print('\n'*2)
	