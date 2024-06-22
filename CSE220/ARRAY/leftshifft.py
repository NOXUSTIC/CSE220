import numpy as np
def leftshift(arr):
    for i in range(1, len(arr), 1):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=0
    return arr
arr=np.array([1,2,3,4,5])
print(leftshift(arr))
