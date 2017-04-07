import requests
import math
import time

def k2f(t):
    return (t*9/5.0)-459.67

def k2c(t):
    return t-273.15

zip_code = input('What ZIP code?: ')
payload = {'appid': '3a8a1438c7631c88e1845e8268e7c0f9' , 'zip' : zip_code}

r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
tday = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=payload)

data = r.json()
day_data = tday.json()

t = data['main']['temp']

print(data['name'])

decision = input('Would you like the temperature in Farenheit (f) or Celsius (c): ')
if decision == 'c':
    print(math.floor(k2c(t)))
elif decision == 'f':
    print(math.floor(k2f(t)))
else:
    print('User error, replace user')

for x in day_data['list']:
    t = time.strftime('%b-%d %H:%M', time.localtime(x['dt']))
    w = x['weather']
    for q in w:
        print(q['description'])
        print(t)

print(t)

# print(w[0]['description'])

if data['main']['temp'] >= 75:
    print('Lovely day for a Corona!')
elif data['main']['temp'] <= 50:
    print('Lovely day for a Guiness!')



# print(data['main']['temp'])



# print('What ZIP?')
# zip_code = input(int(''))
#
# print('Joke #{}: '.format(data['value']['id']))
# print('{}'.format(data['value']['joke']))


# 3a8a1438c7631c88e1845e8268e7c0f9
