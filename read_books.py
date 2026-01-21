def read_books(filename):
    '''Читает книги из текстового файла. Возвращает (успех, данные_или_ошибка, ошибки_строк).'''
    
    content = None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return False, f"Файл '{filename}' не найден. Пожалуйста, проверьте наличие файла.", None
    except PermissionError:
        return False, f"Нет прав на чтение файла '{filename}'.", None
    except Exception as e:
        return False, f"Ошибка при открытии файла: {e}", None

    # Проверка: пустой ли файл (физически)
    if len(content) == 0:
        return False, 'Файл для чтения пустой, пожалуйста проверьте наличие данных.', None

    # Теперь обрабатываем строки
    errors = []
    books = []
    lines = content.splitlines()

    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue  # Пропускаем пустые строки

        parts = line.split(';')
        if len(parts) != 6:
            errors.append(f"Ошибка в строке {line_num}: ожидается 6 значений, получено {len(parts)}")
            continue

        author = parts[0].strip()
        title = parts[1].strip()
        publisher = parts[2].strip()
        year_str = parts[3].strip()
        pages_str = parts[4].strip()
        copies_str = parts[5].strip()

        if not year_str or not pages_str or not copies_str:
            errors.append(f"Ошибка в строке {line_num}: числовые поля не могут быть пустыми")
            continue

        try:
            year = int(year_str)
            pages = int(pages_str)
            copies = int(copies_str)
        except ValueError:
            errors.append(f"Ошибка в строке {line_num}: год, страницы и экземпляры должны быть целыми числами")
            continue

        if year <= 0 or pages <= 0 or copies <= 0:
            errors.append(f"Ошибка в строке {line_num}: значения должны быть положительными")
            continue

        books.append({
            'author': author,
            'title': title,
            'publisher': publisher,
            'year': year,
            'pages': pages,
            'copies': copies
        })

    if not books:
        return False, "Файл не содержит корректных данных (только пустые строки или некорректные записи).", None

    return True, books, errors


def print_books(books):
    '''Красивый вывод списка книг.'''
    for book in books:
        print(f"  {book['author']}; {book['title']}; {book['publisher']}; "
              f"{book['year']}; {book['pages']}; {book['copies']}")