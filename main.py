from datetime import datetime


def get_days_from_today(date: str):
    # Функція отримує дату та перетворює її у об'єкт datetime, розраховує поточну дату та повертає різницю у днях
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        days_diff = today - date
        return days_diff    
    except Exception as e:
        print(f"An error occured: {e}") 
   
         
print(get_days_from_today("2024-06-06"))

    



