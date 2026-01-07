def heapify(array, heap_size, index, compare_func):
    '''
    Восстанавливает кучу с использованием пользовательской функции сравнения.
    compare_func(a, b) должна возвращать True, если a < b (т.е. a "меньше" b → b должен быть выше в куче). (для макс-кучи)
    '''
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and compare_func(array[largest], array[left]):
        largest = left

    if right < heap_size and compare_func(array[largest], array[right]):
        largest = right

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, heap_size, largest, compare_func)