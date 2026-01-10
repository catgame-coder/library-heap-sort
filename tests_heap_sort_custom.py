from heap_sort_custom import heap_sort_custom

def test_heap_sort_custom(): # Тесты на корректную работу функции heap_sort_custom
    test_cases =   [
        {
            "name": "числа по возрастанию",
            "input": [3, 1, 2],
            "compare": lambda a, b: a < b,
            "expected": [1, 2, 3]
        },
        {
            "name": "пустой список при возрастании",
            "input": [],
            "compare": lambda a, b: a < b,
            "expected": []
        },
        {
            "name": "строки по возрастанию",
            "input": ["z", "a", "m"],
            "compare": lambda a, b: a < b,
            "expected": ["a", "m", "z"]
        },
        {
            "name": "числа по убыванию",
            "input": [4, 6, 5, 7],
            "compare": lambda a, b: a > b,
            "expected": [7, 6, 5, 4]
        },
        {
            "name": "пустой список при убывании",
            "input": [],
            "compare": lambda a, b: a > b,
            "expected": []
        },
        {
            "name": "строки по убыванию",
            "input": ["b", "y", "p"],
            "compare": lambda a, b: a > b,
            "expected": ["y", "p", "b"]
        },
        {
            "name": "одно число",
            "input": [42], 
            "compare": lambda a, b: a < b,
            "expected": [42]
        },
        {
            "name": "одна строка",
            "input": ["q"],
            "compare": lambda a, b: a < b,
            "expected": ["q"]
        },
        {
            "name": " все числа одинаковые",
            "input": [5, 5, 5, 5],
            "compare": lambda a, b: a < b,
            "expected": [5, 5, 5, 5]
        },
        {
            "name": " все строки одинаковые",
            "input": ["za", "za", "za", "za"],
            "compare": lambda a, b: a < b,
            "expected": ["za", "za", "za", "za"]
        },
        {
            "name": "уже отсортированный список чисел",
            "input": [1, 2, 3, 4, 5],
            "compare": lambda a, b: a < b,
            "expected": [1, 2, 3, 4, 5]
        },
        {
            "name": "уже отсортированный список строк",
            "input": ["ba", "bo", "f", "h", "k"],
            "compare": lambda a, b: a < b,
            "expected": ["ba", "bo", "f", "h", "k"]
        },
        {
            "name": "обратно отсортированный список чисел",
            "input": [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            "compare": lambda a, b: a < b,
            "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        },
        {
            "name": "обратно отсортированный список строк",
            "input": ["z","y","x","w","v","u","t","s","r","q","p"],
            "compare": lambda a, b: a < b,
            "expected": ["p","q","r","s","t","u","v","w","x","y","z"]
        },
        {
            "name": "отрицательные числа и ноль",
            "input": [-3, 0, 2, -1, 5],
            "compare": lambda a, b: a < b,
            "expected": [-3, -1, 0, 2, 5]
        },
        {
            "name": "длинный список",
            "input": list(range(1000, 0, -1)),  # [1000, 99, ..., 1]
            "compare": lambda a, b: a < b,
            "expected": list(range(1, 1001))   # [1, 2, ..., 1000]
        },
        {
            "name": "числа с плавающей точкой",
            "input": [3.14, 2.71, -1.5, 0.0], 
            "compare": lambda a, b: a < b, 
            "expected": [-1.5, 0.0, 2.71, 3.14]
        },
        {
            "name": "пустой список и списки со значениями",
            "input": [[3, 8, 11], [], [1, 4]],
            "compare": lambda a, b: a < b,
            "expected": [[], [1, 4], [3, 8, 11]]
        },
        {
            "name": "списки координаты",
            "input": [[3, 2], [1, 4], [2, 1]],
            "compare": lambda a, b: a < b,
            "expected": [[1, 4], [2, 1], [3, 2]]
        },
        {
            "name": "кортежи",
            "input": [(2, 'b'), (1, 'a'), (2, 'a')],
            "compare": lambda a, b: a < b,
            "expected": [(1, 'a'), (2, 'a'), (2, 'b')]
        },
        {
            "name": "булевы значения",
            "input": [True, False, True],
            "compare": lambda a, b: a < b,
            "expected": [False, True, True]
        },
        {
            "name": "словарь книг сортировка по году",
            "input": [
                {"title": "Dracula", "year": 1897},
                {"title": "1984", "year": 1949},
                {"title": "Fahrenheit", "year": 1953}
            ],
            "compare": lambda a, b: a["year"] < b["year"],
            "expected": [
                {"title": "Dracula", "year": 1897},
                {"title": "1984", "year": 1949},
                {"title": "Fahrenheit", "year": 1953}
            ]
        },
        {
        "name": "словарь книг сортировка по названию",
        "input": [
            {"title": "The Picture of Dorian Gray", "year": 1890},
            {"title": "1984", "year": 1949},
            {"title": "Alice's Adventures in Wonderland", "year": 1865},
            {"title": "Имя ветра", "year": 2007},
            {"title": "Большие надежды", "year": 1860}
        ],
        "compare": lambda a, b: a["title"] < b["title"],
        "expected": [
            {"title": "1984", "year": 1949},
            {'title': "Alice's Adventures in Wonderland", 'year': 1865},
            {'title': 'The Picture of Dorian Gray', 'year': 1890},
            {"title": "Большие надежды", "year": 1860},
            {"title": "Имя ветра", "year": 2007}
        ]
        }

] 

    all_passed= True
    for i,case in enumerate(test_cases,1): # Функция enumerate() добавляет счётчик к элементам списка (или любого перебираемого объекта).
        copy=case["input"].copy() # Делаем копию, чтобы не испортить исходные данные
        heap_sort_custom(copy, case["compare"])

        if copy == case["expected"]:
            print(f"✅ Тест {i} ({case['name']}): OK")
        else:
            print (f"❌ Тест {i} ({case['name']}): FAIL")
            print (f"Вход: {case['input']}")
            print (f"Получено: {copy}")
            print (f"Ожидалось: {case['expected']}")
            all_passed= False
    return all_passed


def test_mixed_types_raise_error(): # Тесты на корректную обработку ошибок
    error_test_cases = [
        {
            "name": "число и строка",
            "input": [1, "a", 2]
        },
        {
            "name": "строка и число",
            "input": ["hello", 42]
        },
        {
            "name": "число и None",
            "input": [1, None, 3]
        },
        {
            "name": "список и число",
            "input": [[1, 2], 5]
        },
        {
            "name": "булево и строка",
            "input": [True, "yes"]
        },
        {
            "name": "пустой список с разными типами",
            "input": [[],{}] 
        },
        {
            "name": "только None",
            "input": [None, None, None]
        }
    ]

    all_passed = True

    for i, case in enumerate(error_test_cases, 1):
        arr = case["input"]

        try:
            heap_sort_custom(arr, lambda a, b: a < b)
            print(f"❌ Тест ошибок {i} ({case['name']}): ошибка НЕ возникла")
            all_passed = False
        except ValueError as e:
            if "Нельзя смешивать разные типы данных" in str(e):
                print(f"✅ Тест ошибок {i} ({case['name']}): корректная ошибка")
            else:
                print(f"❌ Тест ошибок {i} ({case['name']}): неверное сообщение: {e}")
                all_passed = False
        except TypeError as e:
            if "not supported between instances" in str(e):
                print(f"✅ Тест ошибок {i} ({case['name']}): корректная ошибка")
            else:
                print(f"❌ Тест ошибок {i} ({case['name']}): неожиданый TypeError: {e}")
        except Exception as e:
            print(f"❌ Тест ошибок {i} ({case['name']}): неожиданное исключение: {type(e).__name__}: {e}")
            all_passed = False

    return all_passed

#Запуск
if __name__ == "__main__":
    # Запускаем обычные тесты
    success = test_heap_sort_custom()

    print()

    # Запускаем тесты на ошибки
    success_error = test_mixed_types_raise_error()

    # Общий результат: всё должно быть True
    all_passed = success and success_error

    if all_passed:
        print("\n🎉 Все тесты пройдены!")
    else:
        print("\n⚠️ Некоторые тесты провалены.")