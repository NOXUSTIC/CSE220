import numpy as np
def rightshift(arr):
    for i in range(len(arr)-1, 0, -1):
        arr[i]=arr[i-1]
    arr[0]=0
    return arr
arr=np.array([1,2,3,4,5])
print(rightshift(arr))
