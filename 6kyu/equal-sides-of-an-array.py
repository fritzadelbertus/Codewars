# Codewars: Equal Sides of an Array
# Source: https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):
  for i in range(len(arr)-1):
    if sum(arr[:i]) == sum(arr[i+1:]):
      return i
  return -1 if sum(arr[:len(arr)-1]) != 0 else len(arr)-1
