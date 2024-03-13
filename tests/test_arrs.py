import unittest
from unittest_proj.utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_get_out_of_bounds_index(self):
        self.assertEqual(arrs.get([1, 2, 3],5, "test"), "test")

    def test_get_negative_index(self):
        self.assertEqual(arrs.get([1,2,3],-1,"test"),"test")

    def test_slice_no_start_no_end(self):
        self.assertEqual(arrs.my_slice([1,2,3,4]),[1,2,3,4])

    def test_slice_negative_start(self):
        self.assertEqual(arrs.my_slice([1,2,3,4],-2),[3,4])

    def test_slice_negative_end(self):
        self.assertEqual(arrs.my_slice([1,2,3,4],end=-2),[1,2])

    def test_slice_negative_start_and_end(self):
        self.assertEqual(arrs.my_slice([1,2,3,4],-2,-1),[3])