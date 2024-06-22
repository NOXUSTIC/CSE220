import numpy as np
def Cyclic_rotation(arr):
    for i in range(0, len(arr),1):
        arr[i]=arr[len(arr)-i-1]
    return arr
arr=np.array([1,2,3,4,5])
print (Cyclic_rotation(arr))