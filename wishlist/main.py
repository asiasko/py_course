from wishlist_module import Wishlist 


def menu():
    """
    Функция для отображения меню с доступными действиями пользователя.
    """
    print("""
         1 - Добавить желание
         2 - Просмотреть все желания
         3 - Найти желание по ID
         4 - Найти желание по названию
         5 - Найти желания по категории
         6 - Изменить желание по ID
         7 - Удалить желание по ID
         -1 - Выйти из программы""")


def main():
    """
    Основная функция программы. Обрабатывает ввод пользователя, вызывает
    соответствующие методы для управления списком желаний, отображает меню и
    выполняет проверки на корректность ввода.
    """
    print("Привет! Это твой список желаний!")
    wishlist = Wishlist()  # Создаем объект менеджера желаний
    menu()

    while True:
        try:
            oper = int(input("Выбери нужную функцию из меню: "))
            if oper < -1 or oper > 7:  # Проверка на корректность ввода
                print("Неверный выбор! Пожалуйста, выбери число от -1 до 7.")
                continue
            if oper == 0:  # Обработка случая, если введен 0
                print("Ошибка! Пункт с номером 0 отсутствует в меню.")
                continue
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите число.")
            continue

        if oper == -1:
            print("До свидания!")
            break  # Завершаем программу

        elif oper == 1:
            # Проверка ID
            while True:
                try:
                    wish_id = int(input("Введите ID для желания: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            # Проверка названия
            while True:
                name = input("Введите название желания: ").strip()
                if len(name) >= 3:
                    break
                print("Ошибка! Название желания должно быть не менее 3 символов.")

            # Проверка ссылки
            link = input("Введите ссылку на желание: ").strip()

            # Проверка стоимости
            while True:
                try:
                    cost = float(input("Введите стоимость желания: "))
                    if cost >= 0:
                        break
                    print("Ошибка! Стоимость должна быть положительным числом.")
                except ValueError:
                    print("Ошибка ввода стоимости! Пожалуйста, введите число.")

            # Проверка категории
            while True:
                category = input("Введите категорию желания: ").strip()
                if category:
                    break
                print("Ошибка! Категория не может быть пустой.")

            try:
                wishlist.add_wish(wish_id, name, link, cost, category)  # Добавление желания
                print("Желание успешно добавлено!")
            except Exception as e:
                print(e)

        elif oper == 2:
            wishlist.show_all_wishes()  # Показать все желания

        elif oper == 3:
            # Проверка ID
            while True:
                try:
                    wish_id = int(input("Введите ID для поиска желания: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            result = wishlist.find_wish_by_id(wish_id)  # Поиск желания по ID
            if result:  # Если желание найдено, вывести его
                print(result)

        elif oper == 4:
            search_name = input("Введите название для поиска: ").strip()
            wishlist.find_wish_by_name(search_name)  # Поиск желания по названию

        elif oper == 5:
            category = input("Введите категорию для поиска: ").strip()
            wishlist.find_wishes_by_category(category)  # Поиск желаний по категории

        elif oper == 6:
            # Проверка ID для изменения желания
            while True:
                try:
                    wish_id = int(input("Введите ID для изменения желания: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            # Проверка нового названия
            while True:
                new_name = input("Введите новое название желания: ").strip()
                if len(new_name) >= 3:
                    break
                print("Ошибка! Название желания должно быть не менее 3 символов.")

            # Проверка новой ссылки
            new_link = input("Введите новую ссылку на желание: ").strip()

            # Проверка новой стоимости
            while True:
                try:
                    new_cost = float(input("Введите новую стоимость желания: "))
                    if new_cost >= 0:
                        break
                    print("Ошибка! Стоимость должна быть положительным числом.")
                except ValueError:
                    print("Ошибка ввода стоимости! Пожалуйста, введите число.")

            # Проверка новой категории
            while True:
                new_category = input("Введите новую категорию желания: ").strip()
                if new_category:
                    break
                print("Ошибка! Категория не может быть пустой.")

            # Попытка изменить желание
            wishlist.change_wish(wish_id, new_name, new_link, new_cost, new_category)
            print("Желание успешно изменено!")

        elif oper == 7:
            # Проверка ID для удаления желания
            while True:
                try:
                    wish_id = int(input("Введите ID для удаления желания: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            wishlist.delete_wish(wish_id)  # Удаление желания
            print("Желание успешно удалено!")

        menu()  # Выводим меню после выполнения действия


if __name__ == "__main__":
    main()  # Запуск основной функции
    