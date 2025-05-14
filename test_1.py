import unittest
from lab8_p1 import Table, insert, get, delete, hash_fn

def make_empty_table(size: int) -> Table:
    return Table(size, [None] * size)

class TestHashTable(unittest.TestCase):

    def test_hash_fn(self):
        # Basic hash function correctness
        self.assertEqual(hash_fn((12, "apple"), 5), 2)
        self.assertEqual(hash_fn((7, "banana"), 5), 2)

    def test_insert_and_get(self):
        # Basic insertion and retrieval without collisions
        t = make_empty_table(5)
        t = insert(t, (12, "apple"))
        self.assertEqual(get(t, 12), "apple")

    def test_multiple_inserts(self):
        # Insert two items that hash to different spots (we assume no collisions)
        t = make_empty_table(5)
        t = insert(t, (0, "alpha"))  # 0 % 5 == 0
        t = insert(t, (1, "beta"))   # 1 % 5 == 1
        self.assertEqual(get(t, 0), "alpha")
        self.assertEqual(get(t, 1), "beta")


    def test_delete(self):
        # Basic delete behavior
        t = make_empty_table(5)
        t = insert(t, (12, "apple"))
        t = delete(t, 12)
        self.assertIsNone(get(t, 12))

if __name__ == '__main__':
    unittest.main()
