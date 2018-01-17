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