# Codewars: Shortest Knight Path
# Source: https://www.codewars.com/kata/549ee8b47111a81214000941/train/python

def knight(p1:str,p2:str):
  alphabetToNumericNotation = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
  }
  x1,y1 = alphabetToNumericNotation[p1[0]], int(p1[1])
  x2,y2 = alphabetToNumericNotation[p2[0]], int(p2[1])
  
  moves = 0
  visited = [(x1,y1)]
  possibleMoves = {0: [(x1,y1)]}
  xMove = [1,1,2,2,-1,-1,-2,-2]
  yMove = [2,-2,1,-1,2,-2,1,-1]
  newMovesLength = len(xMove)
  while (x2,y2) not in visited:
    moves += 1
    newMoves =[]
    for positionIndex in range(len(possibleMoves[moves-1])):
      position = possibleMoves[moves-1][positionIndex]
      for newMoveIndex in range(newMovesLength):
        newMove = (position[0] + xMove[newMoveIndex], position[1] + yMove[newMoveIndex])
        validNewMove = newMove[0] >= 1 and newMove[1] >= 1 and newMove[0] <= 8 and newMove[1] <= 8
        if newMove not in visited and validNewMove:
          visited.append(newMove)
          newMoves.append(newMove)
      if (x2,y2) in visited:
        break
    possibleMoves[moves] = newMoves
  return moves

print(knight('a1', 'f1'))
  