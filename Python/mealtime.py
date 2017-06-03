"""
Write a function that returns the meal for any given hour of the day.
Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM
>>> meal(7)
'Breakfast time.'
>>> meal(13)
'Lunch time.'
>>> meal(20)
'Dinner time.'
>>> meal(21)
'No meal scheduled at this time.'
>>> meal(0)
'No meal scheduled at this time.'
>>> meal(3)
'Hammer time.'
>>> meal(9999)
'Not a valid time.'
"""

def meal_time(time):
    breakfast = range(700, 900)
    lunch = range(1200, 1400)
    dinner = range(1900, 2100)
    hammer = range(2200, 400)
    if time in breakfast:
        print ('Its breakfast time!')
    elif time in  lunch:
        print ('Its lunch time!')
    elif time in dinner:
        print ('Dinner time!')
    elif time in hammer:
        print ('Its HAMMER TIME')
    else:
        print ('No meal scheduled at this time!')

user_time = int(input('Military Time: '))
meal_time(user_time)
