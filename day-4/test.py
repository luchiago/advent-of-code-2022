import unittest

from main import process

class TestMain(unittest.TestCase):
    pairs = [
        '2-4,6-8',
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8'
    ]

    def test_process(self):
        result = process(self.pairs)

        self.assertEqual(result, 2, "Should be 2")

    def test_process_overlap(self):
        result = process(self.pairs, overlap=True)

        self.assertEqual(result, 4, "Should be 4")

if __name__ == '__main__':
    unittest.main()
