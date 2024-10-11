from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    week_later = today + timedelta(days=7)
    result = []
    
    for user in users:
        name = user['name']
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        if today <= birthday_this_year <= week_later:
            if birthday_this_year.weekday() == 5:
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year
            
            result.append({
                'name': name,
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })
    
    return result

users = [
    {"name": "Олексій", "birthday": "1990.10.05"},
    {"name": "Марина", "birthday": "1987.10.09"},
    {"name": "Іван", "birthday": "1995.10.03"},
    {"name": "Катерина", "birthday": "1992.10.07"},
    {"name": "Олег", "birthday": "1999.10.02"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)