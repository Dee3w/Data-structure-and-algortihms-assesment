import unittest
from algos.word_frequency import word_frequency

class TestWordFrequency(unittest.TestCase):

    def test_word_frequency(self):
        sentence = "This is a test sentence. This sentence is a test."
        result = word_frequency(sentence)
        expected = {
            "this": 2,
            "is": 2,
            "a": 2,
            "test": 2,
            "sentence": 2,
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()