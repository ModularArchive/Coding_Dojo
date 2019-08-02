wordslist = ['hello','world','my','name','is','Anna']

letters = set('o')

for words in wordslist:
    if letters & set(words):
        print words