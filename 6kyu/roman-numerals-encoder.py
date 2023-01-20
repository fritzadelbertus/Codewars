# Codewars: Roman Numerals Encoder
# Source: https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python

def solution(n):
  roman = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
  }
  answer = ''
  for letter in roman:
    while n >= roman[letter]:
      answer += letter
      n -= roman[letter]
  return answer
