# Codewars: Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
  return len([letter for letter in sentence if letter in 'aiueo'])
