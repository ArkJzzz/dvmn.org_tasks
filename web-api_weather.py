#!/usr/bin/python3

import requests

def print_weather_in_cities(cities, url_template, payload):
    for city in cities:
        url = url_template.format(city)
        response = requests.get(url, params=payload)
        print(response.text)

def main():
    url_template = 'http://wttr.in/{}'
    payload = {
        'nTqMm':'', 
        'lang':'ru'
    }
    cities = (
        'London', 
        'Шереметьево', 
        'Санкт-Петербург'
    )
    
    print_weather_in_cities(cities, url_template, payload)

if __name__ == '__main__':
    main()
