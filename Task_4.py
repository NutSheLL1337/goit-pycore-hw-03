from datetime import datetime


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    weekends = datetime.today().weekday() # if weekday 6 or 5 we transfer to 0
    
    # for user in users:
    #     difference_days = today - birthday_this_year
    #     name = 
    #     congratulation_date = 
    #    # if birthday_this_year < today
    return print(today, weekends)
    #return users[{"name": ""}, {"congratulation_date": ""}]


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