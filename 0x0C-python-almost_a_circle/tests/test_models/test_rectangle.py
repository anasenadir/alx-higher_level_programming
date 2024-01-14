#!/usr/bin/python3
"""Test module for the Rectangle Calss
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0

    def test_constractor_with_no_args(self):
        """test the Rectangle constractor with no args"""
        msg = "Rectangle.__init__() missing 3 required positional arguments: 'self', 'width', and 'height'"
        with self.assertRaises(TypeError) as e:
            Rectangle.__init__()
        self.assertEqual(str(e.exception), msg)

    def test_constractor_with_only_self_arg(self):
        """test the Rectangle constractor with no args"""
        msg = "Rectangle.__init__() missing 2 required positional arguments: 'width' and 'height'"
        with self.assertRaises(TypeError) as e:
            Rectangle()
        self.assertEqual(str(e.exception), msg)

    def test_constractor_with_one_arg(self):
        """test the Rectangle constractor with one args"""
        msg = "Rectangle.__init__() missing 1 required positional argument: 'height'"
        with self.assertRaises(TypeError) as e:
            Rectangle(1)
        self.assertEqual(str(e.exception), msg)
    
    def test_constractor_with_more_than_6_args(self):
        """test the Rectangle constractor with more than 6 args"""
        msg = "Rectangle.__init__() takes from 3 to 6 positional arguments but 7 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle(12,45,45,546,45,444)
        self.assertEqual(str(e.exception), msg)
    # ----------------- Tests for #2 ------------------------
