import unittest
from memory_numbers import MemoryNumber

class TestMemoryNumber(unittest.TestCase):
    def test_initial_value(self):
        m = MemoryNumber(5)
        self.assertEqual(m.value, 5)

    def test_single_addition(self):
        m = MemoryNumber(5)
        m.apply(lambda x: x + 3, "add 3")
        self.assertEqual(m.value, 8)

    def test_multiple_steps(self):
        m = MemoryNumber(2)
        m.apply(lambda x: x * 4, "multiply by 4")
        m.apply(lambda x: x - 1, "subtract 1")
        self.assertEqual(m.value, 7)

    def test_reset(self):
        m = MemoryNumber(10)
        m.apply(lambda x: x + 1, "add 1")
        m.reset()
        self.assertEqual(m.value, 10)
        self.assertEqual(len(m.memory_chain), 0)

if __name__ == "__main__":
    unittest.main()

