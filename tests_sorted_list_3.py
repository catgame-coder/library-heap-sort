from sorted_list_3 import get_sorted_list_3
# Год выпуска (по убыванию) + автор (по возрастанию)
def test_get_sorted_list_3():
    test_cases = [
        {
            "name": "базовая сортировка: разные авторы и года",
            "input": [
                {'author': 'Tolkien', 'title': 'LOTR', 'publisher': 'Allen', 'year': 1954, 'pages': 1200, 'copies': 10},
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine', 'year': 1953, 'pages': 249, 'copies': 9}
            ],
            "n1": 1940,
            "n2": 1960,
            "expected": [
                {'author': 'Tolkien', 'title': 'LOTR', 'publisher': 'Allen', 'year': 1954, 'pages': 1200, 'copies': 10},
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine', 'year': 1953, 'pages': 249, 'copies': 9},
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5}
            ]
        },
        {
            "name": "одинаковый автор — сортировка по году (убывание)",
            "input": [
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'A', 'year': 1945, 'pages': 112, 'copies': 8},
                {'author': 'Orwell', 'title': '1984', 'publisher': 'B', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Orwell', 'title': 'Homage', 'publisher': 'C', 'year': 1938, 'pages': 300, 'copies': 6}
            ],
            "n1": 1930,
            "n2": 1950,
            "expected": [
                {'author': 'Orwell', 'title': '1984', 'publisher': 'B', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'A', 'year': 1945, 'pages': 112, 'copies': 8},
                {'author': 'Orwell', 'title': 'Homage', 'publisher': 'C', 'year': 1938, 'pages': 300, 'copies': 6}
            ]
        },
        {
            "name": "пустой диапазон (нет книг в [n1, n2])",
            "input": [
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5}
            ],
            "n1": 2000,
            "n2": 2020,
            "expected": []
        },
        {
            "name": "одна книга в диапазоне",
            "input": [
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine', 'year': 1953, 'pages': 249, 'copies': 9},
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5}
            ],
            "n1": 1953,
            "n2": 1953,
            "expected": [
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine', 'year': 1953, 'pages': 249, 'copies': 9}
            ]
        },
        {
            "name": "сложный случай: перекрывающиеся авторы и года",
            "input": [
                {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'publisher': 'Эксмо', 'year': 1869, 'pages': 1225, 'copies': 2},
                {'author': 'Булгаков М.А.', 'title': 'Мастер и Маргарита', 'publisher': 'Сов. писатель', 'year': 1967, 'pages': 480, 'copies': 5},
                {'author': 'Толстой Л.Н.', 'title': 'Анна Каренина', 'publisher': 'Азбука', 'year': 1877, 'pages': 864, 'copies': 8},
                {'author': 'Булгаков М.А.', 'title': 'Белая гвардия', 'publisher': 'АСТ', 'year': 1925, 'pages': 400, 'copies': 12},
                {'author': 'Достоевский Ф.М.', 'title': 'Преступление и наказание', 'publisher': 'АСТ', 'year': 1866, 'pages': 672, 'copies': 5}
            ],
            "n1": 1860,
            "n2": 1970,
            "expected": [
                {'author': 'Булгаков М.А.', 'title': 'Мастер и Маргарита', 'publisher': 'Сов. писатель', 'year': 1967, 'pages': 480, 'copies': 5},
                {'author': 'Булгаков М.А.', 'title': 'Белая гвардия', 'publisher': 'АСТ', 'year': 1925, 'pages': 400, 'copies': 12},
                {'author': 'Толстой Л.Н.', 'title': 'Анна Каренина', 'publisher': 'Азбука', 'year': 1877, 'pages': 864, 'copies': 8},
                {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'publisher': 'Эксмо', 'year': 1869, 'pages': 1225, 'copies': 2},
                {'author': 'Достоевский Ф.М.', 'title': 'Преступление и наказание', 'publisher': 'АСТ', 'year': 1866, 'pages': 672, 'copies': 5}
            ]
        },
        {
            "name": "границы диапазона включительно",
            "input": [
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Bradbury', 'title': 'Dandelion Wine', 'publisher': 'Ballantine', 'year': 1957, 'pages': 249, 'copies': 9},
                {'author': 'Huxley', 'title': 'Brave New World', 'publisher': 'Chatto', 'year': 1932, 'pages': 311, 'copies': 6},
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine', 'year': 1953, 'pages': 249, 'copies': 9}
            ],
            "n1": 1932,
            "n2": 1957,
            "expected": [
                {'author': 'Bradbury', 'title': 'Dandelion Wine', 'publisher': 'Ballantine', 'year': 1957, 'pages': 249, 'copies': 9},
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine', 'year': 1953, 'pages': 249, 'copies': 9},
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Huxley', 'title': 'Brave New World', 'publisher': 'Chatto', 'year': 1932, 'pages': 311, 'copies': 6}
            ]
        }
    ]

    all_passed = True

    for i, case in enumerate(test_cases, 1):
        input_books = [b.copy() for b in case["input"]]
        result = get_sorted_list_3(input_books, case["n1"], case["n2"])

        if result == case["expected"]:
            print(f"✅ Тест {i} ({case['name']}): OK")
        else:
            print(f"❌ Тест {i} ({case['name']}): FAIL")
            print(f"   Диапазон: [{case['n1']}, {case['n2']}]")
            print(f"   Вход:      {len(case['input'])} книг")

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
                print(f"   Длины списков разные: получено={len(result)}, ожидалось={len(case['expected'])}")

            all_passed = False

    return all_passed


if __name__ == "__main__":
    success = test_get_sorted_list_3()
    if success:
        print("\n🎉 Все тесты get_sorted_list_3 пройдены!")
    else:
        print("\n⚠️ Некоторые тесты провалены.")