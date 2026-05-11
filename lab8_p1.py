from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class Table:
    """
    A basic hash table.
    - size: Number of slots.
    - data: A list of (key, value) tuples or None.
    """
    size: int
    data: List[Optional[Tuple[int, str]]]

def hash_fn(entry: Tuple[int, str], size: int) -> int:
    return entry[0] % size 
    

def insert(table: Table, entry: Tuple[int, str]) -> Table:
    """
    Inserts a (key, value) entry using linear probing.
    Overwrites if key already exists.
    Raises RuntimeError if the table is full.
    """
    index = hash_fn(entry, table.size)
    if table.data[index] is None:
        table.data[index] = entry
        return table

    if table[index] > table.size:
        raise RuntimeError("Hash Table Full")
        
    

def delete(table: Table, key: int) -> Table:
    """
    Deletes an entry with the given key by setting the slot to None.
    """
    index = key % table.size
    if table.data[index] != None:
        table.data[index] = None
        
    return table
    

def get(table: Table, key: int) -> Optional[str]:
   
    """
    Retrieves the value associated with the given key using linear probing.
    Returns None if the key is not found.
    """
    
    index = key % table.size
    if table.data[index] != None:
        return table.data[index][1]
    
    return None
    
