import re


def normalize_phone(phone_number: str):
    # Нормалізує телефонні номери до стандартного формату. 
    # Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі.
    try:
        first_pattern = r"([\++])(\d+[38])"
        match = re.search(first_pattern, phone_number)
        if match:
            print("Знайдено:", match.group(1), match.group(2))
        else:
            print("Не знайдено plus або +38.")
            phone_number += "+38"
        return phone_number    
        sub_pattern = r"\s"
        replacement = "_"
        match_digits = re.sub(sub_pattern, replacement, phone_number)    
    except Exception as e:
        print(f"An error occured: {e}")

print(normalize_phone("0999124567"))
    