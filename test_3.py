import unittest
from lab8_p1 import Table
from lab8_p2 import insert, delete, get, TOMBSTONE
from lab8_p3 import rehash

def make_empty_table(size: int) -> Table:
    return Table(size, [None] * size)

class TestRehash(unittest.TestCase):

    def test_rehash_basic(self):
        t = make_empty_table(5)
        t = insert(t, (1, "a"))
        t = insert(t, (6, "b"))  # causes collision
        new_t = rehash(t, 10)

        self.assertEqual(new_t.size, 10)
        self.assertEqual(get(new_t, 1), "a")
        self.assertEqual(get(new_t, 6), "b")

    def test_rehash_skips_tombstones(self):
        t = make_empty_table(5)
        t = insert(t, (1, "x"))
        t = insert(t, (6, "y"))
        t = delete(t, 1)
        self.assertEqual(t.data[1], TOMBSTONE)

        new_t = rehash(t, 10)
        self.assertIsNone(get(new_t, 1))
        self.assertEqual(get(new_t, 6), "y")


if __name__ == "__main__":
    unittest.main()
