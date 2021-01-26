import unittest

from palindrome import *

class TestLargestPalindrome(unittest.TestCase):
    def test_largest_palindrome(self):
        self.assertAlmostEqual(largest_palindrome(1), 9)
        self.assertAlmostEqual(largest_palindrome(2), 9009)
        self.assertAlmostEqual(largest_palindrome(3), 906609)
        self.assertAlmostEqual(largest_palindrome(4), 99000099)