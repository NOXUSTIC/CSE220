import numpy as np

def analyzeHobbies(*args):
    count,index,Unique_count =0, 0, 0
    for i in args:
        for j in i:
            count +=1
    all_hobbies_arr = np.zeros(count, dtype=object)
    for i in args:
        for j in i:
            if j not in all_hobbies_arr:
                all_hobbies_arr[index] = j
                index += 1
    for i in all_hobbies_arr:
        if i != 0:
            Unique_count+=1
            
    Unique_arr = np.zeros(Unique_count, dtype=object)
    index=0
    for i in all_hobbies_arr:
            if i != 0:
                Unique_arr[index] = i
                index += 1
    print(f'Unique Activities in the Town:\n{Unique_arr}')
    for i in Unique_arr:
        element_count = 0
        for j in args:
            if i in j:
                element_count += 1
            elif i == None:
                break
        print(f'{element_count} participant(s) like(s) {i}.')



            
participant_1 = ["Hiking", "Reading", "Photography", "Cooking"]
participant_2 = ["Reading", "Hiking", "Painting"]
participant_3 = ["Hiking", "Cooking", "Photography"]
print(analyzeHobbies(participant_1, participant_2, participant_3))

participant_1 = ["Gardening", "Traveling"]
participant_2 = ["Singing", "Gardening", "Painting"]
print(analyzeHobbies(participant_1, participant_2))


