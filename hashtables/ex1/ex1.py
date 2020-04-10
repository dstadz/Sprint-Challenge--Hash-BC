#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for w in range(len(weights)):
        hash_table_insert(ht, weights[w], w)

    #special cases
    if length == 1:
        return None
    elif length == 2:
        if weights[1] + weights[0] == limit:
            answer = (1,0)
        else:
            return

    #actual work
    else:
        #loop through wieghts arr
        for w in weights:
            a = hash_table_retrieve(ht, w)
            #search through hash for limit - weights[i]
            b = hash_table_retrieve(ht, limit - w)
            if b:
                answer = (max(a,b), min(a,b))
            else:
                continue
    print(answer)
    return answer

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
