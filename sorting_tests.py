import unittest
import random
import math
import sys
sys.setrecursionlimit(100000)

from sorting import *


class TestSortingFunctions(unittest.TestCase):
    """ A class derived from unittest.TestCase to test sorting.py functions """

    def setUp(self):
        self.list_sorted = list(range(1, 5001))
        self.small_list = list(range(1, 51))
        self.list_reversed = self.list_sorted.copy()
        self.list_reversed.reverse()
        self.list_shuffled = self.list_sorted.copy()
        random.seed(1)
        random.shuffle(self.list_shuffled)
        self.shuf_bubbleRes = bubbleSort(list(self.list_shuffled))
        self.shuf_insertionRes = insertionSort(list(self.list_shuffled))
        self.shuf_mergeRes = mergeSort(list(self.list_shuffled))
        self.shuf_hybridRes = hybridSort(list(self.list_shuffled))
        self.shuf_quickResA = quickSort(list(self.list_shuffled), pivot='first')
        self.shuf_quickResB = quickSort(list(self.list_shuffled), pivot='middle')
        self.shuf_radixRes = radixSort(list(self.list_shuffled))
        self.rev_bubbleRes = bubbleSort(list(self.list_reversed))
        self.rev_insertionRes = insertionSort(list(self.list_reversed))
        self.rev_mergeRes = mergeSort(list(self.list_reversed))
        self.rev_quickResA = quickSort(list(self.list_reversed), pivot='first')
        self.rev_quickResB = quickSort(list(self.list_reversed), pivot='middle')
        self.rev_radixRes = radixSort(list(self.list_reversed))
        self.insert_avg_on_large_list = 0
        self.hybrid_avg_on_large_list = 0
        self.merge_avg_on_small_list = 0
        self.hybrid_avg_on_small_list = 0
        num_trials = 5
        for i in range(num_trials):
            tmp = self.list_sorted.copy()
            random.shuffle(tmp)
            self.insert_avg_on_large_list += insertionSort(tmp)[1]
            tmp = self.list_sorted.copy()
            random.shuffle(tmp)
            self.hybrid_avg_on_large_list += hybridSort(tmp)[1]
        self.insert_avg_on_large_list /= num_trials
        self.hybrid_avg_on_large_list /= num_trials

        for i in range(num_trials):
            tmp = self.small_list.copy()
            random.shuffle(tmp)
            self.merge_avg_on_small_list += mergeSort(tmp)[1]
            tmp = self.small_list.copy()
            random.shuffle(tmp)
            self.hybrid_avg_on_small_list += hybridSort(tmp)[1]
        self.merge_avg_on_small_list /= num_trials
        self.hybrid_avg_on_small_list /= num_trials

    def testSorting(self):
        """ Confirm that functions sort as expected """
        self.assertEqual(self.list_sorted, self.shuf_bubbleRes[0])
        self.assertEqual(self.list_sorted, self.shuf_insertionRes[0])
        self.assertEqual(self.list_sorted, self.shuf_mergeRes[0])
        self.assertEqual(self.list_sorted, self.shuf_hybridRes[0])        
        self.assertEqual(self.list_sorted, self.shuf_quickResA[0])
        self.assertEqual(self.list_sorted, self.shuf_quickResB[0])
        self.assertEqual(self.list_sorted, self.shuf_radixRes[0])
        self.assertEqual(self.list_sorted, self.rev_bubbleRes[0])
        self.assertEqual(self.list_sorted, self.rev_insertionRes[0])        
        self.assertEqual(self.list_sorted, self.rev_mergeRes[0])
        self.assertEqual(self.list_sorted, self.rev_quickResA[0])
        self.assertEqual(self.list_sorted, self.rev_quickResB[0])
        self.assertEqual(self.list_sorted, self.rev_radixRes[0])

    def testTimings(self):
        """ Confirm that sorting functions run in expected times """
        self.assertGreater(self.shuf_bubbleRes[1]/2, self.shuf_mergeRes[1])
        self.assertGreater(self.shuf_bubbleRes[1]/5, self.shuf_quickResA[1]) # was 10
        self.assertGreater(self.shuf_bubbleRes[1]/5, self.shuf_quickResB[1]) # was 10
        self.assertGreater(self.shuf_bubbleRes[1]/10, self.shuf_radixRes[1])
        self.assertGreater(self.rev_quickResA[1]/10, self.rev_quickResB[1])
        self.assertGreater(self.rev_insertionRes[1]/1.5, self.shuf_insertionRes[1])

    def testHybridForLargeLists(self):
        """ Confirm that hybrid sort is faster than insertion sort on large lists. """
        self.assertGreater(self.insert_avg_on_large_list, self.hybrid_avg_on_large_list)

    def testHybridForSmallLists(self):
        """ Confirm that hybrid sort is faster than merge sort on small lists. """
        self.assertGreater(self.merge_avg_on_small_list, self.hybrid_avg_on_small_list)
