from functools import reduce


class Class:

    def __init__(self):
        pass

    def get_vowels(self, word):
        word = word.lower()
        letters = ['a','e','i',
                   'o','u','y']
        result = filter(lambda x: x in letters, word)
        return list(result)

    def get_consonants(self, word):
        word = word.lower()
        letters = ['b','c','d',
                   'f','g','h',
                   'j','k','l',
                   'm','n','p',
                   'q','r','s',
                   't','v','w',
                   'x','y','z']
        result = filter(lambda x: x in letters, word)
        return list(result)

    def get_upper(self, letter):
        return letter.upper()

    
word = 'Hello'
A = Class()
res1 = A.get_vowels(word)
res2 = A.get_consonants(word)
print(f'{res1} - гласные в слове: {word}')
# print(list(map(lambda x: x.upper(), res1)))
print(reduce(lambda a, b: a + b, list(map(lambda x: x.upper(), res1))))
print(f'{res2} - согласные в слове: {word}')
# print(list(map(lambda x: x.upper(), res2)))
print(reduce(lambda a, b: a + b, list(map(lambda x: x.upper(), res2))))