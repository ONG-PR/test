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