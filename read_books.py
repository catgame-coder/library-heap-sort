def read_books(filename):
    '''Читает книги из текстового файла.'''
    books = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(';')
            if len(parts) == 6:
                author, title, publisher, year, pages, copies = parts
                books.append({
                    'author': author,
                    'title': title,
                    'publisher': publisher,
                    'year': int(year),
                    'pages': int(pages),
                    'copies': int(copies)
                })
    return books

def print_books(books):
    '''Красивый вывод списка книг.'''
    for book in books:
        print(f"  {book['author']}; {book['title']}; {book['publisher']}; "
              f"{book['year']}; {book['pages']}; {book['copies']}")