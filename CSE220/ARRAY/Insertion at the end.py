import numpy as np

def resizeArray(arr, length):
    New_arr = np.zeros(length, dtype=int)
    for i in range(len(arr)):
        New_arr[i] = arr[i]
    return New_arr

def insert_at_the_end(arr, size, elem):
    if size >= len(arr):
        arr = resizeArray(arr, len(arr)+5)
    arr[size] = elem
    return arr

arr = np.zeros(4, dtype=int)
arr[0], arr[1], arr[2] = 4, 6, 5
print(arr)
print(insert_at_the_end(arr, 3, 15)) 
print(insert_at_the_end(arr, 4, 25))
print(insert_at_the_end(arr, 5, 26))