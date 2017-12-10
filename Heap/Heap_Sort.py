from Heap import Heap

def heap_sort(items, cmp_func):
    sorted_array = []
    if cmp_func is None:
        cmp_func = lambda parent, child: parent <= child

    heap = Heap(cmp_func)
    heap.build_heap(items)
    while heap.size > 0:
        sorted_array.append(heap.pop())

    return sorted_array
