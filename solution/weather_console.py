
from pprint import pprint
import requests, json, codecs, random

API_KEY = '&APPID=5c55042b76165ad5321007003915fc66'
URL = 'http://api.openweathermap.org/data/2.5/'
city_dict = {}
city_list = []
random_city_list = []

result_list = []

def load_city_list():
    city_data = json.load(codecs.open('city.list.json', 'r', 'utf-8'))
    for eachCity in city_data:
        city_dict[eachCity['id']] = eachCity['name']
        city_list.append(eachCity['id'])

def get_weather_for_city(city):
    print (city_dict[city])
    base_request_url = 'weather?q=' + city_dict[city] + '&units=metric'
    response = requests.get(URL+base_request_url+API_KEY)
    return response.json()

def build_random_city_list(count):
    for _ in range(count):
        random_number = random.randrange(0, len(city_list))
        random_city_list.append(city_list[random_number])

load_city_list()
build_random_city_list(5)
for eachCity in random_city_list:
    cityData = get_weather_for_city(eachCity)
    print ("Град: %s" %cityData['name'])
    print ("Tемпература в момента: %s" %cityData['main']['temp'])
    print ("Град: %s" %cityData['name'])
    raise



