#!/usr/bin/env python
#-*- coding:utf-8 -*- 

from optparse import OptionParser

def main():
    print "\nProblem: Sort numbers in an array"

    parser = OptionParser()
    parser.add_option("-v", "--array", dest="array")
    parser.add_option("-i", "--insertion_sort", action="store_true",dest="insertion_sort")
    parser.add_option("-m", "--merge_sort", action="store_true",dest="merge_sort")
    parser.add_option("-q", "--quick_sort", action="store_true",dest="quick_sort")

    (options, args) = parser.parse_args()
    if options.array:
        array_splitted = options.array.split(",")
        array = list()
        usage_message = "Wrong Parameters. Usage: python sort.py -v <number1,number2> <method>"

        for num in array_splitted:
            array.append(int(num))

        print "\nInput array: %s" % array

        final_array = list()

        if options.insertion_sort:
            insertion = InsertionSort()
            final_array = insertion.sort(array)
        elif options.merge_sort:
            merge = MergeSort()
            final_array = merge.sort(array)
        elif options.quick_sort:
            quick = QuickSort()
            final_array = quick.sort(array)
        else:
            print usage_message

        print "Sorted array: %s" % final_array
    else:
        print usage_message

class Sort(object):

    def sort(self,array):
        pass

class InsertionSort(Sort):

    def sort(self,array):

        for i in range(1,len(array)):
            key = array[i]
            j = i

            while j > 0 and array [j-1] > key:
                array[j] = array [j-1]
                j -= 1
            array[j] = key

        return array

class MergeSort(Sort):

    def sort(self,array):

        if len(array) == 1:
            return array

        final_array = list()

        middle = len(array) / 2

        left_array = self.sort(array[0:middle])
        right_array = self.sort(array[middle:len(array)+1])
        final_array = self.merge(left_array,right_array)

        return final_array

    def merge(self,array1,array2):

        i = j = 0
        final_array = list()

        for k in range(len(array1) + len(array2)):

            if i >= len(array1):
                final_array.append(array2[j]) 
                j += 1
                continue

            if j >= len(array2):
                final_array.append(array1[i])
                i += 1
                continue

            if array1[i] < array2[j]:
                final_array.append(array1[i])
                i += 1
            else:
                final_array.append(array2[j])
                j += 1

        return final_array

class QuickSort(Sort):

    def sort(self,array):

        if len(array) <= 1:
            return array

        less, equal, greater = self.partition(array)
        return self.sort(less) + equal + self.sort(greater)

    def partition(self,array):

        less, equal, greater = [], [], []
        pivot = self.select_pivot(array)

        for x in array:
            if x < pivot: 
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return (less, equal, greater)

    def select_pivot(self,array):
        return array[len(array)-1]

class HeapSort(Sort):

    def sort(self,array):

        max_heap = MaxHeap(array)
        final_array = [0] * len(array)

        for i in range(len(array) - 1,-1,-1):
            final_array[i] = max_heap.get(0)
            max_heap.swap(0,i)
            max_heap.remove_last()

            if len(max_heap.array) >= 1: # do not call max_heapify in an empty heap
                max_heap.max_heapify(0)

        return final_array

class MaxHeap(object):

    def __init__(self,array):
        self.array = array
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.array) / 2,-1,-1):
            self.max_heapify(i)

    def max_heapify(self,index):

        left = self.left(index)
        right = self.right(index)

        index_value = self.array[index]
        valor_left = self.array[left] if left < len(self.array) else None
        valor_right = self.array[right] if right < len(self.array) else None

        # leaf node
        if not valor_left and not valor_right:
            return

        greater = None
        if valor_left > index_value and (not valor_right or self.array[left] > self.array[right]):
            greater = left
        elif valor_right and self.array[right] > self.array[index] and self.array[right] > self.array[index]:
            greater = right

        if greater:
            self.swap(index,greater)
            self.max_heapify(greater)

    def swap(self,a,b):
        (self.array[a],self.array[b]) = (self.array[b],self.array[a])

    def get(self,i):
        return self.array[i]

    def remove_last(self):
        self.array = self.array[:-1]

    def left(self,i):
        return 2 * i + 1

    def right(self,i):
        return 2 * i + 2

    def parent(self,i):
        if i == 0 or i == 1:
            return 0
        else:
            if i % 2 == 0:
                return i / 2 - 1
            else:
                return i / 2

if __name__ == "__main__":
    main()
