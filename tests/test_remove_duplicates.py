import unittest
from algos.remove_duplicates import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
        result = remove_duplicates(input_sequence)
        self.assertEqual(result, [2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()