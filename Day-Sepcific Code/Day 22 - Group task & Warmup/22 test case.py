import unittest
from .Group Task import graduation_check


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        purple = [5, 8, 1, 3, 4]
        black = [6, 9, 2, 4, 5]
        expected = True
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        purple = [6]
        black = [6]
        expected = False
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        purple = [125]
        black = [126]
        expected = True
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        purple = [2, 3, 4, 5, 6]
        black = [1, 2, 3, 4, 5]
        expected = True
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        purple = [5, 6, 7, 2, 3, 1, 2, 3]
        black = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = False
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        purple = [21, 5, 4, 4, 4, 4, 4, 4, 4]
        black = [19, 2, 4, 6, 2, 3, 1, 1, 4]
        expected = False
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        purple = [21, 5, 4, 4, 4, 4, 4, 4, 4]
        black = [19, 2, 3, 6, 2, 3, 1, 1, 3]
        expected = False
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_8(self):
        purple = [5, 4]
        black = [4, 5]
        expected = False
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        purple = [5, 4]
        black = [5, 6]
        expected = True
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)

    def test_case_10(self):
        purple = [2, 3, 4, 5, 6]
        black = [1, 2, 3, 4, 5]
        expected = True
        actual = is_possible_photo(purple, black)
        self.assertEqual(actual, expected)