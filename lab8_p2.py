from lab8_p1 import Table
from typing import Optional, Tuple

TOMBSTONE = (100000, "")

def hash_fn(entry: Tuple[int, str], size: int) -> int:
    """
    Hashes the key of an entry using modulo.
    """
    pass

def insert(table: Table, entry: Tuple[int, str]) -> Table:
    """
    Inserts a (key, value) entry using linear probing.
    Reuses tombstone slots if found.
    Overwrites if the key already exists.
    """
    pass

def delete(table: Table, key: int) -> Table:
    """
    Deletes the entry with the given key by marking the slot with TOMBSTONE.
    """
    pass

def get(table: Table, key: int) -> Optional[str]:
    """
    Retrieves the value associated with the given key using linear probing.
    Skips over tombstones.
    Returns None if not found.
    """
    pass