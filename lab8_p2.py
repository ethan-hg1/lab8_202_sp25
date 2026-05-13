from lab8_p1 import Table
from typing import Optional, Tuple

TOMBSTONE = (100000, "")

def hash_fn(entry: Tuple[int, str], size: int) -> int:
    return entry[0] % size

def insert(table: Table, entry: Tuple[int, str]) -> Table:
    """
    Inserts a (key, value) entry using linear probing.
    Reuses tombstone slots if found.
    Overwrites if the key already exists.
    """
    index = hash_fn(entry, table.size)
    start = index

    if table.data[index] != None:
        index = (index + 1) % table.size

    while index != start:
      if table.data[index] == None:
        table.data[index] = entry
        break
      index = (index + 1) % table.size
  
    table.data[index] = entry

    return table

def delete(table: Table, key: int) -> Table:
    """
    Deletes the entry with the given key by marking the slot with TOMBSTONE.
    """
    index = key % table.size
    
    if table.data[index] != None:
        table.data[index] = TOMBSTONE
        
    return table
    

def get(table: Table, key: int) -> Optional[str]:
    """
    Retrieves the value associated with the given key using linear probing.
    Skips over tombstones.
    Returns None if not found.
    """
    index = key % table.size
    start = index

    while True:
        entry = table.data[index]

        if entry is None:
            return None

        if entry != TOMBSTONE and entry[0] == key:
            return entry[1]

        index = (index + 1) % table.size

        if index == start:
            return None