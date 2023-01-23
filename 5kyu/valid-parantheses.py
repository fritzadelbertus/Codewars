# Codewars: Valid Parantheses
# Source: https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

def valid_parentheses(string):
  count = 0
  for character in string:
    if character == '(':
      count += 1
    elif character == ')':
      count -= 1
    if count < 0:
      return False      
  return True if count == 0 else False
