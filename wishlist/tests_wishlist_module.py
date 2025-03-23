import pytest
from wishlist_module import Wishlist 

class TestWishlist:
    @pytest.fixture
    def wishlist(self):
        """Фикстура для создания экземпляра WishlistManager."""
        wishlist = Wishlist()
        # Добавляем тестовые данные
        wishlist.add_wish(1, "Купить велосипед", "https://example.com/bike", 1500, "Спорт")
        wishlist.add_wish(2, "Путешествие в Кению", "https://example.com/japan-trip", 3000, "Путешествия")
        wishlist.add_wish(3, "Ноутбук", "https://example.com/laptop", 4000, "Электроника")
        return wishlist

    def test_add_wish(self, wishlist):
        """Тест добавления желания."""
        # Проверяем, что желание добавлено
        assert len(wishlist.wishlist) == 3

        # Проверяем, что нельзя добавить желание с существующим ID
        with pytest.raises(ValueError):
            wishlist.add_wish(1, "Тестовое желание 1", "https://example.com/test", 1000, "Тест")

        # Проверяем, что нельзя добавить желание с пустой категорией
        with pytest.raises(ValueError):
            wishlist.add_wish(4, "Тестовое желание 2", "https://example.com/test2", 1000, "")

    def test_find_wish_by_id(self, wishlist):
        """Тест поиска желания по ID."""
        # Поиск существующего желания
        result = wishlist.find_wish_by_id(1)
        assert "Купить велосипед" in result
        assert "1500" in result

        # Поиск несуществующего желания
        result = wishlist.find_wish_by_id(999)
        assert result is None

    def test_find_wish_by_name(self, wishlist, capsys):
        """Тест поиска желания по названию."""
        # Поиск существующего желания
        wishlist.find_wish_by_name("велосипед")
        captured = capsys.readouterr()
        assert "Купить велосипед" in captured.out

        # Поиск несуществующего желания
        wishlist.find_wish_by_name("несуществующее")
        captured = capsys.readouterr()
        assert "не найдены" in captured.out

    def test_find_wishes_by_category(self, wishlist, capsys):
        """Тест поиска желаний по категории."""
        # Поиск существующей категории
        wishlist.find_wishes_by_category("Спорт")
        captured = capsys.readouterr()
        assert "Купить велосипед" in captured.out

        # Поиск несуществующей категории
        wishlist.find_wishes_by_category("Несуществующая")
        captured = capsys.readouterr()
        assert "не найдены" in captured.out

    def test_change_wish(self, wishlist):
        """Тест изменения желания."""
        # Изменяем существующее желание
        wishlist.change_wish(1, "Новый велосипед", "https://example.com/new-bike", 2000, "Спорт")
        result = wishlist.find_wish_by_id(1)
        assert "Новый велосипед" in result
        assert "2000" in result

        # Попытка изменить несуществующее желание
        wishlist.change_wish(999, "Тест", "https://example.com/test", 1000, "Тест")
        result = wishlist.find_wish_by_id(999)
        assert result is None

    def test_delete_wish(self, wishlist):
        """Тест удаления желания."""
        # Удаляем существующее желание
        wishlist.delete_wish(1)
        assert len(wishlist.wishlist) == 2

        # Попытка удалить несуществующее желание
        wishlist.delete_wish(999)
        assert len(wishlist.wishlist) == 2

    def test_show_all_wishes(self, wishlist, capsys):
        """Тест вывода всех желаний."""
        wishlist.show_all_wishes()
        captured = capsys.readouterr()
        assert "Купить велосипед" in captured.out
        assert "Путешествие в Кению" in captured.out
        assert "Ноутбук" in captured.out
