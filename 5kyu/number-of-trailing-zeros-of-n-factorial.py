# Codewars: Number of Trailing Zeros for N!
# Source: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python
# Helpful Solution: https://mathworld.wolfram.com/Factorial.html

def zeros(n):
  kmax = 0
  n2 = n
  while n2 > 5:
    kmax += 1
    n2 /= 5
  result = 0
  for i in range(1,kmax+1):
    result += int(n/(5**i))
  return result

print(zeros(30)) # 7