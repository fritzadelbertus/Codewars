# Codewars: Find the unique number
# Source: https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
  for i in range(1,len(arr)-1):
    if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
      return arr[i]
  return arr[len(arr)-1] if arr[0] == arr[1] else arr[0]
