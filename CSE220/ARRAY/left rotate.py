import numpy as np

def rotateleft(arr):
    temp=arr[0]
    for i in range(1,len(arr),1):
        arr[i-1]=arr[i]
    arr[-1]=temp
    return arr
arr=np.array([1,2,3,4,5])
print(rotateleft(arr))