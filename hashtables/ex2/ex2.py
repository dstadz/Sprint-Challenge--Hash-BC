#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length
    n = 0
    cur = 'earth'
    for t in tickets:
        if t.source == 'NONE':
            cur = t.destination
        hash_table_insert(ht, t.source, t.destination)

    while cur != "NONE":
        print(cur, end='')
        route[n] = cur
        cur = hash_table_retrieve(ht, cur)
        n += 1
        if n > length:
    return route
