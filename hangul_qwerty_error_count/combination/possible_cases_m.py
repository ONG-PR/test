
###한글 오타 조합###
chosung=['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
			'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', ' ']

jungsung=['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ',
			'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ',
			'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', ' ']

jongsung=[' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ',
			'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ',
			'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', ' ','\n']
###########################################################################################################
cho_combi=[('ㄷ','ㅅ'), ('ㄸ','ㅆ'), ('ㅁ','ㅇ'), ('ㄱ','ㅈ'), ('ㅉ','ㄲ'), ('ㅇ','ㅎ'), ('ㄴ'), ('ㅈ'), ('ㅉ'),
			('ㄱ'), ('ㄲ'), ('ㄴ','ㄹ'), ('ㅂ','ㄷ'), ('ㅃ','ㄸ'), ('ㅌ','ㅍ'), ('ㅌ'), ('ㅊ','ㅋ'), ('ㅊ'), ('ㄹ'), (' ')]

jung_combi=[('ㅓ','ㅣ'), ('ㅑ','ㅔ'),('ㅕ','ㅐ'), ('ㅑ','ㅖ'), ('ㅗ','ㅏ'), ('ㅐ'), ('ㅛ','ㅑ'),
			('ㅒ'), ('ㅓ'), ('ㅚ'), ('ㅙ'), ('ㅘ'), ('ㅕ'), ('ㅠ','ㅡ'), ('ㅝ'), ('ㅞ'), ('ㅢ'),
			('ㅜ'), ('ㅜ'), ('ㅟ'), ('ㅏ'),(' ')]

jong_combi=[(' '),('ㄷ','ㅅ'),('ㄸ','ㅆ'),('ㄳ'),('ㅁ','ㅇ'),('ㄵ'),('ㄶ'),('ㅈ','ㄱ'),('ㅇ','ㅎ'),
			('ㄺ'),('ㄻ'),('ㄼ'),('ㄺ'),('ㄾ'),('ㄿ'),('ㅀ'),('ㄴ'),('ㅈ'),('ㅄ'),('ㄱ'),('ㄲ'),('ㄴ','ㄹ'),
			('ㅂ','ㄷ'),('ㅌ','ㅍ'),('ㅌ'),('ㅋ','ㅊ'),('ㅊ'),('ㄹ'), (' '),('\n')]

class pos_case:
	
	'''
	return possible cases of letters
	'''
	def possible_letter(self,type,num):
		if type=='cho': combi=cho_combi
		elif type=='jung': combi=jung_combi
		elif type=='jong': combi=jong_combi
		else:
			print('wrong type')
			return
		#print(combi[num])
		i=0
		list=[]
		for k in combi[num]:
			list.append(combi[num][i])
			i+=1
		#print (list)
		return list
	
	
	'''
	find the list of possible combination of chosung,jungsung,jongsung
	'''
	def assume(self,l,m,n):
		cho_list=l
		jung_list=m
		jong_list=n
		cases=[]
		
		for k in jong_list:
			for j in jung_list:
				for i in cho_list:
					temp=[]
					temp.append(i)
					temp.append(j)
					temp.append(k)
					cases.append(temp)
		#print("cases",cases)		
		return cases
	
	
	'''
	find the list index number of each cases
	'''
	def letter_index(self,type,list):
		index=[]
		if type=='cho': letter=chosung
		elif type=='jung': letter=jungsung
		elif type=='jong': letter=jongsung
		else:
			print('wrong type')
			return

		for c in list:
			i=0
			for s in letter:
				if c==s:
					index.append(i)
					break
				else:
					i+=1
		#print(index)
		return index



#################################################################################################

#b=pos_case()

#list2=b.possible_letter('cho',2)
#b.letter_index('cho',list2)

#b.assume(['ㄱ','ㄴ'],['ㅏ','ㅐ'],['ㅇ','ㄷ'])