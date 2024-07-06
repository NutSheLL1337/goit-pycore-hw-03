import random


def get_numbers_ticket(min, max, quantity):
    # Генерує набір унікальних випадкових чисел у межах заданих параметрів для лотереї
    try:
        random_numb = random.randint(min, max)
        unique_numbers = random.sample(range(random_numb), quantity)
        if min < 1 and max > 1000:
            print("You've entered number out of range, min is 1, and maximum is 1000")
        else:
            return print(unique_numbers)
    except Exception as e:
        print(f"An error occured: {e}")
    

get_numbers_ticket(1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)