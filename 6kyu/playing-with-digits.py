# Codewars: Playing with Digits
# Source: https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
  sumOfPow = 0
  numberStr = str(n)
  for i in range(len(numberStr)):
    sumOfPow += int(numberStr[i])**(i+p)
  return int(sumOfPow/n) if sumOfPow % n == 0 else -1

# Tests
print(dig_pow(89,1)) # 1
print(dig_pow(92,1)) # -1
print(dig_pow(46288,3)) # 51
print(dig_pow(41,5)) # 25
print(dig_pow(114,3)) # 9
print(dig_pow(8,3)) # 64
