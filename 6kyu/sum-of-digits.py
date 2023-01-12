# Codewars: Sum of Digits / Digital Root
# Source: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
  if n < 10:
    return n
  result = 0
  for number in str(n):
    result += int(number)
  return digital_root(result)

# Tests
print(digital_root(16)) # 7
print(digital_root(942)) # 6
print(digital_root(132189)) # 6
print(digital_root(493193)) # 2
