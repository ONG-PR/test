
class Ngram:
	def __init__(self,text="", n=1):
		# dictionaray 생성
		self.di = dict()
		self.text=text
		self.n=n
		
	def ngram(self):
		# check input str
		if len(self.text) < 1:
			return self.di

		# split text as list
		word_list = self.text.split()

		for i in range(len(word_list) - (self.n - 1)):
			temp_str = " "
			for j in range(self.n):
				temp_str += word_list[i + j]
				temp_str += " "

			num = 1
			if self.di.get(temp_str):
				num = self.di.get(temp_str) + 1
			
			self.di.update({temp_str: num})
			
		self.dik=list( self.di.keys() )
		#print(self.di)
		#print(self.dik)
		
	"""
	github.com/YoungHunCho/konlp-test
	"""