import unittest

from main import process, organize_supplies, queue_pkgs, make_movements, get_message, make_movements_2

class TestMain(unittest.TestCase):
    supplies = [
        '    [D]\n',
        '[N] [C]\n',
        '[Z] [M] [P]\n',
        ' 1   2   3\n',
        '\n',
        'move 1 from 2 to 1\n',
        'move 3 from 1 to 3\n',
        'move 2 from 2 to 1\n',
        'move 1 from 1 to 2\n'
    ]

    def test_process(self):
        result = process(self.supplies)

        self.assertEqual(result, 'CMZ', "Should be CMZ")

    def test_organize_supplies(self):
        test1 = self.supplies[0]
        expected1 = [(4, 'D')]

        self.assertEqual(organize_supplies(test1), expected1)

        test2 = self.supplies[1]
        expected2 = [(0, 'N'), (4, 'C')]

        self.assertEqual(organize_supplies(test2), expected2)

        test3= self.supplies[2]
        expected3 = [(0, 'Z'), (4, 'M'), (8, 'P')]

        self.assertEqual(organize_supplies(test3), expected3)

    def test_queue_pkgs(self):
        test = [
            [(4, 'D')],
            [(0, 'N'), (4, 'C')],
            [(0, 'Z'), (4, 'M'), (8, 'P')],
            [(0, '1'), (4, '2'), (8, '3')],
        ]
        expected = {0: ['Z', 'N'], 1: ['M', 'C', 'D'], 2: ['P']}

        self.assertDictEqual(queue_pkgs(test), expected)

    def test_make_movements(self):
        test_supplies = {0: ['Z', 'N'], 1: ['M', 'C', 'D'], 2: ['P']}
        test_movements = [
            ['move', '1', 'from', '2', 'to', '1'],
            ['move', '3', 'from', '1', 'to', '3'],
            ['move', '2', 'from', '2', 'to', '1'],
            ['move', '1', 'from', '1', 'to', '2'],
        ]
        expected = {0: ['C'], 1: ['M'], 2: ['P', 'D', 'N', 'Z']}

        self.assertDictEqual(make_movements(test_supplies, test_movements), expected)

    def test_get_message(self):
        test = {0: ['C'], 1: ['M'], 2: ['P', 'D', 'N', 'Z']}
        expected = 'CMZ'

        self.assertEqual(get_message(test), expected)

    def test_make_movements_2(self):
        test_supplies = {0: ['Z', 'N'], 1: ['M', 'C', 'D'], 2: ['P']}
        test_movements = [
            ['move', '1', 'from', '2', 'to', '1'],
            ['move', '3', 'from', '1', 'to', '3'],
            ['move', '2', 'from', '2', 'to', '1'],
            ['move', '1', 'from', '1', 'to', '2'],
        ]
        expected = {0: ['M'], 1: ['C'], 2: ['P', 'Z', 'N', 'D']}

        self.assertDictEqual(make_movements_2(test_supplies, test_movements), expected)

if __name__ == '__main__':
    unittest.main()
