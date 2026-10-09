import requests
from app_logger import logger
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
API_key=os.getenv("openweather_API")

#request the weather data of the place
def get_weather(lat,lon):
        urlweather=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
        response=requests.get(urlweather, timeout=10)
        response.raise_for_status()
        logger.log_program.info("weather info gotten")
        response=response.json()
        lattitude=response['coord']['lat']
        longitude=response['coord']['lon']
        weather_description = (response['weather'][0]['main'], response['weather'][0]['description'])
        temperature= response['main']['temp']
        temperature_min=response['main']['temp_min']
        temperature_max=response['main']['temp_max']
        pressure=response['main']['pressure']
        humidity=response['main']['humidity']
        visibility=response['visibility']
        dt=response['dt']
        time=datetime.fromtimestamp(dt)
        tzone=response['timezone']
        timezone=datetime.fromtimestamp(tzone).time()
        print("\n======================WEATHER======================")
        print(f"Time={time}Celsius, Timezone=+{timezone}\nLongitude={longitude}degrees, Lattitude={lattitude}degrees\nWeather={weather_description}\nTemperature={temperature}Celsius, Lowest Temperature={temperature_min}Celsius, Highest Temperature={temperature_max}Celsius\nPressure={pressure}hPa, Humidity={humidity}%\nThe maximum distance you can see is {visibility}meters\n\n")
        print("==========FORECAST==========")
        urlweather=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric"
        response_F=requests.get(urlweather, timeout=10)
        response_F.raise_for_status
        logger.log_program.info("forecast info gotten")
        response_F=response_F.json()
        response_F=response_F['list'][0]
        weather_description_forecast = (response_F['weather'][0]['main'], response_F['weather'][0]['description'])
        temperature_forecast= response_F['main']['temp']
        temperature_min_forecast=response_F['main']['temp_min']
        temperature_max_forecast=response_F['main']['temp_max']
        pressure_forecast=response_F['main']['pressure']
        humidity_forecast=response_F['main']['humidity']
        visibility_forecast=response_F['visibility']
        forecast_time=response_F['dt_txt']
        print(f"FORECAST TIME= {forecast_time}\nWeather={weather_description_forecast}\nTemperature= {temperature_forecast} Celsius, Lowest Temperature= {temperature_min_forecast}Celsius, Highest Temperature= {temperature_max_forecast} Celsius\nPressure= {pressure_forecast}hPa, Humidity= {humidity_forecast}%\nThe maximum distance you can see is {visibility_forecast}meters\n")



        

