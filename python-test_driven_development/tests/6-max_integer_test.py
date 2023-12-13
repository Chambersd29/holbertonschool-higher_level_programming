#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_two_item(self):
        self.assertEqual(max_integer([4, 2]), 4)

    def test_three_item(self):
        self.assertEqual(max_integer([4, 2, 8]), 8)

    def test_one_item(self):
        self.assertEqual(max_integer([9]), 9)

    def test_num_negative(self):
        self.assertEqual(max_integer([-9, 9]), 9)

    def test_two_num_middle(self):
        self.assertEqual(max_integer([-9, 9, 9, 8]), 9)

    def test_other__negative(self):
        self.assertEqual(max_integer([-9]), -9)

    def test_list_empty(self):
        self.assertIsNone(max_integer([]), None)
