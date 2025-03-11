from mobile_number import MobilePhone


def test_turn_on():
    my_phone_number = MobilePhone("123-456-789")
    assert my_phone_number.turn_on() == "\nТелефон включен"

def test_turn_off():
    my_phone_number = MobilePhone("123-456-789")
    my_phone_number.turn_on()
    assert my_phone_number.turn_off() == "\nТелефон выключен"

def test_call_when_on():
    my_phone_number = MobilePhone("123-456-789")
    my_phone_number.turn_on()
    assert my_phone_number.call("123-456-789") == "\nЗвонок на 123-456-789 ...."

def test_call_when_off():
    my_phone_number = MobilePhone("123-456-789")
    assert my_phone_number.call("123-456-789") == "\nТелефон 123-456-789 выключен, нельзя позвонить"
