"""
This script provides comparison of runtime of the five common sorting
algorithms.

Bubble sort     :   Exchange two adjacent elements if they are out of order.
                    Repeat until array is sorted.
Insertion sort  :   Scan successive elements for an out-of-order item, then
                    insert the item in the proper place.
Selection sort  :   Find the smallest element in the array, and put it in the
                    proper place. Swap it with the value in the first
                    position. Repeat until array is sorted.
Quick sort      :   Partition the array into two segments. In the first
                    segment, all elements are less than or equal to the pivot
                    value. In the second segment, all elements are greater
                    than or equal to the pivot value. Finally, sort the two
                    segments recursively.
Merge sort      :   Divide the list of elements in two parts, sort the two
                    parts individually and then merge it.
"""

import time
import random


class BubbleSort:
    """
    Bubble sort, sometimes referred to as sinking sort, is a simple sorting
    algorithm that repeatedly steps through the list to be sorted, compares
    each pair of adjacent items and swaps them if they are in the wrong order.
    """
    def __init__(self, arr):
        start_time = time.time()
        sorted_arr = BubbleSort.bubble_sort(arr)
        elapsed_time = time.time() - start_time
        print('::Bubble Sort::', sorted_arr, 'Time Elapsed = {}'
              .format(elapsed_time), sep='\n', end='\n\n')

    @staticmethod
    def bubble_sort(arr):
        for i in range(len(arr)-1, 0, -1):
            pre_sorted = True
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    pre_sorted = False
            if pre_sorted:
                break
        return arr


class InsertionSort:
    """
    Insertion sort is a simple sorting algorithm that builds the final sorted
    array (or list) one item at a time. It is much less efficient on large
    lists than more advanced algorithms such as quicksort, heapsort, or merge
    sort.
    """

    def __init__(self, arr):
        start_time = time.time()
        sorted_arr = self.insertion_sort(arr)
        elapsed_time = time.time() - start_time
        print('::Insertion Sort::', sorted_arr, 'Time Elapsed = {}'
              .format(elapsed_time), sep='\n', end='\n\n')

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
        return arr


class SelectionSort:
    """
    The selection sort is a combination of searching and sorting. During each
    pass, the unsorted element with the smallest (or largest) value is moved
    to its proper position in the array. The number of times the sort passes
    through the array is one less than the number of items in the array.
    """

    def __init__(self, arr):
        start_time = time.time()
        sorted_arr = self.selection_sort(arr)
        elapsed_time = time.time() - start_time
        print('::Selection Sort::', sorted_arr, 'Time Elapsed = {}'
              .format(elapsed_time), sep='\n', end='\n\n')

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr)-1):
            min_value = min(arr[i:])
            index = arr.index(min_value)
            arr[i], arr[index] = arr[index], arr[i]
        return arr


class QuickSort:
    """
    Quicksort (sometimes called partition-exchange sort) is an efficient
    sorting algorithm, serving as a systematic method for placing the elements
    of an array in order. When implemented well, it can be about two or three
    times faster than its main competitors, merge sort and heapsort.
    """

    def __init__(self, arr):
        start_time = time.time()
        sorted_arr = self.quick_sort(arr, 0, len(arr)-1)
        elapsed_time = time.time() - start_time
        print('::Quick Sort::', sorted_arr, 'Time Elapsed = {}'
              .format(elapsed_time), sep='\n', end='\n\n')

    @staticmethod
    def quick_sort(arr, start, end):
        if start < end:
            pivot = QuickSort.partition(arr, start, end)
            QuickSort.quick_sort(arr, start, pivot-1)
            QuickSort.quick_sort(arr, pivot+1, end)
        return arr

    @staticmethod
    def partition(arr, start, end):
        pivot = start
        left = start+1
        right = end
        while True:
            while left <= right and arr[left] <= arr[pivot]:
                left += 1
            while arr[right] >= arr[pivot] and right >= left:
                right -= 1
            if right < left:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[pivot], arr[right] = arr[right], arr[pivot]
        return right


class MergeSort:
    """
    Merge sort is a sorting technique based on divide and conquer technique.
    With worst-case time complexity being Ο(n log n), it is one of the most
    respected algorithms. Merge sort first divides the array into equal halves
    and then combines them in a sorted manner.
    """

    def __init__(self, arr):
        start_time = time.time()
        sorted_arr = self.merge_sort(arr)
        elapsed_time = time.time() - start_time
        print('::Merge Sort::', sorted_arr, 'Time Elapsed = {}'.format(elapsed_time),
              sep='\n', end='\n\n')

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            left_array = MergeSort.merge_sort(arr[:len(arr)//2])
            right_array = MergeSort.merge_sort(arr[len(arr)//2:])
            return MergeSort.merge(left_array, right_array)

    @staticmethod
    def merge(left_array, right_array):
        temp_array = []
        while left_array and right_array:
            if left_array[0] < right_array[0]:
                temp_array.append(left_array.pop(0))
            else:
                temp_array.append(right_array.pop(0))
        if left_array:
            temp_array.extend(left_array)
        if right_array:
            temp_array.extend(right_array)
        return temp_array


class PythonListSort:
    """
    List sort of Python 3.
    """

    def __init__(self, arr):
        start_time = time.time()
        arr.sort()
        elapsed_time = time.time() - start_time
        print('::Inbuilt Sort Method::', arr, 'Time Elapsed = {}'.format(elapsed_time),
              sep='\n', end='\n\n')


if __name__ == '__main__':
    input_array = [random.randint(-100, 100) for i in range(10)]
    BubbleSort(input_array[:])
    InsertionSort(input_array[:])
    SelectionSort(input_array[:])
    QuickSort(input_array[:])
    MergeSort(input_array[:])
    PythonListSort(input_array[:])
