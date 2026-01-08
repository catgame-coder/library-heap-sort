from heap_sort_custom import heap_sort_custom

'''Сортировка по издателю ↓, названию ↑ для конкретного автора'''
def compare_report2(a, b):
    if a['author'] != b['author']:
        raise ValueError("Сравнение книг разных авторов")
    if a['publisher'] != b['publisher']:
        return a['publisher'] < b['publisher']
    return a['title'] > b['title']


def compare_author_asc(x, y):
    '''Сравнение двух строк (авторов) по возрастанию.'''
    return x > y


def get_all_authors(books):
    '''Возвращает список уникальных авторов, отсортированный по алфавиту (по возрастанию).'''
    if not books: 
        return []
    unique_authors =list(set(b['author'] for b in books))
    heap_sort_custom(unique_authors,compare_author_asc)
    return unique_authors


def get_sorted_list_2(books, author):
    '''Возвращает отсортированные книги указанного автора.'''
    filtered = [b for b in books if b['author'] == author]
    if not filtered:
        return []
    books_copy = [b.copy() for b in filtered]
    heap_sort_custom(books_copy, compare_report2)
    return books_copy