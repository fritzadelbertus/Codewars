# Codewars: Printer Errors
# Source: https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
  error = len([i for i in s if i not in 'abcdefghijklm'])
  return f'{error}/{len(s)}'
