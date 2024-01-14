def min_heapify(arr, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    smallest = i

    if left_child < len(arr) and arr[left_child] < arr[smallest]:
        smallest = left_child

    if right_child < len(arr) and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest)

def max_heapify(arr, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    largest = i

    if left_child < len(arr) and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < len(arr) and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)

def insert_min_heap(hea
