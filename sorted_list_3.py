from heap_sort_custom import heap_sort_custom

def compare_report3(a, b):
    '''Автор (по возрастанию) + год выпуска (по убыванию).'''
    if a['year'] != b['year']:
        return a['year'] > b['year']
    return a['author'] < b['author']

def get_sorted_list_3(books, n1, n2):
    '''Возвращает отсортированные книги в диапазоне лет [n1, n2].'''
    filtered = [b for b in books if n1 <= b['year'] <= n2]
    if not filtered:
        return []
    books_copy = [b.copy() for b in filtered]
    heap_sort_custom(books_copy, compare_report3)
    return books_copy

def get_year_range(books):
    '''Возвращает кортеж (min_year, max_year) из списка книг.'''
    if not books:
        raise ValueError("Список книг пуст. Проверьте файл books.txt.")

    min_year = books[0]['year']
    max_year = books[0]['year']

    for book in books[1:]:
        year = book['year']
        if year < min_year:
            min_year = year
        if year > max_year:
            max_year = year

    return (min_year, max_year)