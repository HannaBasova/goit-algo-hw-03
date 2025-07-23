from datetime import datetime
'''
Function which calculates the number of days between a given date and the current date

Input:
:param date: str
Output:
:return: integer
'''
def get_days_from_today(date:str)->int:
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d') #Convert a string to a date object
        today = datetime.today() #current date
        days_ahead = (date_obj.date() - today.date()).days
        return days_ahead
    except ValueError:
        print("Please enter a correct date format: 'YYYY-MM-DD' ")

print(get_days_from_today('2025-07-23'))