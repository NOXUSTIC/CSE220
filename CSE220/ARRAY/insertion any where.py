import numpy as np

def resize_array(arr, new_length):
    new_arr = np.zeros(new_length, dtype=int)
    for i in range(len(arr)):
        new_arr[i] = arr[i]
    return new_arr

def insert_anywhere(arr, index, elem):
    if index < 0:
        return "Insertion not possible"
    
    if index >= len(arr):
        arr = resize_array(arr, len(arr) + 3)
    
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    
    arr[index] = elem
    return arr

arr = np.zeros(4, dtype=int)
arr[0], arr[1], arr[2] = 4, 6, 5
print(arr)
print(insert_anywhere(arr, 1, 15))
print(insert_anywhere(arr, 4, 25))
print(insert_anywhere(arr, 5, 26))