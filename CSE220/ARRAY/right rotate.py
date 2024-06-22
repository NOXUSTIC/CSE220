import numpy as np

def rotateleft(arr):
    temp=arr[-1]
    for i in range(len(arr)-1 , 0 ,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    return arr
arr=np.array([1,2,3,4,5])
print(rotateleft(arr))