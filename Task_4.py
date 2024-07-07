from datetime import datetime

def get_upcoming_birthdays(users):
    birthday_this_year = datetime.strptime(users["birthday"], "%Y.%m.%d").date()
    today = datetime.today().date()
    for user in users:
        difference_days = today - birthday_this_year
        if birthday_this_year < today
            
    return print(difference_days)

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)



# Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)

# Якщо сьогодні 2024.01.22 результатом може бути:
# [
#     {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
#     {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
#]