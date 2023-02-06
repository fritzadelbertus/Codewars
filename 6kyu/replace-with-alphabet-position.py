# Codewars: Replace With Alphabet Position
# Source: https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  return ' '.join([str((alphabet.index(letter.lower())+1)) for letter in text if letter.lower() in alphabet])

print(alphabet_position("The sunset sets at twelve o' clock."))
