#!/usr/bin/python3
"""Test module for the Base Calss
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test The Base Calss"""

    def setUp(self):
        """instantiates the class"""
        Base.__nb_objects = 0

    def test_if_base_class_has_private_attr(self):
        """test if the base class has a private class attribute"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
    
    def test_if_private_attr_initialized_to_zero(self):
        """tests if the nb_objects initialized to zero"""
        self.assertEqual(Base.__nb_objects, 0)
    
    


if __name__ == "__main__":
    unittest.main()
