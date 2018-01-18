# hangul separate

chosung=['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', ' ']
jungsung=['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', ' ']
jongsung=['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', ' ','\n']


class separate_txt:
	
	def __init__(self,text):
		self.text=text
		
	def sep(self):
		self.cho=[]
		self.jung=[]
		self.jong=[]
		for onechar in self.text:
			c=ord(onechar)
			if c==0x0020:
				self.cho.append(19)
				self.jung.append(21)
				self.jong.append(28)
			elif c==0x000A:
				self.cho.append(19)
				self.jung.append(21)
				self.jong.append(29)
			else:
				self.cho.append( int( ((c-0xAC00)/(28*21)) %19 ) )
				self.jung.append( int( ((c-0xAC00)/28) %21 ) )
				self.jong.append( int( (c-0xAC00)%28 ) )
			
	def print_txt(self):
		print('='*25,"초성 나열",'='*26)
		for j in self.cho:	print(chosung[j], end=" ")
		print('\n',end='')
		print('='*60,'\n\n')
		i=0
		for k in self.text:
			#print("==%s번째 글자==" %i, end="\n")      #테스트용
			print(chosung[self.cho[i]], end=" ")
			print(jungsung[self.jung[i]], end=" ")
			print(jongsung[self.jong[i]], end="/")
			i=i+1
		print('\n',end='')
		print('='*60,'\n\n')

'''
c=separate_txt('가나다라마바사 분리')
c.sep()
c.print_txt()
'''




