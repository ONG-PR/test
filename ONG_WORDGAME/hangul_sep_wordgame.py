#-*- coding: utf-8 -*-
# hangul separate

def define_end(word):
    '''
    chosung = ['ㄱ', 'ㄲ', 2'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 11'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    jungsung = [0'ㅏ', 1'ㅐ', 2'ㅑ', 3'ㅒ', 4'ㅓ', 5'ㅔ', 6'ㅕ', 7'ㅖ', 8'ㅗ', 9'ㅘ', 10'ㅙ', 11'ㅚ', 12'ㅛ', 13'ㅜ', 14'ㅝ', 15'ㅞ', 16'ㅟ', 17'ㅠ', 19'ㅡ', 20'ㅢ', 21'ㅣ']
    jongsung = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ',
                'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    '''

    end = word[-3:]
    onechar = unicode(end, 'utf8')[-1]
    print(onechar) ###################################
    c = ord(onechar)

    cho =  int(((c - 0xAC00) / (28 * 21)) % 19)
    jung = int(((c - 0xAC00) / 28) % 21)
    jong = int((c - 0xAC00) % 28)

    if cho == 2 and (jung == 6 or jung == 12 or jung == 17 or jung == 20): cho = 11 #녀,뇨,뉴,니 -> 여,요,유,이
    elif cho == 5 and (jung == 2 or jung == 6 or jung == 7 or jung == 12 or jung == 17 or jung == 20): cho = 11 #랴,려,례,료,류,리 -> 야,여,예,요,유,이
    elif cho == 5 and (jung == 0 or jung == 1 or jung == 8 or jung == 11 or jung == 13 or jung == 18): cho = 2 #라,래,로,뢰,루,르 -> 나,내,노,뇌,누,느
    else: pass


    char_num = cho * 588 + jung * 28 + jong
    char_unicode = char_num + 0xAC00

    end_uni = unichr(char_unicode)
    print('unicode', end_uni)
    end = end_uni.encode('utf8')
    print('utf8', end)

    if word[-3:] != end: print("  end=<%s>" % end)

    return end


word='녀뇨뉴니-랴려례료류리-라래로뢰루르' #녀뇨뉴니-랴려례료류리-라래로뢰루르
print (define_end(word))