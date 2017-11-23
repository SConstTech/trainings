

import requests, json, codecs, random

API_KEY = '&APPID=5c55042b76165ad5321007003915fc66'
URL = 'http://api.openweathermap.org/data/2.5/'
city_dict = {}
city_list = []
random_city_list = []

def load_city_list():
    x = json.load(codecs.open('city.list.json', 'r', 'utf-8'))
    for each in x:
        city_dict[each['id']] = each['name']
        city_list.append(each['id'])


def get_weather_for_city(city):
    base_request_url = 'weather?q=' + city
    response = requests.get(URL+base_request_url+API_KEY)
    return response.json()

# current_city_data = get_weather_for_city(city='Sofia').json()
# from pprint import pprint
# pprint (current_city_data['main'])


def build_random_city_list(count):
    for _ in range(count):
        random_number = random.randrange(0, len(city_list))
        random_city_list.append(city_list[random_number])

load_city_list()
build_random_city_list(5)
print (random_city_list)



