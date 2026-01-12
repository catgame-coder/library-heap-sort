from sorted_list_1 import get_sorted_list_1
#Автор по убыванию, год по возрастанию, экземпляры по убыванию'
def test_get_sorted_list_1():
    test_cases = [
        {
            "name": "базовая сортировка по автору",
            "input": [
                {'author': 'Tolkien', 'title': 'LOTR', 'publisher': 'X', 'year': 1954, 'pages': 1000, 'copies': 5},
                {'author': 'Asimov', 'title': 'Foundation', 'publisher': 'Y', 'year': 1951, 'pages': 200, 'copies': 10},
                {'author': 'Bradbury', 'title': 'Fahrenheit', 'publisher': 'Z', 'year': 1953, 'pages': 250, 'copies': 7}
            ],
            "expected": [
                {'author': 'Asimov', 'title': 'Foundation', 'publisher': 'Y', 'year': 1951, 'pages': 200, 'copies': 10},
                {'author': 'Bradbury', 'title': 'Fahrenheit', 'publisher': 'Z', 'year': 1953, 'pages': 250, 'copies': 7},
                {'author': 'Tolkien', 'title': 'LOTR', 'publisher': 'X', 'year': 1954, 'pages': 1000, 'copies': 5}
            ]
        },
        {
            "name": "одинаковый автор — сортировка по году (убывание)",
            "input": [
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'A', 'year': 1945, 'pages': 112, 'copies': 8},
                {'author': 'Orwell', 'title': '1984', 'publisher': 'B', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Orwell', 'title': 'Homage', 'publisher': 'C', 'year': 1938, 'pages': 300, 'copies': 6}
            ],
            "expected": [
                {'author': 'Orwell', 'title': '1984', 'publisher': 'B', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'A', 'year': 1945, 'pages': 112, 'copies': 8},
                {'author': 'Orwell', 'title': 'Homage', 'publisher': 'C', 'year': 1938, 'pages': 300, 'copies': 6}
            ]
        },
        {
            "name": "одинаковый автор и год — сортировка по экземплярам (убывание)",
            "input": [
                {'author': 'King', 'title': 'It', 'publisher': 'P1', 'year': 1986, 'pages': 1100, 'copies': 3},
                {'author': 'King', 'title': 'The Stand', 'publisher': 'P2', 'year': 1986, 'pages': 800, 'copies': 10},
                {'author': 'King', 'title': 'Carrie', 'publisher': 'P3', 'year': 1986, 'pages': 200, 'copies': 7}
            ],
            "expected": [
                {'author': 'King', 'title': 'The Stand', 'publisher': 'P2', 'year': 1986, 'pages': 800, 'copies': 10},
                {'author': 'King', 'title': 'Carrie', 'publisher': 'P3', 'year': 1986, 'pages': 200, 'copies': 7},
                {'author': 'King', 'title': 'It', 'publisher': 'P1', 'year': 1986, 'pages': 1100, 'copies': 3}
            ]
        },
        {
            "name": "полные дубликаты — не должно быть ошибки",
            "input": [
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10},
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10},
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10}
            ],
            "expected": [
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10},
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10},
                {'author': 'Пушкин А.С.', 'title': 'Евгений Онегин', 'publisher': 'АСТ', 'year': 1833, 'pages': 288, 'copies': 10}
            ]
        },
        {
            "name": "сложный случай: перекрывающиеся группы",
            "input": [
                {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'publisher': 'Эксмо', 'year': 1869, 'pages': 1225, 'copies': 2},
                {'author': 'Булгаков М.А.', 'title': 'Мастер и Маргарита', 'publisher': 'Сов. писатель', 'year': 1967, 'pages': 480, 'copies': 5},
                {'author': 'Толстой Л.Н.', 'title': 'Анна Каренина', 'publisher': 'Азбука', 'year': 1877, 'pages': 864, 'copies': 8},
                {'author': 'Булгаков М.А.', 'title': 'Белая гвардия', 'publisher': 'АСТ', 'year': 1925, 'pages': 400, 'copies': 12},
                {'author': 'Булгаков М.А.', 'title': 'Собачье сердце', 'publisher': 'Варгус', 'year': 1925, 'pages': 160, 'copies': 3}
            ],
            "expected": [
                {'author': 'Булгаков М.А.', 'title': 'Мастер и Маргарита', 'publisher': 'Сов. писатель', 'year': 1967, 'pages': 480, 'copies': 5},
                {'author': 'Булгаков М.А.', 'title': 'Белая гвардия', 'publisher': 'АСТ', 'year': 1925, 'pages': 400, 'copies': 12},
                {'author': 'Булгаков М.А.', 'title': 'Собачье сердце', 'publisher': 'Варгус', 'year': 1925, 'pages': 160, 'copies': 3},
                {'author': 'Толстой Л.Н.', 'title': 'Анна Каренина', 'publisher': 'Азбука', 'year': 1877, 'pages': 864, 'copies': 8},
                {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'publisher': 'Эксмо', 'year': 1869, 'pages': 1225, 'copies': 2}
            ]
        }
    ]

    all_passed = True

    for i, case in enumerate(test_cases, 1):
        input_books = [b.copy() for b in case["input"]]
        result = get_sorted_list_1(input_books)

        if result == case["expected"]:
            print(f"✅ Тест {i} ({case['name']}): OK")
        else:
            print(f"❌ Тест {i} ({case['name']}): FAIL")
            print(f"   Вход: {len(case['input'])} книг")

            # Находим первую отличающуюся книгу
            for j in range(min(len(result), len(case["expected"]))):
                got = result[j]
                exp = case["expected"][j]
                if got != exp:
                    print(f"   Первая отличающаяся книга (№{j+1}):")
                    print(f"     Получено:  {got}")
                    print(f"     Ожидалось: {exp}")
                    break
            else:
                # Если все книги совпадают, но длины разные
                print(f"   Длины списков разные: получено={len(result)}, ожидалось={len(case['expected'])}")
            all_passed = False

    return all_passed


if __name__ == "__main__":
    success = test_get_sorted_list_1()
    if success:
        print("\n🎉 Все тесты get_sorted_list_1 пройдены!")
    else:
        print("\n⚠️ Некоторые тесты провалены.")