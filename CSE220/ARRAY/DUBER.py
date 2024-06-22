import numpy as np

def findGroups( arr, fare):
    flag = 0
    secondary_count = 0
    ungroup_count = 0
    secondary_arr = np.zeros(len(arr), dtype=int)
    ungroup_arr = np.zeros(len(arr), dtype=int)
    state = False
    

    for i in range(len(arr)):
        base = arr[i]

        if base == None:
            continue

        elif base == fare:
            flag += 1
            secondary_arr[len(arr) - (len(arr) - secondary_count)] += base
            secondary_count += 1
            print( f"Group {flag} : {base}" )
            base = None
            continue
        else:
            for j in range(i+1, len(arr)):

                if arr[j] == None:
                    continue

                if base + arr[j] == fare:
                    if arr[j] == None:
                        continue
                    else:
                        flag+=1
                        
                        secondary_arr[len(arr) - (len(arr) - secondary_count)] += base
                        secondary_count += 1
                        secondary_arr[len(arr) - (len(arr) - secondary_count)] += arr[j]
                        secondary_count += 1
                        print( f"Group {flag} : {base}, {arr[j]}")

                        base = None
                        arr[j] = None
                        break
            if base != None:
                    ungroup_arr[len(arr) - (len(arr) - ungroup_count)] += base
                    state = True
                    ungroup_count += 1
    
    if state == True:
        print("Unrouped : ", end ="")
        for k in ungroup_arr:
            if k != 0:
                print (str(k), end =" ")
    print()

print("///  Task 03: DUBER Fare Splitting  ///")
findGroups ( [60, 150, 60, 180, 30, 120, 30, 7], 180 )
print()
findGroups( [120, 100, 150, 50, 30], 150 )
print()
findGroups ( [30, 150, 150], 180 )
print()
findGroups ( [30, 150, 180, -2, 182, 150, 103], 180 )
print()