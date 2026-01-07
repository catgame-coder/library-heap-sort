from heap_sort_custom import heap_sort_custom

def compare_report3(a, b):
    if a['year'] != b['year']:
        return a['year'] < b['year']
    return a['author'] > b['author']

def get_sorted_list_3(books, n1, n2):
    '''Возвращает отсортированные книги в диапазоне лет [n1, n2].'''
    filtered = [b for b in books if n1 <= b['year'] <= n2]
    if not filtered:
        return []
    books_copy = [b.copy() for b in filtered]
    heap_sort_custom(books_copy, compare_report3)
    return books_copy