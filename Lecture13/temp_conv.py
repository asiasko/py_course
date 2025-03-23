import xml.etree.ElementTree as ET

class ForecastXmlParser:
    @staticmethod
    def convert_celsius_to_fahrenheit(temperature_in_celsius):
        """Конвертация температуры из Цельсия в Фаренгейт"""
        return 9.0 / 5.0 * temperature_in_celsius + 32

    def parse(self, file):
        """Метод для парсинга данных и преобразования"""
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            temperature_in_celsius = int(child.find("temperature_in_celsius").text)
            temperature_in_fahrenheit = round(self.convert_celsius_to_fahrenheit(temperature_in_celsius), 1)
            print(f"{child.find('day').text}: {temperature_in_celsius} ℃, convert: {temperature_in_fahrenheit} ℉")

# Запуск.
parser = ForecastXmlParser()
parser.parse("forecast.xml")