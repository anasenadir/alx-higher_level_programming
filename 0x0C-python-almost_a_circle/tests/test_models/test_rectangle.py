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
        """test the base constractor with no args"""
        msg = "Rectangle.__init__() missing 3 required positional arguments: 'self', 'width', and 'height'"
        with self.assertRaises(TypeError) as e:
            Rectangle.__init__()
        self.assertEqual(str(e.exception), msg)

    # ----------------- Tests for #2 ------------------------
