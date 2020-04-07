import pyowm
import time

owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
city = input("What city do you want to khow weather in?: ")
observation = owm.weather_at_place(city)
w = observation.get_weather()
#print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
sky = w.get_status()
wind = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
humidity = w.get_humidity()              # 87
temperature = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
sky = w.get_status()

print("In {} the weather is fine:".format(city))
print("Sky is {} ".format(sky))
print("Wind is {} m/s\nDirection is {} degrees".format(wind['speed'],wind['deg']))
print("Humidity is {}%".format(humidity))
print("Temperature is {}°C".format(temperature['temp']))


# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)