# Codewars: The Millionth Fibonacci Kata
# Source: https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python

def multiply(matrixA, matrixB):
  newMatrix = [[0,0],[0,0]]
  newMatrix[0][0] += matrixA[0][0] * matrixB[0][0] + matrixA[0][1] * matrixB[1][0]
  newMatrix[0][1] += matrixA[0][0] * matrixB[0][1] + matrixA[0][1] * matrixB[1][1]
  newMatrix[1][0] += matrixA[1][0] * matrixB[0][0] + matrixA[1][1] * matrixB[1][0]
  newMatrix[1][1] += matrixA[1][0] * matrixB[0][1] + matrixA[1][1] * matrixB[1][1]
  return newMatrix

def fib(n):
  if n == 0:
    return 0
  negative = n < 0
  even = n%2 == 0 
  n = abs(n)
  fiboMatrix = [[1,1],[1,0]]
  tempo = [[1,0],[0,1]]
  while n > 1:
    if n%2 == 0:
      fiboMatrix = multiply(fiboMatrix, fiboMatrix)
      n = n/2
    else:
      tempo = multiply(tempo, fiboMatrix)
      n = n-1
  answer = multiply(fiboMatrix, tempo)[0][1]
  return answer * -1 if negative and even else answer