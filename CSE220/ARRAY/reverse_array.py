import numpy as np

def reverse_array(arr):
  x = len(arr) // 2
  for i in range(x):
    temp = arr[i]
    arr[i] = arr[len(arr) - i - 1]
    arr[len(arr) - i - 1] = temp
  return arr
arr=np.array([1,2,3,4,5])
print(reverse_array(arr))