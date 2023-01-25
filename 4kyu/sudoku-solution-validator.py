def valid_solution(board):
  # Validity Check
  def check(result:list):
    result.sort()
    return result != [1,2,3,4,5,6,7,8,9]

  # Evaluate Columns
  for i in range(9):
    result = []
    for j in range(9):
      result.append(board[j][i])
    if check(result): return False

  # Evaluate Rows
  for i in range(9):
    result = []
    for j in range(9):
      result.append(board[i][j])
    if check(result): return False
  
  # Evaluate 3x3
  for i in range(3):
    for j in range(3):
      result = []
      for innerrow in range(i*3, i*3+3):
        for innercolumn in range(j*3, j*3+3):
          result.append(board[innerrow][innercolumn])
      if check(result): return False
  
  return True


print(valid_solution(
  [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]]
))
