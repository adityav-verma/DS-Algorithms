def max_heapify(arr, index, heap_size):
	left = (index << 1) + 1
	right = (index << 1) + 2
	if left < heap_size and arr[left] > arr[index]:
		largest = left
	else:
		largest = index
	if right < heap_size and arr[right] > arr[largest]:
		largest = right
	if largest != index:
		arr[index], arr[largest] = arr[largest], arr[index]
		max_heapify(arr, largest, heap_size)


def build_max_heap(arr):
	mid = int(len(arr)/2)
	for index in range(mid, -1, -1):
		max_heapify(arr, index, len(arr))

def heap_sort(arr):
	build_max_heap(arr)
	for i in range(len(arr) -1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		max_heapify(arr, 0, i)


a = [10, 1, 2, 3, 6, 7, 8, 4, 5, 9]
heap_sort(a)
print(a)