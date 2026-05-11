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
    index = hash_fn(table)
    if table[index] == None:
        table[index] = entry

    if table[index] > table.size:
        raise RuntimeError
        
    return table
    

def delete(table: Table, key: int) -> Table:
    index = hash_fn(table)
    if table[index] != None:
        table[index] = None
        
    return Table
    

def get(table: Table, key: int) -> Optional[str]:
    """
    Retrieves the value associated with the given key using linear probing.
    Returns None if the key is not found.
    """
    
    index = hash_fn(key, table)
    if table[index] != None:
        return table[index]
    return None
    
