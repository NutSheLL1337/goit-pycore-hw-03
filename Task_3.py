import re


def normalize_phone(phone_number: str):
    # Нормалізує телефонні номери до стандартного формату. 
    # Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі.
    first_pattern = r"[+]"
    second_pattern = r""

    if first_pattern:
        pattern_all = r"([+])\d"
        replacement_all = ""
    elif second_pattern:
        replacement = "380"
        formatted_name = re.sub(first_pattern, replacement, phone_number)
    elif third_pattern:
        code_replacement = '+38'
        formatted_code = re.sub(second_pattern, code_replacement, phone_number)
    # match = re.search(pattern, phone_number)
    return print(formatted_name)


normalize_phone("+999124567")
    