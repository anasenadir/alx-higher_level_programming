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

    def test_class_type(self):
        """test the class type"""
        self.assertEqual(str(Rectangle), 
                         "<class 'models.rectangle.Rectangle'>")

    def test_inheritance(self):
        """check the parent of this class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id_inctrementation(self):
        """check if the id is incremented after any instansiation"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_instantiation(self):
        """test the reactangle instantiation"""
        r = Rectangle(12, 30)
        d = {'id': 1, '_Rectangle__width': 12, '_Rectangle__height': 30,
             '_Rectangle__x': 0, '_Rectangle__y': 0}
        
        self.assertDictEqual(r.__dict__, d)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))

        msg = "width must be an integer."
        with self.assertRaises(TypeError) as e:
            Rectangle("12", 20)
        self.assertEqual(str(e.exception), msg)

        msg = "height must be an integer."
        with self.assertRaises(TypeError) as e:
            Rectangle(12, "20")
        self.assertEqual(str(e.exception), msg)
    
        msg = "x must be an integer."
        with self.assertRaises(TypeError) as e:
            Rectangle(12, 78, "20")
        self.assertEqual(str(e.exception), msg)
    
        msg = "y must be an integer."
        with self.assertRaises(TypeError) as e:
            Rectangle(12, 78, 24, "20")
        self.assertEqual(str(e.exception), msg)
        
        msg = "width must be > 0"
        with self.assertRaises(ValueError) as e:
            Rectangle(-12, 78)
        self.assertEqual(str(e.exception), msg)

        msg = "height must be > 0"
        with self.assertRaises(ValueError) as e:
            Rectangle(12, -78)
        self.assertEqual(str(e.exception), msg)

        msg = "x must be >= 0"
        with self.assertRaises(ValueError) as e:
            Rectangle(12, 78, -1)
        self.assertEqual(str(e.exception), msg)

        msg = "y must be >= 0"
        with self.assertRaises(ValueError) as e:
            Rectangle(12, 78, 2, -1)
        self.assertEqual(str(e.exception), msg)

    def test_instantiation_2(self):
        """tests the instantiation"""
        d = {'id': 1, '_Rectangle__width': 5,
             '_Rectangle__height': 12, '_Rectangle__x': 45, '_Rectangle__y': 44}
        r = Rectangle(5, 12, 45, 44)
        self.assertEqual(r.__dict__, d)

        d = {'id': 20, '_Rectangle__width': 5,
             '_Rectangle__height': 12, '_Rectangle__x': 45, '_Rectangle__y': 44}
        r = Rectangle(5, 12, 45, 44, 20)
        self.assertEqual(r.__dict__, d)
    
    def test_getters_setter(self):
        """tests the getters and setter"""
        r = Rectangle(1, 45)
        r.width = 20
        r.height = 98
        r.x = 147
        r.y = 13
        d = {'id': 1, '_Rectangle__width': 20,
             '_Rectangle__height': 98, '_Rectangle__x': 147, '_Rectangle__y': 13}
        self.assertDictEqual(r.__dict__, d)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 98)
        self.assertEqual(r.x, 147)
        self.assertEqual(r.y, 13)

    def test_instantiation_keyword(self):
        '''Tests positional instantiation using keywords.'''
        r = Rectangle(100, 200, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    #-----------------------test for 3----------------------

    def test_validate_types(self):
        """Test types of the properties"""
        r  = Rectangle(20, 12)
        attributes = ["width", "height", "x", "y"]
        invalid_types = (None, 10.2, -20.2, float('inf'), float('-inf'),
                         True, "text",[7], {78}, (4,), {4:745})
        
        for attr in attributes:
            msg = f"{attr} must be an integer."
            for inv_type in invalid_types:
                with self.assertRaises(TypeError) as e:
                    setattr(r, attr, inv_type)
                self.assertEqual(str(e.exception), msg)
