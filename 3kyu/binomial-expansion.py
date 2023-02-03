# Codewars: Binomial Expansion
# Source: https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python
# Helpful Resource: https://www.youtube.com/watch?v=cvhyJT9c0ac&t=722s

import re
import math

def findBinom(data):
  a, b , variable, power, k = data
  binomialConstant = math.comb(power,k)
  aConstant = a**(power-k)
  bConstant = b**(k)
  varConstant = binomialConstant * aConstant * bConstant
  varPower = power-k
  if varPower == 0:
    return f'{"+" if varConstant > 0 else ""}{varConstant}'
  else:
    variableCoefficient = "" if varConstant == 1 else "-" if varConstant == -1 else varConstant
    variablePower = "" if varPower == 1 else "^"+str(varPower)
    return f'{"+" if varConstant > 0 else ""}{variableCoefficient}{variable}{variablePower}'

def expand(expr):
  pattern = r'\((-?\d*)([a-z])([+-]\d+)\)\^(\d+)'
  a, variable, b, power = re.search(pattern, expr).groups()
  a = 1 if a == '' else -1 if a == '-' else int(a)
  b = int(b)
  power = int(power)
  result = ''.join([findBinom([a,b,variable,power,k]) for k in range(power+1)])
  
  return result[1:] if result.startswith('+') else result


print(expand('(x+1)^1'))
