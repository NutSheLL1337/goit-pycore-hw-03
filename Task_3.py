import re


def normalize_phone(phone_number: str):
    # Нормалізує телефонні номери до стандартного формату. 
    # Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі.
    try:
        if first_pattern:
            first_pattern = r"([+])\d"
            replacement_first = ""
            formatted_phone = re.sub(first_pattern, replacement_first, phone_number)
        elif second_pattern:
            second_pattern = r"[+]"
            replacement = "380"
            formatted_plus = re.sub(first_pattern, replacement, phone_number)
        elif third_pattern:
            third_pattern = r"\w[38]"
            code_replacement = '+38'
            formatted_code = re.sub(second_pattern, code_replacement, phone_number)
    except Exception as e:
        print(f"An error occured: {e}")
        



    # match = re.search(pattern, phone_number)
    return print(formatted_name)

    


normalize_phone("+999124567")
    