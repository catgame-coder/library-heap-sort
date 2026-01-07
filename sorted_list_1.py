from heap_sort_custom import heap_sort_custom

def compare_report1(a, b):
    '''Автор ↑, год ↓, экземпляры ↓'''
    if a['author'] != b['author']:
        return a['author'] > b['author']   # если a > b → a должен быть ПОЗЖЕ → значит, в куче b "больше"
    if a['year'] != b['year']:
        return a['year'] < b['year']       # по убыванию: если a < b → a позже
    return a['copies'] < b['copies']

def get_sorted_list_1(books):
    '''Возвращает отсортированный список по отчёту 1.'''
    books_copy = [b.copy() for b in books]
    heap_sort_custom(books_copy, compare_report1)
    return books_copy