from read_books import read_books,print_books
from sorted_list_1 import get_sorted_list_1
from sorted_list_2 import get_sorted_list_2, get_all_authors
from sorted_list_3 import get_sorted_list_3, get_year_range


def main_menu():
    books = read_books('books.txt')
    print("Здравствуйте! Вас приветствует программа «Библиотека»\n")

    while True:
        print("\nВы находитесь в главном меню:")
        print("1. Полный список всех книг")
        print("2. Список книг определённого автора")
        print("3. Список всех книг, выпущенных в период с N1 до N2 года")
        print("0. Выход\n")
        print('Обратите внимание - информация выводится в формате: автор; название; издательство; год выпуска; количество страниц; количество экземпляров')
        choice = input("\nВведите номер пункта: ").strip()

        if choice == '1':
            menu_report_1(books)
        elif choice == '2':
            menu_report_2(books)
        elif choice == '3':
            menu_report_3(books)
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("❌ Неверный ввод. Введите 0, 1, 2 или 3.")


def menu_report_1(books):
    print("\n--- 1. Полный список всех книг ---")
    sorted_books = get_sorted_list_1(books)
    print_books(sorted_books)
    input("\nНажмите Enter, чтобы вернуться в главное меню...")


def menu_report_2(books):
    print("\n--- 2. Список книг определённого автора ---")
    authors = get_all_authors(books)

    while True:
        print(f"\nСписок всех авторов ({len(authors)}):")
        for i, author in enumerate(authors, 1):
            print(f"{i}. {author}")
        print("Для возврата в главное меню введите 0")

        user_input = input("\nВведите номер или фамилию автора: ").strip()

        if user_input == '0':
            return

        # По номеру
        if user_input.isdigit():
            idx = int(user_input) - 1
            if 0 <= idx < len(authors):
                selected_author = authors[idx]
            else:
                print("❌ Неверный номер.")
                continue
        else:
            # По фамилии (без инициалов)
            found = None
            for author in authors:
                if user_input.lower() in author.split()[0].lower():
                    found = author
                    break
            if found is None:
                print("❌ Автор не найден.")
                continue
            selected_author = found

        # Вывод книг
        result = get_sorted_list_2(books, selected_author)
        if not result:
            print(f"⚠️ У автора {selected_author} нет книг.")
        else:
            print(f"\nСписок всех книг автора {selected_author}:")
            print_books(result)

        # Подменю
        while True:
            choice = input("\nДля возврата к списку авторов введите 01. Для возврата в главное меню — 0: ").strip()
            if choice == '01':
                break
            elif choice == '0':
                return
            else:
                print("❌ Введите 01 или 0.")


def menu_report_3(books):
    print("\n--- 3. Список книг в периоде с N1 по N2 ---")
    
    min_year, max_year = get_year_range(books)
    print(f"Доступные годы: с {min_year} по {max_year}")

    while True:
        try:
            n1 = int(input("Введите N1:"))
            n2 = int(input("Введите N2:"))
            if n1 > n2:
                print("❌ N1 не может быть больше N2.")
                continue
            if n1 < min_year or n2 > max_year:
                print(f"❌ Годы должны быть в диапазоне от {min_year} до {max_year}.")
                continue
            break
        except ValueError:
            print("❌ Введите целые числа.")

    result = get_sorted_list_3(books, n1, n2)
    if not result:
        print(f"\n⚠️ Нет книг в периоде с {n1} по {n2} год.")
    else:
        print(f"\nНайдено {len(result)} книг:")
        print_books(result)

    input("\nНажмите Enter, чтобы вернуться в главное меню...")