class MinionGame:
    
    def __init__(self, testString):
        self.testString = testString.lower()

    def __get_all_substrings(self):
        length = len(self.testString)
        alist = []
        for i in range(length):
            for j in range(i,length):
                alist.append(self.testString[i:j + 1]) 
        return list(set(alist))
    
    def __consonants_or_vowel(self, list):
        vowel = []
        consonant = []
        for i in list:
            if i[0] in ['a', 'e', 'i', 'o', 'u']:
                vowel.append(i)
            else:
                consonant.append(i)
        return {"vowel":vowel, "consonant":consonant}

    def __all_ocurrences(self, testSubstring):
        cuenta = 0
        for i in range(len(self.testString)):
            if self.testString.startswith(testSubstring, i):
                cuenta+=1
        return cuenta

    def winner(self):

        all_substrings = self.__get_all_substrings()
        dictionary = self.__consonants_or_vowel(all_substrings)
        kevinScore = 0
        stuartScore = 0
        for i in dictionary["vowel"]:
            kevinScore += self.__all_ocurrences(i)
        for i in dictionary["consonant"]:
            stuartScore += self.__all_ocurrences(i)
        if stuartScore > kevinScore:
            print("Stuart " + str(stuartScore))
        elif kevinScore > stuartScore:
            print("Kevin " + str(kevinScore))            
        else:
            print("Draw")


game = MinionGame("BANANA")
game.winner()

