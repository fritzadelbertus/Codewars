# Codewars: Convert number to reversed array of digits
# Source: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

def digitize(n):
  return [int(str(n)[i]) for i in range(len(str(n))-1,-1,-1)]
