from read_books import read_books


def test_read_books():
    test_cases = [
        {
            "name": "обычный файл",
            "filename": "files_for_tests_read_books/normal_file.txt",
            "expected": [
                {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'publisher': 'Эксмо', 'year': 1869, 'pages': 1225, 'copies': 3},
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker & Warburg', 'year': 1949, 'pages': 328, 'copies': 7},
                {'author': 'Чехов А.П.', 'title': 'Рассказы', 'publisher': 'Азбука', 'year': 1890, 'pages': 560, 'copies': 5},
                {'author': 'Tolkien', 'title': 'The Lord of the Rings', 'publisher': 'Allen & Unwin', 'year': 1954, 'pages': 1216, 'copies': 6},
                {'author': 'Булгаков М.А.', 'title': 'Мастер и Маргарита', 'publisher': 'Советский писатель', 'year': 1967, 'pages': 480, 'copies': 8},
                {'author': 'Austen', 'title': 'Pride and Prejudice', 'publisher': 'T. Egerton', 'year': 1813, 'pages': 432, 'copies': 4},
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10},
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine Books', 'year': 1953, 'pages': 249, 'copies': 9},
                {'author': 'Гоголь Н.В.', 'title': 'Мёртвые души', 'publisher': 'Оникс', 'year': 1842, 'pages': 352, 'copies': 2},
                {'author': 'Rowling', 'title': 'Harry Potter and the Philosopher', 'publisher': 'Bloomsbury', 'year': 1997, 'pages': 223, 'copies': 12}
            ],
            "expect_error": False,
            "expected_errors": []
        },
        {
            "name": "файл с пустыми строчками",
            "filename": "files_for_tests_read_books/empty_lines_file.txt",
            "expected": [
                {'author': 'Достоевский Ф.М.', 'title': 'Преступление и наказание', 'publisher': 'АСТ', 'year': 1866, 'pages': 672, 'copies': 5},
                {'author': 'Huxley', 'title': 'Brave New World', 'publisher': 'Chatto & Windus', 'year': 1932, 'pages': 311, 'copies': 6},
                {'author': 'Акунин Б.', 'title': 'Азазель', 'publisher': 'Захаров', 'year': 1998, 'pages': 416, 'copies': 8},
                {'author': 'Atwood', 'title': 'The Handmaid\'s Tale', 'publisher': 'McClelland and Stewart', 'year': 1985, 'pages': 311, 'copies': 7},
                {'author': 'Лермонтов М.Ю.', 'title': 'Герой нашего времени', 'publisher': 'Эксмо', 'year': 1840, 'pages': 256, 'copies': 4}
            ],
            "expect_error": False,
            "expected_errors": []
        },
        {
            "name": "файл с пробелами вокруг значений",
            "filename": "files_for_tests_read_books/spaces_around_values.txt",
            "expected": [
                {'author': 'Достоевский Ф.М.', 'title': 'Идиот', 'publisher': 'Айко', 'year': 1869, 'pages': 640, 'copies': 3},
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'Secker & Warburg', 'year': 1945, 'pages': 112, 'copies': 9},
                {'author': 'Пелевин В.О.', 'title': 'Чапаев и Пустота', 'publisher': 'Вагриус', 'year': 1996, 'pages': 448, 'copies': 6},
                {'author': 'Shelley', 'title': 'Frankenstein', 'publisher': 'Lackington, Hughes', 'year': 1818, 'pages': 280, 'copies': 4},
                {'author': 'Грибоедов А.С.', 'title': 'Горе от ума', 'publisher': 'Эксмо', 'year': 1825, 'pages': 128, 'copies': 7}
            ],
            "expect_error": False,
            "expected_errors": []
        },
        {
            "name": "незначащие нули в числах",
            "filename": "files_for_tests_read_books/useless_zeros_in_numbers.txt",
            "expected": [
                {'author': 'Толстой Л.Н.', 'title': 'Анна Каренина', 'publisher': 'Эксмо', 'year': 1877, 'pages': 864, 'copies': 2},
                {'author': 'Asimov', 'title': 'Foundation', 'publisher': 'Gnome Press', 'year': 1951, 'pages': 244, 'copies': 9},
                {'author': 'Чехов А.П.', 'title': 'Вишнёвый сад', 'publisher': 'Азбука', 'year': 1904, 'pages': 112, 'copies': 3},
                {'author': 'Hemingway', 'title': 'The Old Man and the Sea', 'publisher': "Scribner's", 'year': 1952, 'pages': 127, 'copies': 5},
                {'author': 'Булгаков М.А.', 'title': 'Собачье сердце', 'publisher': 'Советский писатель', 'year': 1925, 'pages': 150, 'copies': 7},
                {'author': 'Dick', 'title': 'Do Androids Dream of Electric Sheep?', 'publisher': 'Doubleday', 'year': 1968, 'pages': 210, 'copies': 4},
                {'author': 'Лермонтов М.Ю.', 'title': 'Мцыри', 'publisher': 'Оникс', 'year': 1840, 'pages': 64, 'copies': 1}
            ],
            "expect_error": False,
            "expected_errors": []
        },
        {
            "name": "большие числа",
            "filename": "files_for_tests_read_books/large_numbers.txt",
            "expected": [
                {'author': 'Гоголь Н.В.', 'title': 'Ревизор', 'publisher': 'Азбука', 'year': 1836, 'pages': 1500000000000000000000000, 'copies': 9999999999999999999999999999999999999999999},
                {'author': 'Булгаков М.А.', 'title': 'Собачье сердце', 'publisher': 'Эксмо', 'year': 192523425345345345560000000000, 'pages': 18000000000000000000000000000, 'copies': 12},
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 183333333333333, 'pages': 300, 'copies': 11111111111111111111111111111111111111111111},
                {'author': 'Пушкин А.С.', 'title': 'Капитанская дочка', 'publisher': 'Азбука', 'year': 18333333333333336, 'pages': 200000000000000000, 'copies': 61111111111111111},
                {'author': 'Лермонтов М.Ю.', 'title': 'Герой нашего времени', 'publisher': 'Эксмо', 'year': 184053567356735673567, 'pages': 250, 'copies': 777777777777777777777777777777},
                {'author': 'Достоевский Ф.М.', 'title': 'Идиот', 'publisher': 'АСТ', 'year': 1869, 'pages': 600673567567567537357357356735673567, 'copies': 33451345345435},
                {'author': 'Толстой Л.Н.', 'title': 'Воскресение', 'publisher': 'Азбука', 'year': 189935673567356735673567, 'pages': 70077777777, 'copies': 565735673567567567}
            ],
            "expect_error": False,
            "expected_errors": []
        },
        {
            "name": "пробелы внутри полей",
            "filename": "files_for_tests_read_books/space_inside_fields.txt",
            "expected": [
                {'author': 'Досто евский Ф.М.', 'title': 'Иди от', 'publisher': 'АС Т', 'year': 1869, 'pages': 640, 'copies': 3},
                {'author': 'О рвелл', 'title': '19 84', 'publisher': 'Сек кер & Вар бург', 'year': 1949, 'pages': 328, 'copies': 7},
                {'author': 'Чех ов А.П.', 'title': 'Три сест ры', 'publisher': 'Аз бука', 'year': 1901, 'pages': 180, 'copies': 5},
                {'author': 'Тол стой Л.Н.', 'title': 'Ан на Каре ни на', 'publisher': 'Экс мо', 'year': 1877, 'pages': 864, 'copies': 2},
                {'author': 'Роулинг Дж.К.', 'title': 'Гар ри Пот тер', 'publisher': 'Блумсбери', 'year': 1997, 'pages': 309, 'copies': 10}
            ],
            "expect_error": False,
            "expected_errors": []
        },
                {
            "name": "две одинаковые фамилии",
            "filename": "files_for_tests_read_books/two_identical_surnames.txt",
            "expected": [
                {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'publisher': 'Эксмо', 'year': 1869, 'pages': 1225, 'copies': 3}, 
                {'author': 'Толстой А.Н.', 'title': 'Пётр Первый', 'publisher': 'Азбука', 'year': 1945, 'pages': 916, 'copies': 1}, 
                {'author': 'Чехов А.П.', 'title': 'Рассказы', 'publisher': 'Азбука', 'year': 1890, 'pages': 560, 'copies': 5}, 
                {'author': 'Tolkien', 'title': 'The Lord of the Rings', 'publisher': 'Allen & Unwin', 'year': 1954, 'pages': 1216, 'copies': 6}, 
                {'author': 'Булгаков М.А.', 'title': 'Мастер и Маргарита', 'publisher': 'Советский писатель', 'year': 1967, 'pages': 480, 'copies': 8}, 
                {'author': 'Austen', 'title': 'Pride and Prejudice', 'publisher': 'T. Egerton', 'year': 1813, 'pages': 432, 'copies': 4}
            ],
            "expect_error": False,
            "expected_errors": []

        },
        {
            "name": "неправильное количество элементов",
            "filename": "files_for_tests_read_books/not_six_fields.txt",
            "expected": [
                {'author': 'Толстой Л.Н.', 'title': 'Анна Каренина', 'publisher': 'Эксмо', 'year': 1877, 'pages': 864, 'copies': 5},
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'Secker & Warburg', 'year': 1945, 'pages': 112, 'copies': 8},
                {'author': 'Atwood', 'title': "The Handmaid's Tale", 'publisher': 'McClelland and Stewart', 'year': 1985, 'pages': 311, 'copies': 7}
            ],
            "expect_error": False,
            "expected_errors":[
                "Ошибка в строке 3: ожидается 6 значений, получено 7",f"Ошибка в строке 5: ожидается 6 значений, получено 5"
            ]
                
        },
        {
            "name": "отрицательный год выпуска",
            "filename": "files_for_tests_read_books/negative_year.txt",
            "expected": [
                {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'publisher': 'Эксмо', 'year': 1869, 'pages': 1225, 'copies': 3},
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker & Warburg', 'year': 1949, 'pages': 328, 'copies': 7},
                {'author': 'Чехов А.П.', 'title': 'Рассказы', 'publisher': 'Азбука', 'year': 1890, 'pages': 560, 'copies': 5},
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10},
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine Books', 'year': 1953, 'pages': 249, 'copies': 9},
                {'author': 'Гоголь Н.В.', 'title': 'Мёртвые души', 'publisher': 'Оникс', 'year': 1842, 'pages': 352, 'copies': 2}
            ],
            "expect_error": False,
            "expected_errors": [
                "Ошибка в строке 4: значения должны быть положительными"
            ]
        },
        {
            "name": "отрицательное количество страниц",
            "filename": "files_for_tests_read_books/negative_pages.txt",
            "expected": [
                {'author': 'Tolkien', 'title': 'The Lord of the Rings', 'publisher': 'Allen & Unwin', 'year': 1954, 'pages': 1216, 'copies': 6},
                {'author': 'Austen', 'title': 'Pride and Prejudice', 'publisher': 'T. Egerton', 'year': 1813, 'pages': 432, 'copies': 4},
                {'author': 'Huxley', 'title': 'Brave New World', 'publisher': 'Chatto & Windus', 'year': 1932, 'pages': 311, 'copies': 6},
                {'author': 'Акунин Б.', 'title': 'Азазель', 'publisher': 'Захаров', 'year': 1998, 'pages': 416, 'copies': 8},
                {'author': 'Atwood', 'title': "The Handmaid's Tale", 'publisher': 'McClelland and Stewart', 'year': 1985, 'pages': 311, 'copies': 7},
                {'author': 'Лермонтов М.Ю.', 'title': 'Герой нашего времени', 'publisher': 'Эксмо', 'year': 1840, 'pages': 256, 'copies': 4}
            ],
            "expect_error": False,
            "expected_errors": [
                "Ошибка в строке 3: значения должны быть положительными"
            ]
        },
        {
            "name": "отрицательное количество экземпляров",
            "filename": "files_for_tests_read_books/negative_copies.txt",
            "expected": [
                {'author': 'Грибоедов А.С.', 'title': 'Горе от ума', 'publisher': 'Эксмо', 'year': 1825, 'pages': 128, 'copies': 7},
                {'author': 'Shelley', 'title': 'Frankenstein', 'publisher': 'Lackington, Hughes', 'year': 1818, 'pages': 280, 'copies': 4},
                {'author': 'Пелевин В.О.', 'title': 'Чапаев и Пустота', 'publisher': 'Варгус', 'year': 1996, 'pages': 448, 'copies': 6},
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'Secker & Warburg', 'year': 1945, 'pages': 112, 'copies': 9},
                {'author': 'Тургенев И.С.', 'title': 'Отцы и дети', 'publisher': 'Азбука', 'year': 1862, 'pages': 320, 'copies': 5},
                {'author': 'Хемингуэй Э.', 'title': 'Старик и море', 'publisher': 'АСТ', 'year': 1952, 'pages': 127, 'copies': 8}
            ],
            "expect_error": False,
            "expected_errors": [
                "Ошибка в строке 4: значения должны быть положительными"
            ]
        },
        {
            "name": "некорректный год (строка вместо числа)",
            "filename": "files_for_tests_read_books/invalid_year.txt",
            "expected": [
                {'author': 'Rowling', 'title': 'Harry Potter', 'publisher': 'Bloomsbury', 'year': 1997, 'pages': 223, 'copies': 12},
                {'author': 'Кафка Ф.', 'title': 'Процесс', 'publisher': 'Амфора', 'year': 1925, 'pages': 300, 'copies': 6},
                {'author': 'Толстой Л.Н.', 'title': 'Анна Каренина', 'publisher': 'Эксмо', 'year': 1877, 'pages': 864, 'copies': 5},
                {'author': 'Чехов А.П.', 'title': 'Вишнёвый сад', 'publisher': 'Азбука', 'year': 1904, 'pages': 160, 'copies': 4},
                {'author': 'Пушкин А.С.', 'title': 'Капитанская дочка', 'publisher': 'АСТ', 'year': 1836, 'pages': 256, 'copies': 9},
                {'author': 'Гоголь Н.В.', 'title': 'Ревизор', 'publisher': 'Оникс', 'year': 1836, 'pages': 192, 'copies': 3}
            ],
            "expect_error": False,
            "expected_errors": [
                "Ошибка в строке 4: год, страницы и экземпляры должны быть целыми числами"
            ]
        },
        {
            "name": "некорректные страницы (дробное число)",
            "filename": "files_for_tests_read_books/invalid_pages.txt",
            "expected": [
                {'author': 'Tolkien', 'title': 'The Lord of the Rings', 'publisher': 'Allen & Unwin', 'year': 1954, 'pages': 1216, 'copies': 6},
            {'author': 'Austen', 'title': 'Pride and Prejudice', 'publisher': 'T. Egerton', 'year': 1813, 'pages': 432, 'copies': 4},
            {'author': 'Достоевский Ф.М.', 'title': 'Преступление и наказание', 'publisher': 'АСТ', 'year': 1866, 'pages': 672, 'copies': 5},
            {'author': 'Huxley', 'title': 'Brave New World', 'publisher': 'Chatto & Windus', 'year': 1932, 'pages': 199, 'copies': 6},
            {'author': 'Акунин Б.', 'title': 'Азазель', 'publisher': 'Захаров', 'year': 1998, 'pages': 416, 'copies': 8},
            {'author': 'Лермонтов М.Ю.', 'title': 'Герой нашего времени', 'publisher': 'Эксмо', 'year': 1840, 'pages': 256, 'copies': 4},
            {'author': 'Rowling', 'title': 'Harry Potter', 'publisher': 'Bloomsbury', 'year': 1997, 'pages': 223, 'copies': 12}
            ],
            "expect_error": False,
            "expected_errors": [
                "Ошибка в строке 6: год, страницы и экземпляры должны быть целыми числами"
            ]
        },
        {
            "name": "некорректные экземпляры (слово вместо числа)",
            "filename": "files_for_tests_read_books/invalid_copies.txt",
            "expected": [
                {'author': 'Грибоедов А.С.', 'title': 'Стихотворения', 'publisher': 'Эксмо', 'year': 1820, 'pages': 96, 'copies': 10},
                {'author': 'Пелевин В.О.', 'title': "Generation 'П'", 'publisher': 'Варгус', 'year': 1999, 'pages': 352, 'copies': 7},
                {'author': 'Dostoevsky', 'title': 'The Brothers Karamazov', 'publisher': 'AICo', 'year': 1880, 'pages': 800, 'copies': 5},
                {'author': 'Orwell', 'title': 'Homage to Catalonia', 'publisher': 'Secker & Warburg', 'year': 1938, 'pages': 300, 'copies': 9},
                {'author': 'Тургенев И.С.', 'title': 'Дворянское гнездо', 'publisher': 'Азбука', 'year': 1859, 'pages': 352, 'copies': 6},
                {'author': 'Хемингуэй Э.', 'title': 'Иметь и не иметь', 'publisher': 'АСТ', 'year': 1937, 'pages': 288, 'copies': 4},
            ],
            "expect_error": False,
            "expected_errors": [
                "Ошибка в строке 2: год, страницы и экземпляры должны быть целыми числами"
            ]
        },
        {
            "name": "ноль лет, ноль страниц и ноль экземпляров",
            "filename": "files_for_tests_read_books/zero_years_pages_copies.txt",
            "expected": [
                {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'publisher': 'Эксмо', 'year': 1869, 'pages': 1225, 'copies': 3},
                {'author': 'Чехов А.П.', 'title': 'Рассказы', 'publisher': 'Азбука', 'year': 1890, 'pages': 560, 'copies': 5},
                {'author': 'Булгаков М.А.', 'title': 'Мастер и Маргарита', 'publisher': 'Советский писатель', 'year': 1967, 'pages': 480, 'copies': 8},
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10},
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine Books', 'year': 1953, 'pages': 249, 'copies': 9},
                {'author': 'Гоголь Н.В.', 'title': 'Мёртвые души', 'publisher': 'Оникс', 'year': 1842, 'pages': 352, 'copies': 2}
            ],
            "expect_error": False,
            "expected_errors": [
                "Ошибка в строке 2: значения должны быть положительными"
            ]
        },
        {
            "name": "пустой файл",
            "filename": "files_for_tests_read_books/empty_file.txt",
            "expected": None,
            "expect_error": True,
            "error_message": "Файл для чтения пустой, пожалуйста проверьте наличие данных"
        },
        {
            "name": "файл только с пробелами и табуляций",
            "filename": "files_for_tests_read_books/only_spaces_and_tab.txt",
            "expected": None,
            "expect_error": True,
            "error_message": "Файл не содержит корректных данных (только пустые строки или некорректные записи)"
        }
    ]

    all_passed = True

    for i, case in enumerate(test_cases, 1):

        success, books, errors = read_books(case["filename"]) 

        if case["expect_error"]:
            if success:
                print(f"❌ Тест {i} ({case['name']}): ошибка НЕ возникла")
                all_passed = False
            else:
                # result - это строка с сообщением об ошибке
                if case["error_message"] in books:  # здесь books — это сообщение об ошибке при успехе=False
                    print(f"✅ Тест {i} ({case['name']}): корректная ошибка")
                else:
                    print(f"❌ Тест {i} ({case['name']}): неверное сообщение: {books}")
                    all_passed = False

        else:
            if not success:
                print(f"❌ Тест {i} ({case['name']}): неожиданная ошибка: {books}")
                all_passed = False
            else:
                # Проверяем книги
                if books == case["expected"]:
                    print(f"✅ Тест {i} ({case['name']}): OK")
                else:
                    print(f"❌ Тест {i} ({case['name']}): FAIL")
                    print(f"   Файл:      {case['filename']}")
                    print(f"   Получено:  {books}")
                    print(f"   Ожидалось: {case['expected']}")

                    # Выводим первую отличающуюся книгу
                    for j in range(min(len(books), len(case["expected"]))):
                        got = books[j]
                        exp = case["expected"][j]
                        if got != exp:
                            print(f"   Книга №{j+1} отличается:")
                            print(f"     Получено:  {got}")
                            print(f"     Ожидалось: {exp}")
                            break
                    else:
                        # Если все книги совпадают, но длины разные
                        print(f"   Длины списков разные: получено={len(books)}, ожидалось={len(case['expected'])}")
                    all_passed = False

                # Проверяем ошибки в строках
                if errors != case.get("expected_errors", []):
                    print(f"❌ Тест {i} ({case['name']}): неверный список ошибок")
                    print(f"   Получено:  {errors}")
                    print(f"   Ожидалось: {case.get('expected_errors', [])}")
                    all_passed = False
                else:
                    print(f"   • Ошибки в строках: OK")

    return all_passed
def one_thousand():
    success, books, errors = read_books("files_for_tests_read_books/test_1000.txt")
    
    if not success:
        print("❌ Тест 1000: неожиданная ошибка при чтении файла:", books)
        return False

    k = len(books)
    e = len(errors) if errors else 0

    print(f"✅ Прочитано книг: {k}")
    print(f"   • Ошибок в строках: {e}")

    if k == 900 and e == 100:
        print("✅ Тест 1000: OK - ровно 900 книг и 100 ошибок.")
        return True
    elif k == 900:
        print("⚠️ Тест 1000: FAIL, получено 900 книг, но количество ошибок не совпадает (было", e, ")")
        return False
    else:
        print(f"❌ Тест 1000: ожидалось 900 книг, получено {k}")
        return False


if __name__ == "__main__":
    result1 = test_read_books()
    result2 = one_thousand()
    
    if result1 and result2:
        print("\n🎉 Все тесты, включая 1000-строчный, пройдены!")
    else:
        print("\n⚠️ Некоторые тесты провалены.")