# Codewars: Duplicate Encoder
# Source: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
  word = word.lower()
  counter_map = {}
  for letter in word:
    letter = letter
    if letter in counter_map:
      counter_map[letter] += 1
    else:
      counter_map[letter] = 1
  encoded_list = ['(' if counter_map[i] == 1 else ')' for i in word]
  answer = ''
  for bracket in encoded_list:
    answer += bracket
  return answer
  