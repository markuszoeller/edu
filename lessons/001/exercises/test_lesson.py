import importlib
import unittest
# from by_student_number.lesson_456723 import Mat456723

lm = importlib.import_module(name="by_student_number.lesson_456723")

class TestLesson001(unittest.TestCase):

    def test_do_something(self):
        m = lm.Mat456723()
        v = m.do_something()
        self.assertEqual(4, v)   #, msg=str(type(m)))

    @unittest.skip("not yet")
    def test_not_yet(self):
        self.assertEqual(True, False)
