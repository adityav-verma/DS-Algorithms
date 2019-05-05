class PriorityQueue(object):

    QUEUE_UNDERFLOW = 'QueueUnderflow: No keys present in the Queue'
    INVALID_OEPRATION = 'InvalidOperation'
    INT_MIN = -1000000000
    INT_MAX = 1000000000

    def __init__(self, arr=[]):
        self.arr = []
        self.heap_size = -1
        for key in arr:
            self.insert(key)

    def __len__(self):
        return self.heap_size + 1

    def __str__(self):
        queue = 'PriorityQueue: '
        if not self.heap_size < 0:
            for index in range(0, self.heap_size + 1):
                queue = queue + str(self.arr[index]) + " "
        return queue

    def __repr__(self):
        return self.__str__()

    def _max_heapify(self, index):
        left = (index << 1) + 1
        right = (index << 1) + 2
        if left <= self.heap_size and self.arr[left] > self.arr[index]:
            largest = left
        else:
            largest = index
        if right <= self.heap_size and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self._max_heapify(largest)

    def insert(self, key):
        """Insert a new key in the PriorityQueue
        Run time: O(LogN)
        """
        self.heap_size = self.heap_size + 1
        if len(self.arr) > self.heap_size:
            self.arr[self.heap_size] = self.INT_MIN
        else:
            self.arr.append(self.INT_MIN)
        return self.increase_key(self.heap_size, key)

    def maximum(self):
        """Return the maximum element in the PriorityQueue
        Run time: O(LogN)
        """
        if self.heap_size < 0:
            raise Exception(self.QUEUE_UNDERFLOW)
        return self.arr[0]

    def extract_maximum(self):
        """Remove the maximum element from the PriorityQueue
        Run time: O(LogN)
        """
        if self.heap_size < 0:
            raise Exception(self.QUEUE_UNDERFLOW)
        maximum = self.arr[0]
        self.arr[0], self.arr[self.heap_size] = self.arr[self.heap_size], self.arr[0]
        self.heap_size = self.heap_size - 1
        self._max_heapify(0)
        return maximum

    def increase_key(self, index, new_key):
        """Change the value of a key at an index to the new_key
        Run time: O(LogN)
        """
        if self.heap_size < 0 or self.heap_size < index:
            raise Exception(self.QUEUE_UNDERFLOW)
        if self.arr[index] > new_key:
            raise Exception(self.INVALID_OEPRATION)
        self.arr[index] = new_key
        parent = index >> 1
        while parent >= 0 and self.arr[parent] < self.arr[index]:
            self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            index = parent
            parent = index >> 1
        return new_key
