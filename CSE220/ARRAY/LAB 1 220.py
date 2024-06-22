import numpy as np
def mean(arr):
    mean=0
    for i in arr:
        mean+=i

    return (round(mean/len(arr),10))
arr=np.array([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4])
print(mean(arr))

def standard_daviation(arr):

    mean=0
    for i in arr:
        mean+=i

    standard_daviation=0
    for i in arr:
        standard_daviation+=(i- mean/len(arr))**2
    
    return (round((standard_daviation/(len(arr)-1))**(0.5),2))
arr=np.array([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4])
print(standard_daviation(arr))


def SD_away(arr):
    mean = 0
    for i in arr:
        mean += i

    standard_deviation = 0
    for i in arr:
        standard_deviation += (i - mean / len(arr)) ** 2

    mean = round(mean / len(arr), 10)
    standard_deviation = round((standard_deviation / (len(arr) - 1)) ** (0.5), 2)
    bounce = 0
    limit1 = mean + standard_deviation * 1.5
    limit2 = mean - standard_deviation * 1.5
    count = 0

    for i in arr:
        if i >= limit1 or i <= limit2:
            count += 1
    New_arr = np.zeros(count, dtype=int)
    index = 0

    for i in arr:
        if i <= limit2 or i >= limit1:
            New_arr[index] = i
            index += 1

    output = '['
    for i in range(len(New_arr)):
        output += str(New_arr[i])
        if i < len(New_arr) - 1:
            output += ', '
    output += ']'
    return output

arr = np.array([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4])
print(SD_away(arr))