import unittest

from main import process, process2

class TestMain(unittest.TestCase):
    test_cases = [
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)
    ]

    test_cases_2 = [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)
    ]

    def test_process(self):
        for case in self.test_cases:
            result = process(case[0])

            self.assertEqual(result, case[1], f'Should be {case[1]}')

    def test_process_2(self):
        for case in self.test_cases_2:
            result = process2(case[0])

            self.assertEqual(result, case[1], f'Should be {case[1]}')

if __name__ == '__main__':
    unittest.main()
