import requests

api_key = "d94220aab9bb5055c3618578a10df0f1"

user_input = input("Enter city:")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")



if weather_data.json() ["cod"] == 404:
	print ("CITY NOT FOUND")

else:
	weather = weather_data.json() ["weather"] [0] ["main"]
	sensation = weather_data.json() ["main"] ["feels_like"]
	temperature = round(weather_data.json () ["main"] ["temp"]) 
	
	#Convert from fahrenheit to celcius
	sensation = (sensation - 32) * 5/9
	temperature = (temperature - 32) * 5/9

	print ("The weather in " +user_input+  " is " +str(weather))
	print ("The tempreture in " +user_input+ " is " +str(temperature)+ "ºC but it feels like " +str(sensation)+ "ºC")