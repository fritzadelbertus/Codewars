# Codewars: Pick Peaks
# Source: https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

def pick_peaks(arr):
  front = 1
  back = 1
  pos = []
  peaks = []

  while front < len(arr)-1:
    if arr[front-1] < arr[front] and arr[front] > arr[front+1]:
      pos.append(front)
      peaks.append(arr[front])
    elif arr[front] == arr[front+1]:
      back = front
      while front < len(arr)-1 and arr[front] == arr[front+1]:
        front += 1
      if front < len(arr)-1 and arr[front+1] < arr[back] and arr[back-1] < arr[back]:
        pos.append(back)
        peaks.append(arr[back])
    front += 1
  return { 'pos': pos, 'peaks': peaks}

pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])