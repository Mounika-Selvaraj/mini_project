import tkinter as tk 
import requests
import time

def getWeather(city):
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b8562264114252a845e3b7c88d222393"
    json_data = requests.get(api).json()

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = f"{condition}\n{temp}°C"
    final_data = (
        f"Max Temp: {max_temp}°C\n"
        f"Min Temp: {min_temp}°C\n"
        f"Pressure: {pressure} hPa\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind} m/s\n"
        f"Sunrise: {sunrise}\n"
        f"Sunset: {sunset}"
    )

    print("Weather Information:")
    print(final_info)
    print(final_data)

city = input("Enter city name: ")
getWeather(city)
