# Practice problem from Codewars.com
# take a string and return the numerical position of each letter in the alphabet


import string
def alphabet_position(text):
    alphabet = string.ascii_lowercase
    text = text.lower()
    result = []
    for i in text:
        if i in alphabet:
            result.append(str(alphabet.find(i) + 1))
    return ' '.join(result)
    


test = "The sunset sets at twelve o' clock."
print(alphabet_position(test))
