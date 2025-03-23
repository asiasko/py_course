class Wishlist:
    """Класс для управления списком желаний с категориями."""

    def __init__(self):
        self.wishlist = {}

    def add_wish(self, wish_id, name, link, cost, category):
        """Добавление желания с проверкой длины строк и уникальности ID."""
        if wish_id in self.wishlist:
            raise ValueError("Желание с таким ID уже существует!")

        # Проверка на минимальную длину названия
        if len(name) < 3:
            raise ValueError("Название желания должно быть длиной не менее 3 символов!")

        # Проверка, что стоимость является числом и не отрицательной
        if not isinstance(cost, (int, float)) or cost < 0:
            raise ValueError("Стоимость должна быть положительным числом!")

        # Проверка, что категория не пустая
        if not category:
            raise ValueError("Категория не может быть пустой!")

        self.wishlist[wish_id] = (name, link, cost, category)

    def find_wish_by_id(self, wish_id):
        """Поиск желания по ID."""
        if wish_id in self.wishlist:
            name, link, cost, category = self.wishlist[wish_id]
            return f"Название: {name}, Ссылка: {link}, Стоимость: {cost} руб., Категория: {category}"
        else:
            print("Желание с таким ID не найдено!")
            return None

    def find_wish_by_name(self, search_name):
        """Поиск желания по названию."""
        found_wishes = []
        for wish_id, (name, link, cost, category) in self.wishlist.items():
            if search_name.lower() in name.lower():
                found_wishes.append((wish_id, name, link, cost, category))

        if found_wishes:
            print(f"Найдены желания по запросу '{search_name}':")
            for wish in found_wishes:
                print(f"ID: {wish[0]}, Название: {wish[1]}, Ссылка: {wish[2]}, Стоимость: {wish[3]} руб., Категория: {wish[4]}")
        else:
            print(f"Желания по запросу '{search_name}' не найдены.")

    def find_wishes_by_category(self, category):
        """Поиск желаний по категории."""
        found_wishes = []
        for wish_id, (name, link, cost, cat) in self.wishlist.items():
            if cat.lower() == category.lower():
                found_wishes.append((wish_id, name, link, cost, cat))

        if found_wishes:
            print(f"Найдены желания в категории '{category}':")
            for wish in found_wishes:
                print(f"ID: {wish[0]}, Название: {wish[1]}, Ссылка: {wish[2]}, Стоимость: {wish[3]} руб., Категория: {wish[4]}")
        else:
            print(f"Желания в категории '{category}' не найдены.")

    def change_wish(self, wish_id, new_name, new_link, new_cost, new_category):
        """Изменение желания."""
        if wish_id in self.wishlist:
            # Проверка, что новая стоимость является числом и не отрицательной
            if not isinstance(new_cost, (int, float)) or new_cost < 0:
                raise ValueError("Стоимость должна быть положительным числом!")
            self.wishlist[wish_id] = (new_name, new_link, new_cost, new_category)
            print(f"Желание с ID {wish_id} успешно изменено.")
        else:
            print("ID не найден!")

    def delete_wish(self, wish_id):
        """Удаление желания по ID."""
        if wish_id in self.wishlist:
            del self.wishlist[wish_id]
            print(f"Желание с ID {wish_id} было удалено.")
        else:
            print("ID не найден!")

    def show_all_wishes(self):
        """Показать все желания."""
        if self.wishlist:
            total_cost = 0  # Общая стоимость всех желаний
            for wish_id, (name, link, cost, category) in self.wishlist.items():
                print(f"ID: {wish_id}, Название: {name}, Ссылка: {link}, Стоимость: {cost} руб., Категория: {category}")
                total_cost += cost
            print(f"Общая стоимость всех желаний: {total_cost} руб.")
        else:
            print("Список желаний пуст.")
