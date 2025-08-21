import unittest
import random
import math
from assign1 import *


class TestAssign1Functions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test activity01.py functions """

    def setUp(self):
        self.list_testA = [3, 5, 6, 13, 22, 27, 35]
        self.item_testA = 13
        self.index_testA = self.list_testA.index(self.item_testA)
        self.list_testB = list(range(1, 1001))
        self.item_testB = 500
        self.index_testB = self.list_testB.index(self.item_testB)
        self.list_testC = list(range(1, int(1e7)))
        self.item_testC = int(1e7)+1
        self.linear_testC = linearSearch(self.list_testC, self.item_testC)
        self.binary_testC = binarySearch(self.list_testC, self.item_testC)
        self.trinary_testC = trinarySearch(self.list_testC, self.item_testC)

    def testLinearSearchA(self):
        """ Confirm that linearSearch can find an item """
        ls_res = linearSearch(self.list_testA, self.item_testA)
        print(f"testLinearSearchA runtime = {ls_res[2]:.6f}")
        self.assertEqual(ls_res[0], self.index_testA)
        self.assertEqual(ls_res[1], 4)

    def testBinarySearchA(self):
        """ Confirm that binarySearch can find an item """
        bs_res = binarySearch(self.list_testA, self.item_testA)
        print(f"testBinarySearchA runtime = {bs_res[2]:.6f}")
        self.assertEqual(bs_res[0], self.index_testA)
        self.assertEqual(bs_res[1], 1)

    def testTrinarySearchA(self):
        """ Confirm that trinarySearch can find an item """
        ts_res = trinarySearch(self.list_testA, self.item_testA)
        print(f"testTrinarySearchA runtime = {ts_res[2]:.6f}")
        self.assertEqual(ts_res[0], self.index_testA)
        self.assertLessEqual(ts_res[1], 2*math.log(len(self.list_testA), 3) + 2)

    def testLinearSearchB(self):
        """ Confirm that linearSearch can find an item """
        ls_res = linearSearch(self.list_testB, self.item_testB)
        print(f"testLinearSearchB runtime = {ls_res[2]:.6f}")
        self.assertEqual(ls_res[0], self.index_testB)
        self.assertEqual(ls_res[1], self.item_testB)

    def testBinarySearchB(self):
        """ Confirm that binarySearch can find an item """
        bs_res = binarySearch(self.list_testB, self.item_testB)
        print(f"testBinarySearchB runtime = {bs_res[2]:.6f}")
        self.assertEqual(bs_res[0], self.index_testB)
        self.assertLessEqual(bs_res[1], int(math.log2(len(self.list_testB))) + 1)

    def testTrinarySearchB(self):
        """ Confirm that binarySearch can find an item """
        ts_res = trinarySearch(self.list_testB, self.item_testB)
        print(f"testTrinarySearchB runtime = {ts_res[2]:.6f}")
        self.assertEqual(ts_res[0], self.index_testB)
        self.assertLessEqual(ts_res[1], 2*math.log(len(self.list_testB), 3) + 2)

    def testLinearSearchC(self):
        print(f"testLinearSearchC runtime = {self.linear_testC[2]:.6f}")
        self.assertEqual(self.linear_testC[0], -1)
        self.assertAlmostEqual(self.linear_testC[1]/1e7, 1, 1)

    def testBinarySearchC(self):
        print(f"testBinarySearchC runtime = {self.binary_testC[2]:.6f}")
        self.assertEqual(self.binary_testC[0], -1)
        self.assertAlmostEqual(self.binary_testC[1]/(math.log(1e7, 2)+2), 1, 1)

    def testTrinarySearchC(self):
        print(f"testTrinarySearchC runtime = {self.trinary_testC[2]:.6f}")
        self.assertEqual(self.trinary_testC[0], -1)
        self.assertAlmostEqual(self.trinary_testC[1], (2*math.floor(math.log(1e7, 3))+1), delta=3)

    def testCompareRuntimes(self):
        self.assertLess(self.binary_testC[2], self.linear_testC[2]/5.0)
        self.assertLess(self.trinary_testC[2], self.linear_testC[2]/5.0)
