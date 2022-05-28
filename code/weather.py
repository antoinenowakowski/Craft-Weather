import requests



lat = 48.433982
lon = 0.082475
<<<<<<< HEAD
api_key = 'f49b123dc74107df107f6d559cdd331b'
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt=8&appid={api_key}&units=metric'
r = requests.get(url).json() # get l'url
=======
lang = 'fr'
api_key = ''
>>>>>>> f55ae7762e4efa7726ab47cbe10382a7a45e0f81

def get_temp(j):
    return r['list'][j]['main']['temp']

def get_weather(k):
    return r['list'][int(k)]['weather'][0]['main']

def get_clouds(l):
    return r['list'][int(l)]['weather'][0]['description']

def  get_speed_wind(m):
    return r['list'][int(m)]['wind']['speed']