import requests
import json

API_KEY = "3671248f2d09c9dd699eb07ff60ea5bd"

city = input("Enter the city you are looking for: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Weather:", data["weather"][0]["description"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("Error:", data["message"])


