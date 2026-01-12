from heap_sort_custom import heap_sort_custom

def compare_report2(a, b):
    '''Название (по возрастанию) + издательство (по убыванию).'''
    if a['title'] != b['title']:
        return a['title'] < b['title']
    return a['publisher'] > b['publisher']


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