#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import unittest
from sort import InsertionSort,MergeSort,QuickSort,MaxHeap


vetor_default = [8,4,3,1,2,5,9,6,4,2,7]

vetor_esperado_default = [1,2,2,3,4,4,5,6,7,8,9]

class InsertionSortTest(unittest.TestCase):

    def test_insertion_sort(self):
        insertion = InsertionSort()
        vetor_ordenado = insertion.sort(vetor_default)

        self.assertEquals(vetor_esperado_default,vetor_ordenado)

class MergeSortTest(unittest.TestCase):

    def test_merge_sort(self):
        merge = MergeSort()
        vetor_ordenado = merge.sort(vetor_default)

        self.assertEquals(vetor_esperado_default,vetor_ordenado)

    def test_intercalacao(self):
        merge = MergeSort()

        vetor1 = [1,3,5,7,9]
        vetor2 = [2,2,4,6,8]

        vetor_intercalado = merge.intercalacao(vetor1,vetor2)

        vetor_esperado = [1,2,2,3,4,5,6,7,8,9]

        self.assertEquals(vetor_esperado,vetor_intercalado)

class QuickSortTest(unittest.TestCase):

    def test_quick_sort(self):
        quick = QuickSort()
        vetor_ordenado = quick.sort(vetor_default)

        self.assertEquals(vetor_esperado_default,vetor_ordenado)

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

    def test_max_heapify(self):
        vetor_nao_heap = [1,4,3,2]
        max_heap = MaxHeap(vetor_nao_heap)

        self.assertEquals([4,2,3,1],max_heap.vetor)

    def test_max_heapify_2(self):
        vetor_nao_heap = [1,2,3,4,5,6]
        max_heap = MaxHeap(vetor_nao_heap)

        self.assertEquals([6,5,3,4,2,1],max_heap.vetor)

if __name__ == "__main__":
    unittest.main()
