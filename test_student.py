"""
Cara Krug 11/1/2020 cjkrug@dmacc.edu
Write unit tests to test the Student class:
Include setUp() and tearDown() methods
Write unit test test_object_created_all_attributes(self)
Write unit test test_student_str(self) etc..
"""

import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Janeway', 'Kathryn', 'CIS', 4.0)
    def tearDown(self):
        del self.student
    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Janeway')
        self.assertEqual(self.student.first_name, 'Kathryn')
        self.assertEqual(self.student.major, 'CIS')
    def test_object_created_all_attributes(self):
        student = s.Student('Janeway', 'Kathryn', 'CIS', 4.0)
        assert student.last_name == 'Janeway'
        assert student.first_name == 'Kathryn'
        assert student.major == 'CIS'
        assert student.gpa == 4.0
    def test_student_str(self):
        self.assertEqual(str(self.student), 'Janeway, Kathryn major CIS with gpa: 4.0')
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = s.Student('333', 'Kathryn', 'CIS')
    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = s.Student('Janeway', '333', 'CIS')
    def test_object_not_created_error_in_major(self):
        with self.assertRaises(ValueError):
            p = s.Student('Janeway', 'Kathryn', 'Reading')
    def test_object_not_created_error_in_gpa(self):
        with self.assertRaises(ValueError):
            p = s.Student('Janeway', 'Kathryn', 'CIS', 5.0)
            d = s.Student('Janeway', 'Kathryn', 'CIS', 2)
            q = s.Student('Janeway', 'Kathryn', 'CIS', 'Four Point O')
