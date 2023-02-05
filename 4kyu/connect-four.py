# Codewars: Connect Four
# Source: https://www.codewars.com/kata/56882731514ec3ec3d000009/train/python

def who_is_winner(pieces_position_list):
  board = [[0,0,0,0,0,0] for j in range(7)]
  currentPlayer = 'Yellow' if pieces_position_list[0].endswith('w') else 'Red'
  columnsEncoding = {v: k for k, v in dict(enumerate(['A','B','C','D','E','F','G'])).items()}
  
  def insertColor(player, column):
    insertIndex = 0
    while insertIndex < len(board[column]) and board[column][insertIndex] != 0:
      insertIndex += 1
    board[column][insertIndex] = 'Yellow' if player == 'Yellow' else 'Red'
    return (insertIndex, column)
  
  def checkWinner(player, position):
    row, column = position
    columnCheck = board[column]
    rowCheck = [col[row] for col in board ]
    diagonal1Check = []
    diagonal2Check = []

    diag1row = row-column if row > column else 0
    diag1col = column-row if column > row else 0
    diag2row = row+column-6 if row > 6-column else 0
    diag2col = row+column if 6-column > row else 6
    while diag1row < 6 and diag1col < 7:
      diagonal1Check.append(board[diag1col][diag1row])
      diag1row += 1
      diag1col += 1
    while diag2col >=0 and diag2row < 6:
      diagonal2Check.append(board[diag2col][diag2row])
      diag2row += 1
      diag2col -= 1

    def winning(check):
      for i in range(len(check)-3):
        if check[i] == player and check[i+1] == player and check[i+2] == player and check[i+3] == player:
          return True
      return False
      
    return winning(columnCheck) or winning(rowCheck) or winning(diagonal1Check) or winning(diagonal2Check)

  for i in pieces_position_list:
    position = insertColor(currentPlayer, columnsEncoding[i[0]])
    if checkWinner(currentPlayer, position):
      return currentPlayer
    currentPlayer = 'Yellow' if currentPlayer == 'Red' else 'Red'

  return 'Draw'

print(who_is_winner(['C_Yellow', 'E_Red', 'G_Yellow', 'B_Red', 'D_Yellow', 'B_Red', 'B_Yellow', 'G_Red', 
                     'C_Yellow', 'C_Red', 'D_Yellow', 'F_Red', 'E_Yellow', 'A_Red', 'A_Yellow', 'G_Red', 
                     'A_Yellow', 'F_Red', 'F_Yellow', 'D_Red', 'B_Yellow', 'E_Red', 'D_Yellow', 'A_Red', 
                     'G_Yellow', 'D_Red', 'D_Yellow', 'C_Red']))