"""A class implementing QuickSort"""
import random


class QuickSort(object):

    @classmethod
    def _partition(cls, arr, sindex, eindex):
        """Picks the last element as the partition and divides the array around
        the partition
        """
        value = arr[eindex]
        i = sindex - 1
        for j in range(sindex, eindex):
            if arr[j] <= value:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        arr[i], arr[eindex] = arr[eindex], arr[i]
        return i

    @classmethod
    def _randomized_partition(cls, arr, sindex, eindex):
        """Randomly selects an index as the partition and then swaps it with
        the last element. Post that normal partiion is called
        """
        random_index = random.randint(sindex, eindex)
        arr[random_index], arr[eindex] = arr[eindex], arr[random_index]
        return cls._partition(arr, sindex, eindex)

    @classmethod
    def _sort(cls, arr, sindex, eindex, randomized):
        """Sort the given array in the given range using QuickSort. Randomized
        QuickSort can be used by setting the passing True to the last arg
        """
        if sindex >= eindex:
            return
        partition = None
        if randomized:
            partition = cls._randomized_partition(arr, sindex, eindex)
        else:
            partition = cls._partition(arr, sindex, eindex)
        cls._sort(arr, sindex, partition - 1, randomized)
        cls._sort(arr, partition + 1, eindex, randomized)

    @classmethod
    def sort(cls, arr, randomized=False):
        cls._sort(arr, 0, len(arr) - 1, randomized)
