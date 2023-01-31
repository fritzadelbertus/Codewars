# Codewars: Validate Sudoku with size 'NxN'
# Source: https://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python

class Sudoku(object):
  def __init__(self, data):
    self.board = data

  def is_valid(self):
    valid = list(range(1,len(self.board)+1))
    
    # Evaluate Rows
    for row in self.board:
      for e in row:
        if type(e) != int:
          return False
      if sorted(row) != valid:
        return False
    
    # Evaluate Columns
    for column in zip(*self.board):
      if sorted(column) != valid:
        return False
    
    # Evaluate Regions
    reg = int(len(self.board) ** (1/2))
    for i in range(reg):
      for j in range(reg):
        region = []
        for line in self.board[i*reg:(i+1)*reg]:
          region += line[j*reg:(j+1)*reg]
        if sorted(region) != valid:
          return False
    
    return True

goodSudoku1 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])

print(goodSudoku1.is_valid())
print(set([True]))
