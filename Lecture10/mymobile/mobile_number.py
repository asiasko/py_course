class MobilePhone:
    def __init__(self, number):
        self.number = number
        self.switch = False
    def turn_on(self):
        self.switch = True
        return f"\nТелефон включен"
    def turn_off(self):
        self.switch = False
        return f"\nТелефон выключен"
    def call(self, cally):
        if self.switch:
            return f"\nЗвонок на {cally} ...."
        else:
            return f"\nТелефон {self.number} выключен, нельзя позвонить"