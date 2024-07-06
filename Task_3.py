import re


def normalize_phone(phone_number: str):
    # Нормалізує телефонні номери до стандартного формату. 
    # Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі.
    normalized_phone = re.search('\+', phone_number)
    