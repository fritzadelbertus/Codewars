# Codewars: Matrix Determinant
# Source: https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python

def determinant(matrix):
# Note: The product of the diagonal elements in a triangular matrix is its determinant
  det = 1
    
# Convert matrix to a triangular matrix
  for i in range(len(matrix)-1):
    for j in range(i+1, len(matrix)):
      if matrix[i][i] == 0:
        l = i+1
        while l < len(matrix) and matrix[l][i] == 0:
          l += 1
        if l == len(matrix):
          return 0
      # Flip rows *flipping rows negate the determinant*
        temp = matrix[l]
        matrix[l] = matrix[i]
        matrix[i] = temp
        det *= -1
    # Row reduction
      ratio = - matrix[j][i] / matrix[i][i] 
      for k in range(len(matrix)):
        matrix[j][k] = matrix[j][k] + matrix[i][k] * ratio

  # Calculate the diagonal product
  for i in range(len(matrix)):
    det *= matrix[i][i]
  return round(det)

print(determinant([
  [2, 4, 5, 3, 1, 2], 
  [2, 4, 7, 5, 3, 2], 
  [1, 1, 0, 2, 3, 1], 
  [1, 3, 9, 0, 3, 2], 
  [1, 1, 2, 2, 4, 1], 
  [0, 0, 4, 1, 2, 3]
]))
