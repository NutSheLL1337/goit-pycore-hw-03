import random


def get_numbers_ticket(min, max, quantity):
    # Генерує набір унікальних випадкових чисел у межах заданих параметрів для лотереї
    try:
        unique_numbers = random.randint(min, max)
        ticket_numbers = random.choices(unique_numbers, k = quantity)
        return print(ticket_numbers)
    except Exception as e:
        print(f"An error occured: {e}")
    

lottery_numbers = get_numbers_ticket(1, 49, 5)
# print("Ваші лотерейні числа:", lottery_numbers)