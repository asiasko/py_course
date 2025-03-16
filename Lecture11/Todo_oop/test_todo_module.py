import pytest
from todo_module import Task, BadPriorityError, BadIdError, BadNameError, TodoList


class TestExceptions:
    def test_bad_priority_error(self):
        """Проверка исключения BadPriorityError."""
        with pytest.raises(BadPriorityError) as exc_info:
            raise BadPriorityError(-1)
        assert str(exc_info.value) == "BadPriorityError: -1 -> Приоритет задачи должен быть больше или равен 0\n"


class TestTodoList:
    """Тесты для класса TodoList."""

    @pytest.fixture
    def todo_list(self):
        """Фикстура для создания объекта TodoList."""
        return TodoList()

    def test_update_task(self, todo_list):
        """Проверка обновления задачи."""
        todo_list.create(1, "smth task", 3)
        todo_list.update(1, task_name="smth task 2", task_prior=5)
        assert todo_list.tasks[1].task_name == "smth task 2"
        assert todo_list.tasks[1].task_prior == 5

    def test_update_task_invalid_name(self, todo_list):
        """Проверка обновления задачи с некорректным именем."""
        todo_list.create(1, "smth task", 3)
        with pytest.raises(BadNameError):
            todo_list.update(1, task_name="Купить")

    def test_update_task_invalid_priority(self, todo_list):
        """Проверка обновления задачи с отрицательным приоритетом."""
        todo_list.create(1, "smth task", 3)
        with pytest.raises(BadPriorityError):
            todo_list.update(1, task_prior=-1)

    def test_update_nonexistent_task(self, todo_list):
        """Проверка обновления несуществующей задачи."""
        todo_list.update(99, task_name="Nonexistent Task")
        assert 99 not in todo_list.tasks

    def test_delete_task(self, todo_list):
        """Проверка удаления задачи."""
        todo_list.create(1, "smth task", 3)
        todo_list.delete(1)
        assert 1 not in todo_list.tasks

    def test_delete_nonexistent_task(self, todo_list):
        """Проверка удаления несуществующей задачи."""
        todo_list.delete(99)
        assert 99 not in todo_list.tasks

    def test_read_all_tasks(self, todo_list):
        """Проверка получения списка всех задач."""
        todo_list.create(1, "Something task 1", 5)
        todo_list.create(2, "Something task 2", 3)
        tasks = todo_list.read_all()
        assert len(tasks) == 2
        assert (1, "Something task 1", 5) in tasks
        assert (2, "Something task 2", 3) in tasks

    def test_find_task(self, todo_list):
        """Проверка поиска задачи."""
        todo_list.create(1, "Something task", 5)
        task = todo_list.find(1)
        assert task is not None
        assert task.task_id == 1
        assert task.task_name == "Something task"
        assert task.task_prior == 5

    def test_find_nonexistent_task(self, todo_list):
        """Проверка поиска несуществующей задачи."""
        task = todo_list.find(99)
        assert task is None