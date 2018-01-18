# hangul separate

chosung=['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
			'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', ' ']

jungsung=['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ',
			'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ',
			'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', ' ']

jongsung=['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ',
			'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ',
			'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', ' ']


class han_assem:

	def __init__(self,letter_set):
		self.cho_index=letter_set[0]
		self.jung_index=letter_set[1]
		self.jong_index=letter_set[2]
		#print( chosung[self.cho_index],jungsung[self.jung_index],jongsung[self.jong_index] )
		
	def assemble_letter(self):
		if self.cho_index==19 and self.jong_index!=29: char_unicode=0x0020
		
		elif self.jong_index==29: char_unicode=0x000A
		
		else:
			char_num = self.cho_index*588 + self.jung_index*28 + self.jong_index
			char_unicode = char_num + 0xAC00
		
		character = chr( char_unicode )
		#print( character )
		return character



#################################################################################################

#c=han_assem([4,2,1])
#ch=c.assemble_letter()
#print(ch)

#c=han_assem([19, 21, 0])
#ch=c.assemble_letter()
#print('this is ch[',ch,']')
