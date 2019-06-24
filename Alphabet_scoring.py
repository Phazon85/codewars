'''
codewars.com practice problem:
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
'''

import string
def high(x):
    values = {}
    output = []
    spstring = x.split()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    return spstring
    for word in spstring:
        for letter in word:
            
            


test = 'man i need a taxi up to ubud'

print(high(test))

