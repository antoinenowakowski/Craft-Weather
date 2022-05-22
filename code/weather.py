import requests
import json
from datetime import *

lat = 48.433982
lon = 0.082475
lang = 'fr'
api_key = 'f49b123dc74107df107f6d559cdd331b'

url =f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt=8&lang={lang}&appid={api_key}&units=metric'

r = requests.get(url).json() # get l'url
print(r)
today = date.today()
get_time = r['list'][0]['dt_txt']

now = datetime.now()
current_time = now.strftime("%H")

def when(x):
    if get_time == f'{today} 0{x}:00:00':
        print("ok")
    elif get_time == f'{today} {x}:00:00':
        print("ok")
    else:
        print('nop')
