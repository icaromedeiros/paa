#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import unittest
from sort import InsertionSort,MergeSort,QuickSort


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

if __name__ == "__main__":
    unittest.main()
