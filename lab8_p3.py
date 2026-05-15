from lab8_p1 import Table
from lab8_p2 import insert, TOMBSTONE

def rehash(table: Table, new_size: int) -> Table:
    """
    Creates a new table of larger size and reinserts all
    valid (non-None, non-TOMBSTONE) entries from the original table.
    """
    new_table = Table(new_size, [None] * new_size)

    for item in table.data:
        if item != None and item != TOMBSTONE:

            insert(new_table, item)
    
    return new_table

