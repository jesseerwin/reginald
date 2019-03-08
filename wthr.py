import pyowm
def printstatus():
    owm = pyowm.OWM('fc2c24483e65b10657ec3aa11d3c729e')
    observation = owm.weather_at_place('Pensacola,US')
    w = observation.get_weather()
    
    # Weather details
    t = str(w.get_temperature('fahrenheit')['temp']) 
    print(t)
    s = w.get_status()
    print(s)
    global stat
    stat = "Weather is looking like " + s + " and the temperature is " + t + "F"
    return stat 
