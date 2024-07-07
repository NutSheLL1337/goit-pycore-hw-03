import re


def normalize_phone(phone_number: str):
    # Нормалізує телефонні номери до стандартного формату. 
    # Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі.
    try:
         # Видаляємо всі символи, крім цифр та '+'
        normalized_number = re.sub(r'[^\d+]', '', phone_number)
         # Якщо номер не починається з '+', додаємо '+38'
        if not re.match(r'^\+', normalized_number):
            if re.match(r'^380', normalized_number):
                normalized_number = '+' + normalized_number
            else:
                normalized_number = '+38' + normalized_number
         # Якщо номер починається з '+', але не має '38' після '+'        
        elif not re.match(r'^\+38', normalized_number):
            normalized_number = '+38' + normalized_number[1:]  
        return normalized_number        
    except Exception as e:
        print(f"An error occured: {e}")

print(normalize_phone("999124567"))
    