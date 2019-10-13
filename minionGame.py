testString = input()

testString = testString.lower()

def get_all_substrings(string):
  length = len(string)
  alist = []
  for i in range(length):
    for j in range(i,length):
      alist.append(string[i:j + 1]) 
  return list(set(alist))

def consonants_or_vowel(list):
    vowel = []
    consonant = []
    for i in list:
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            vowel.append(i)
        else:
            consonant.append(i)
    return {"vowel":vowel, "consonant":consonant}

def all_ocurrences(testSubstring, testString):
    cuenta = 0
    for i in range(len(testString)):
        if testString.startswith(testSubstring, i):
            cuenta+=1
    return cuenta

def winner(dictionary, testString):
    kevinScore = 0
    stuartScore = 0
    for i in dictionary["vowel"]:
        kevinScore += all_ocurrences(i, testString)
    for i in dictionary["consonant"]:
        stuartScore += all_ocurrences(i, testString)
    if stuartScore > kevinScore:
        return ["Stuart ", stuartScore]
    elif kevinScore > stuartScore:
        return ["Kevin ", kevinScore]
    else:
        return ["Draw", ""]

all_substrings = get_all_substrings(testString)
dictionary = consonants_or_vowel(all_substrings)
result = winner(dictionary, testString)
print(str(result[0]) + str(result[1]))