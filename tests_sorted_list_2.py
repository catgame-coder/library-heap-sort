from sorted_list_2 import get_sorted_list_2
# Название (по возрастанию) + издательство (по убыванию)
def test_get_sorted_list_2():
    test_cases = [
        {
            "name": "базовая сортировка по названию",
            "input": [
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'Secker', 'year': 1945, 'pages': 112, 'copies': 8},
                {'author': 'Orwell', 'title': 'Homage to Catalonia', 'publisher': 'Secker', 'year': 1938, 'pages': 300, 'copies': 6}
            ],
            "author": "Orwell",
            "expected": [
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5},
                {'author': 'Orwell', 'title': 'Animal Farm', 'publisher': 'Secker', 'year': 1945, 'pages': 112, 'copies': 8},
                {'author': 'Orwell', 'title': 'Homage to Catalonia', 'publisher': 'Secker', 'year': 1938, 'pages': 300, 'copies': 6}
            ]
        },
        {
            "name": "одинаковые названия — сортировка по издательству (убывание)",
            "input": [
                {'author': 'King', 'title': 'It', 'publisher': 'Viking', 'year': 1986, 'pages': 1100, 'copies': 10},
                {'author': 'King', 'title': 'It', 'publisher': 'Scribner', 'year': 1986, 'pages': 1100, 'copies': 7},
                {'author': 'King', 'title': 'It', 'publisher': 'Hodder', 'year': 1986, 'pages': 1100, 'copies': 5}
            ],
            "author": "King",
            "expected": [
                {'author': 'King', 'title': 'It', 'publisher': 'Viking', 'year': 1986, 'pages': 1100, 'copies': 10},
                {'author': 'King', 'title': 'It', 'publisher': 'Scribner', 'year': 1986, 'pages': 1100, 'copies': 7},
                {'author': 'King', 'title': 'It', 'publisher': 'Hodder', 'year': 1986, 'pages': 1100, 'copies': 5}
            ]
        },
        {
            "name": "автор не найден",
            "input": [
                {'author': 'Orwell', 'title': '1984', 'publisher': 'Secker', 'year': 1949, 'pages': 328, 'copies': 5}
            ],
            "author": "Tolkien",
            "expected": []
        },
        {
            "name": "одна книга",
            "input": [
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine', 'year': 1953, 'pages': 249, 'copies': 9}
            ],
            "author": "Bradbury",
            "expected": [
                {'author': 'Bradbury', 'title': 'Fahrenheit 451', 'publisher': 'Ballantine', 'year': 1953, 'pages': 249, 'copies': 9}
            ]
        },
        {
            "name": "сложный случай: перекрывающиеся названия и издательства",
            "input": [
                {'author': 'Dostoevsky', 'title': 'The Idiot', 'publisher': 'AICo', 'year': 1869, 'pages': 640, 'copies': 3},
                {'author': 'Dostoevsky', 'title': 'Crime and Punishment', 'publisher': 'Penguin', 'year': 1866, 'pages': 672, 'copies': 5},
                {'author': 'Dostoevsky', 'title': 'The Idiot', 'publisher': 'Vintage', 'year': 1869, 'pages': 640, 'copies': 4},
                {'author': 'Dostoevsky', 'title': 'The Idiot', 'publisher': 'Oxford', 'year': 1869, 'pages': 640, 'copies': 2}
            ],
            "author": "Dostoevsky",
            "expected": [
                {'author': 'Dostoevsky', 'title': 'The Idiot', 'publisher': 'Vintage', 'year': 1869, 'pages': 640, 'copies': 4},
                {'author': 'Dostoevsky', 'title': 'Crime and Punishment', 'publisher': 'Penguin', 'year': 1866, 'pages': 672, 'copies': 5},
                {'author': 'Dostoevsky', 'title': 'The Idiot', 'publisher': 'Oxford', 'year': 1869, 'pages': 640, 'copies': 2},
                {'author': 'Dostoevsky', 'title': 'The Idiot', 'publisher': 'AICo', 'year': 1869, 'pages': 640, 'copies': 3}
            ]
        }
    ]

    all_passed = True

    for i, case in enumerate(test_cases, 1):
        input_books = [b.copy() for b in case["input"]]
        result = get_sorted_list_2(input_books, case["author"])

        if result == case["expected"]:
            print(f"✅ Тест {i} ({case['name']}): OK")
        else:
            print(f"❌ Тест {i} ({case['name']}): FAIL")
            print(f"   Автор:     {case['author']}")
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
    success = test_get_sorted_list_2()
    if success:
        print("\n🎉 Все тесты get_sorted_list_2 пройдены!")
    else:
        print("\n⚠️ Некоторые тесты провалены.")