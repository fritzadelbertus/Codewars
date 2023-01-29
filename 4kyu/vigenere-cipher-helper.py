# Codewars: Vigenère Cipher Helper
# Source: https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def shift(self, text, encode):
        answer = ''
        keyIndex = 0
        for letter in text:
            if letter not in self.alphabet:
                answer += letter
            else:
                posL = self.alphabet.index(letter)
                posV = self.alphabet.index(self.key[keyIndex])
                if encode: # For encoding
                    answerIndex = posL + posV if posL + posV < len(self.alphabet) else posL + posV - len(self.alphabet)
                else: # For decoding
                    answerIndex = posL - posV if posL >= posV else posL - posV + len(self.alphabet)
                answer += self.alphabet[answerIndex]
            if keyIndex + 1 == len(self.key):
                keyIndex = 0
            else:
                keyIndex += 1
        return answer

    def encode(self, text):
        return self.shift(text, encode = True)
    
    def decode(self, text):
        return self.shift(text, encode = False)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

c = VigenereCipher(key, alphabet)

print(c.encode("codewars")); #// returns 'rovwsoiv'
print(c.decode('laxxhsj'));  #// returns 'waffles'
