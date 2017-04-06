import requests
import math

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
# print(day_data['list']['weather'])

decision = input('Would you like the temperature in Farenheit (f) or Celsius (c): ')
if decision == 'c':
    print(math.floor(k2c(t)))
elif decision == 'f':
    print(math.floor(k2f(t)))


# print(data['main']['temp'])



# print('What ZIP?')
# zip_code = input(int(''))
#
# print('Joke #{}: '.format(data['value']['id']))
# print('{}'.format(data['value']['joke']))


# 3a8a1438c7631c88e1845e8268e7c0f9
