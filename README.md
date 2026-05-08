````markdown
# Lab 8: Hash Tables

## Overview

In this lab, you will implement a hash table with integer keys and string values. The lab is split into three parts:

1. Basic hash table with linear probing
2. Tombstone-based deletion
3. Rehashing into a larger table

The goal is to understand collision handling, deletion in open-addressed hash tables, and resizing.

---

## Schedule

| Day | Date | Focus |
|---|---|---|
| Day 1 | May 11 | Part 1: Basic linear probing |
| Day 2 | May 13 | Part 2: Tombstones |
| Day 3 | May 15 | Part 3: Rehashing and final submission |

You must get signed off each lab day.

Final submission is due **May 15**.

---

## Files

Complete:
````
```text
lab8_p1.py
lab8_p2.py
lab8_p3.py
````

Provided tests:

```text
test_lab8_p1.py
test_lab8_p2.py
test_lab8_p3.py
```

---

## Part 1: Basic Linear Probing

Complete the functions in `lab8_p1.py`.

The table is represented as:

```python
@dataclass
class Table:
    size: int
    data: List[Optional[Tuple[int, str]]]
```

Each slot stores either:

```python
None
```

or:

```python
(key, value)
```

Implement:

| Function               | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| `hash_fn(entry, size)` | Return `key % size`                                  |
| `insert(table, entry)` | Insert using linear probing; overwrite existing keys |
| `delete(table, key)`   | Delete by setting the slot to `None`                 |
| `get(table, key)`      | Return the value for `key`, or `None` if not found   |

If `insert` cannot find an available slot, raise `RuntimeError`.

---

## Part 2: Tombstones

Complete the functions in `lab8_p2.py`.

In Part 1, deleting by setting a slot to `None` can break future searches. Part 2 fixes this using a tombstone marker:

```python
TOMBSTONE = (100000, "")
```

Implement the same four operations as Part 1, with these changes:

| Function | Required behavior                        |
| -------- | ---------------------------------------- |
| `insert` | Reuse tombstone slots when possible      |
| `delete` | Replace deleted entries with `TOMBSTONE` |
| `get`    | Skip tombstones while probing            |

---

## Part 3: Rehashing

Complete `rehash` in `lab8_p3.py`.

```python
def rehash(table: Table, new_size: int) -> Table:
```

The function should:

1. Create a new empty table of size `new_size`
2. Reinsert every valid entry from the old table
3. Skip `None` and `TOMBSTONE`
4. Return the new table

Use the Part 2 `insert` function when reinserting entries.


---

## Sign-Off Requirements

Each lab day requires sign-off.

| Day    | Sign-off checkpoint             |
| ------ | ------------------------------- |
| May 11 | Part 1 works                    |
| May 13 | Part 2 works                    |
| May 15 | Part 3 works and all tests pass |

---

## Submission

Submit your sign off sheet on the last day
```
