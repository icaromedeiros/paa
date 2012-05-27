#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import unittest
from paa_code.sort import InsertionSort,MergeSort,QuickSort,HeapSort,MaxHeap


default_array = [8,4,3,1,2,5,9,6,4,2,7]

default_expected_array = [1,2,2,3,4,4,5,6,7,8,9]

class InsertionSortTest(unittest.TestCase):

    def test_insertion_sort(self):
        insertion = InsertionSort()
        ordered_array = insertion.sort(default_array)

        self.assertEquals(default_expected_array,ordered_array)

class MergeSortTest(unittest.TestCase):

    def test_merge_sort(self):
        merge = MergeSort()
        ordered_array = merge.sort(default_array)

        self.assertEquals(default_expected_array,ordered_array)

    def test_merge(self):
        merge = MergeSort()

        array1 = [1,3,5,7,9]
        array2 = [2,2,4,6,8]

        merged_array = merge.merge(array1,array2)

        expected_array = [1,2,2,3,4,5,6,7,8,9]

        self.assertEquals(expected_array,merged_array)

class QuickSortTest(unittest.TestCase):

    def test_quick_sort(self):
        quick = QuickSort()
        ordered_array = quick.sort(default_array)

        self.assertEquals(default_expected_array,ordered_array)

    def test_quick_sort_2(self):
        array = [1,7,5,8,9,3,1,5,6]
        expected_array = [1,1,3,5,5,6,7,8,9]

        quick = QuickSort()
        ordered_array = quick.sort(array)

        self.assertEquals(expected_array,ordered_array)

class HeapSortTest(unittest.TestCase):

    def test_heap_sort(self):
        heap = HeapSort()
        ordered_array = heap.sort(default_array)
        self.assertEquals(default_expected_array,ordered_array)

class MaxHeapTest(unittest.TestCase):

    def test_left_zero(self):
        max_heap = MaxHeap([1])
        left = max_heap.left(0)

        self.assertEquals(1,left)

    def test_left_one(self):
        max_heap = MaxHeap([1])

        left = max_heap.left(1)
        self.assertEquals(3,left)

    def test_left_two(self):
        max_heap = MaxHeap([1])

        left = max_heap.left(2)
        self.assertEquals(5,left)

    def test_right_zero(self):
        max_heap = MaxHeap([1])
        right = max_heap.right(0)

        self.assertEquals(2,right)

    def test_right_one(self):
        max_heap = MaxHeap([1])

        right = max_heap.right(1)
        self.assertEquals(4,right)

    def test_right_two(self):
        max_heap = MaxHeap([1])

        right = max_heap.right(2)
        self.assertEquals(6,right)

    def test_parent_zero(self):
        max_heap = MaxHeap([1])

        parent = max_heap.parent(0)
        self.assertEquals(0,parent)

    def test_parent_one(self):
        max_heap = MaxHeap([1])

        parent = max_heap.parent(1)
        self.assertEquals(0,parent)

    def test_parent_two(self):
        max_heap = MaxHeap([1])

        parent = max_heap.parent(2)
        self.assertEquals(0,parent) 

    def test_parent_three(self):
        max_heap = MaxHeap([1])

        parent = max_heap.parent(3)
        self.assertEquals(1,parent) 

    def test_parent_five(self):
        max_heap = MaxHeap([1])

        parent = max_heap.parent(5)
        self.assertEquals(2,parent)

    def test_parent_six(self):
        max_heap = MaxHeap([1])

        parent = max_heap.parent(6)
        self.assertEquals(2,parent)

    def test_build_max_heap(self):
        not_heap_array = [1,4,3,2]
        max_heap = MaxHeap(not_heap_array)

        self.assertEquals([4,2,3,1],max_heap.array)

    def test_build_max_heap_2(self):
        not_heap_array = [1,2,3,4,5,6]
        max_heap = MaxHeap(not_heap_array)

        self.assertEquals([6,5,3,4,2,1],max_heap.array)


if __name__ == "__main__":
    unittest.main()
