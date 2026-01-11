def read_books(filename):
    '''Читает книги из текстового файла.'''
    books = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue  # Пропускаем пустые строки

            parts = line.split(';')
            if len(parts) != 6:
                raise ValueError(f"Ошибка в строке {line_num}: ожидается 6 значений, получено {len(parts)}")

            # Убираем пробелы вокруг каждого поля
            author = parts[0].strip()
            title = parts[1].strip()
            publisher = parts[2].strip()
            year_str = parts[3].strip()
            pages_str = parts[4].strip()
            copies_str = parts[5].strip()

            # Проверяем, что числовые поля не пустые
            if not year_str or not pages_str or not copies_str:
                raise ValueError(f"Ошибка в строке {line_num}: числовые поля не могут быть пустыми")

            # Преобразуем в целые числа
            try:
                year = int(year_str)
                pages = int(pages_str)
                copies = int(copies_str)
            except ValueError:
                raise ValueError(f"Ошибка в строке {line_num}: год, страницы и экземпляры должны быть целыми числами")

            # Проверяем, что значения положительные
            if year <= 0 or pages <= 0 or copies <= 0:
                raise ValueError(f"Ошибка в строке {line_num}: значения должны быть положительными")

            # Добавляем книгу в список
            books.append({
                'author': author,
                'title': title,
                'publisher': publisher,
                'year': year,
                'pages': pages,
                'copies': copies
            })

    # Если ни одной книги не прочитано — ошибка
    if not books:
        raise ValueError("Файл для чтения пустой, пожалуйста проверьте наличие данных")

    return books

def print_books(books):
    '''Красивый вывод списка книг.'''
    for book in books:
        print(f"  {book['author']}; {book['title']}; {book['publisher']}; "
              f"{book['year']}; {book['pages']}; {book['copies']}")