import unittest

from break_string import *

class TestBreakString(unittest.TestCase):
    def test_break_string(self):
        self.assertCountEqual(break_string('program', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']).split(', '), ['pro', 'gram', 'program'])
        self.assertCountEqual(break_string('programit', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']).split(', '), ['pro', 'gram', 'program', 'it'])
        self.assertCountEqual(break_string('programmerit', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']).split(', '), ['pro', 'gram', 'merit', 'program', 'programmer', 'it'])
        self.assertCountEqual(break_string('programlala', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']).split(', '), ['pro', 'gram', 'program'])
        self.assertCountEqual(break_string('proletarian', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']).split(', '), ['pro'])
