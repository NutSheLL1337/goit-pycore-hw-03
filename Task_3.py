import re


def normalize_phone(phone_number: str):
    # Нормалізує телефонні номери до стандартного формату. 
    # Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі.
    replacement = "380"
    start_pattern = r"[+]"
    formatted_name = re.sub(start_pattern, replacement, phone_number)
    # match = re.search(pattern, phone_number)
    return print(formatted_name)


normalize_phone()
    