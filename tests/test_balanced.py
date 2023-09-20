import unittest
from algos.is_balanced import is_balanced

class TestIsBalanced(unittest.TestCase):

    def test_balanced_expression(self):
        self.assertTrue(is_balanced("([]{})"))
    
    def test_unbalanced_expression(self):
        self.assertFalse(is_balanced("([)]"))

if __name__ == '__main__':
    unittest.main()