import unittest
from lab8_p2 import insert, delete, get, hash_fn, TOMBSTONE
from lab8_p1 import Table

def make_empty_table(size: int) -> Table:
    return Table(size=size, data=[None] * size)

class TestHashTableWithTombstones(unittest.TestCase):

    def test_hash_fn(self):
        self.assertEqual(hash_fn((15, "apple"), 5), 0)

    def test_insert_linear_probe(self):
        t = make_empty_table(5)
        t = insert(t, (0, "a"))     # hash to 0
        t = insert(t, (5, "b"))     # hash to 0, probe to 1
        self.assertEqual(get(t, 0), "a")
        self.assertEqual(get(t, 5), "b")

    def test_delete_marks_tombstone(self):
        t = make_empty_table(5)
        t = insert(t, (1, "x"))
        t = delete(t, 1)
        self.assertEqual(t.data[1], TOMBSTONE)
        self.assertIsNone(get(t, 1))

    def test_insert_fills_tombstone(self):
        t = make_empty_table(5)
        t = insert(t, (1, "x"))
        t = delete(t, 1)
        t = insert(t, (6, "y"))  # reuses tombstone at index 1 (6 % 5 = 1)
        self.assertEqual(get(t, 6), "y")

    def test_get_skips_tombstone(self):
        t = make_empty_table(5)
        t = insert(t, (1, "x"))
        t = insert(t, (6, "y"))  # 6 collides with 1, goes to next
        t = delete(t, 1)
        self.assertEqual(get(t, 6), "y")
        self.assertIsNone(get(t, 1))


if __name__ == '__main__':
    unittest.main()
