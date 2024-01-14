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
    
    def test_base_instantiation(self):
        """tests the base instantiation"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {'id': 1})
        self.assertEqual(b.id, 1)
    
    def test_constractor_with_no_args(self):
        """test the base constractor with no args"""
        msg = "Base.__init__() missing 1 required positional argument: 'self'"
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        
        self.assertEqual(str(e.exception), msg)
    
    def test_constractor_with_more_that_2_args(self):
        """test the base constractor with more than 2 args"""
        msg = "Base.__init__() takes from 1 to 2 positional arguments but 3 were given"
        with self.assertRaises(TypeError) as e:
            Base(12, 452)
        
        self.assertEqual(str(e.exception), msg)
    
    # ----------------- Tests for #1 ------------------------
    def test_id_inctrementation(self):
        """check if the id is incremented after any instansiation"""
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 5)
    
    def test_if_id_equal_to_nb_objects(self):
        """test if the id is work as expected and its value
        is equal to nb_objects private class attr"""
        b = Base()
        self.assertEqual(getattr(b, "_Base__nb_objects"), b.id)

        

if __name__ == "__main__":
    unittest.main()
