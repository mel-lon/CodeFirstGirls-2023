import unittest
from .Individual_task import palindrome_substring


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(palindrome_substring("abaxyzzyxf"), "xyzzyx")

    def test_case_2(self):
        self.assertEqual(palindrome_substring("a"), "a")

    def test_case_3(self):
        self.assertEqual(palindrome_substring("it is noon"), "noon")

    def test_case_4(self):
        self.assertEqual(palindrome_substring("abccbait's noon"), "abccba")

    def test_case_5(self):
        self.assertEqual(
            palindrome_substring("abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"),
            "zzzzzzzzzzzzzzzzzzzz"
        )