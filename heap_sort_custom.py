from heapify import heapify

def heap_sort_custom(array, compare_func):
    '''
    Пирамидальная сортировка с пользовательской функцией сравнения.
    Функция compare_func(a, b) должна возвращать True, если a < b (т.е. a должен идти ПОЗЖЕ b в отсортированном порядке).
    '''
    heap_size = len(array)

    # Построение кучи
    for last_parent_index in range(heap_size // 2 - 1, -1, -1):
        heapify(array, heap_size, last_parent_index, compare_func)

    # Извлечение элементов
    for sorted_tail_start in range(heap_size - 1, 0, -1):
        array[0], array[sorted_tail_start] = array[sorted_tail_start], array[0]
        heapify(array, sorted_tail_start, 0, compare_func)