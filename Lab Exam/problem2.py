import requests
import json


def weather_data():
    lat = 22.355734742341156
    lon=91.78545828149409
    api_key= '30d4741c779ba94c470ca1f63045390a'
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={api_key}"
    weather_data = requests.get(api_url)
    content_data = weather_data.content.decode('UTF-8')
    json_data = json.loads(content_data)
    print('City: Chattogram,',json_data['name'])
    print('weather:',json_data['weather'][0]['main'])
    print('Temperatue: ',json_data['main']['temp'],'K')
    print('Pressure: ',json_data['main']['pressure'])
    print('Humidity: ',json_data['main']['humidity'])
    print('Wind Speed: ',json_data['wind'])

weather_data()

