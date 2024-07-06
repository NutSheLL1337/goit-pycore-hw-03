import random


def get_numbers_ticket(min, max, quantity):
    # Генерує набір унікальних випадкових чисел у межах заданих параметрів для лотереї
    try:
        if (min < 1 or max > 1000):
            print("You've entered number out of range, minimum value is 1, and maximum is 1000")
        else:
            random_numb = random.randint(min, max)
            unique_numbers = random.sample(range(random_numb), quantity)
            return print(unique_numbers)
    except Exception as e:
        print(f"An error occured: {e}")
    

get_numbers_ticket(1, 1001, 5)
# print("Ваші лотерейні числа:", lottery_numbers)