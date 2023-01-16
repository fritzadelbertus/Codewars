# Codewars: Tribonacci Sequence
# Source: https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def tribonacci(signature, n):
  while len(signature) < n:
    index = len(signature)
    signature.append(signature[index-1] + signature[index-2] + signature[index-3])
  return signature[:n]

print(tribonacci([1,1,1], 0))
