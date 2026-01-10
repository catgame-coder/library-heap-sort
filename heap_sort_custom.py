from heapify import heapify

def heap_sort_custom(array, compare_func):
    '''
    Пирамидальная сортировка с пользовательской функцией сравнения.
    Функция compare_func(a, b) должна возвращать True, если a < b (т.е. a должен идти ПОЗЖЕ b в отсортированном порядке).
    '''
    heap_size = len(array)

    if not array:
        return
    
    # Проверяем, что все элементы одного типа
    first_type = type(array[0])
    for item in array:
        if type(item) != first_type:
            raise ValueError("Нельзя смешивать разные типы данных")

    # Строим кучу: начинаем с последнего родителя (индекс = heap_size // 2 - 1) и идём вверх до корня (индекс 0), включительно.
    # Шаг -1 — движение справа налево по родителям.
    for last_parent_index in range(heap_size // 2 - 1, -1, -1):
        heapify(array, heap_size, last_parent_index, compare_func)

    # Извлекаем элементы: от последнего индекса (heap_size - 1) до второго (1), потому что когда останется один элемент — он уже на месте.
    # На каждом шаге максимум (корень) перемещается в конец текущей неотсортированной части.
    for sorted_tail_start in range(heap_size - 1, 0, -1):
        array[0], array[sorted_tail_start] = array[sorted_tail_start], array[0]
        heapify(array, sorted_tail_start, 0, compare_func)