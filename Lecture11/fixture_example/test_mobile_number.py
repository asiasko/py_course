from mobile_number import MobilePhone
import pytest

@pytest.fixture
def mobile_phone():
    """Фикстура для создания экземпляра MobilePhone."""
    return MobilePhone("123-456-789")

@pytest.fixture
def mobile_phone_turned_on(mobile_phone):
    """Фикстура для создания включенного телефона."""
    mobile_phone.turn_on()
    return mobile_phone

@pytest.fixture
def mobile_phone_turned_off(mobile_phone):
    """Фикстура для создания выключенного телефона."""
    mobile_phone.turn_off()
    return mobile_phone

def test_turn_on(mobile_phone):
    """Проверка включения телефона."""
    result = mobile_phone.turn_on()
    assert result == "\nТелефон включен"
    assert mobile_phone.switch is True

def test_turn_off(mobile_phone):
    """Проверка выключения телефона."""
    mobile_phone.turn_on()  # Включаем телефон перед выключением
    result = mobile_phone.turn_off()
    assert result == "\nТелефон выключен"
    assert mobile_phone.switch is False

def test_call_when_phone_is_on(mobile_phone_turned_on):
    """Проверка звонка, когда телефон включен."""
    result = mobile_phone_turned_on.call("987-654-321")
    assert result == "\nЗвонок на 987-654-321 ...."

def test_call_when_phone_is_off(mobile_phone_turned_off):
    """Проверка звонка, когда телефон выключен."""
    result = mobile_phone_turned_off.call("987-654-321")
    assert result == "\nТелефон 123-456-789 выключен, нельзя позвонить"