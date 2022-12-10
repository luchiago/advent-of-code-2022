import unittest

from main import process, build_forest, check_edge, process_2

class TestMain(unittest.TestCase):
    test = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ]

    def test_process(self):
        result = process(self.test)

        self.assertEqual(result, 21, 'Should be 21')

    def test_build_forest(self):
        expected = [
            [(3, True), (0, True), (3, True), (7, True), (3, True)],
            [(2, True), (5, False), (5, False), (1, False), (2, True)],
            [(6, True), (5, False), (3, False), (3, False), (2, True)],
            [(3, True), (3, False), (5, False), (4, False), (9, True)],
            [(3, True), (5, True), (3, True), (9, True), (0, True)],
        ]

        result = build_forest(self.test)

        self.assertEqual(result, expected)

    def test_build_forest_only_forest(self):
        expected = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]

        result = build_forest(self.test, True)

        self.assertEqual(result, expected)

    def test_check_edge(self):
        forest_size = 5
        size_column = 5

        # Top Edge
        self.assertTrue(check_edge(0, 0, forest_size, size_column))
        # Left Edge
        self.assertTrue(check_edge(1, 0, forest_size, size_column))
        # Right Edge
        self.assertTrue(check_edge(1, 4, forest_size, size_column))
        # Bottom Edge
        self.assertTrue(check_edge(4, 0, forest_size, size_column))
        # Not Edge
        self.assertFalse(check_edge(2, 2, forest_size, size_column))

    def test_process_2(self):
        result = process_2(self.test)

        self.assertEqual(result, 8, 'Should be 8')

if __name__ == '__main__':
    unittest.main()
