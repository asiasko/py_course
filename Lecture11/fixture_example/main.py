from mobile_number import MobilePhone


def menu():
    """Показывает меню и возвращает выбранный пункт."""
    menu = """
    ====================================================================================================
    |                                       MOBILE NUMBER PROJECT                                        |
    ====================================================================================================
    |                                       1 - Включить телефон                                       |
    |                                       2 - Выключить телефон                                      |
    |                                       3 - Позвонить                                              |
    |                                       4 - Выход                                                  |
    ====================================================================================================
    """
    print(menu)


def main():
    """Основная логика."""
    my_phone_number = MobilePhone("123-456-789")
    while True:
        menu()
        choice = input("Выберите команду: ")
        if choice == "1":
            print(my_phone_number.turn_on())
        elif choice == "2":
            print(my_phone_number.turn_off())
        elif choice == "3":
            print(my_phone_number.call("123-456-789"))
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверная команда.")


if __name__ == "__main__":
    main()