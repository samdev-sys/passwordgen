import requests

# API_KEY ="APIweather" pendiente API_key
city="cali" 
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"

response =requests.get(url)
data= response.json()


if response.status_code==200:
    temp=data["main"]["temp"]
    description= data["weather"][0]["description"]
    print("el clima en {city} es {description} con {temp}°C.")
else:
    print("error al obtener datos")