import numpy as np
def mergeLineup(*args):

    New_arr = np.zeros(len(pokemon_1), dtype =int)
    for i in range(len(pokemon_1)):
        if pokemon_1[i] == None:
             pokemon_1[i] = 0
        if pokemon_2[len(pokemon_1)-1-i] == None:
             pokemon_2[len(pokemon_1)-1-i] = 0
        New_arr[i] = pokemon_1[i] + pokemon_2[len(pokemon_1)-1-i]
    return New_arr

pokemon_1 =  [12, 3, 25, 1, None]
pokemon_2 = [5, -9, 3, None, None]
print(mergeLineup(pokemon_1, pokemon_2))


