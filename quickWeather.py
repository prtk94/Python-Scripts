#! python3
# quickWeather.py - Prints the weather for a location from the command line.
import json, requests, sys
# Compute location from command line arguments.
if (len(sys.argv) <2):
	print("Usage: quickWeather.py location ")

location = ' '.join(sys.argv[1:])
print("Fetching data from OpenWeatherMap.org's API for "+location+"....")
print('\n\n')

# Download the JSON data from OpenWeatherMap.org's API. &APPID={9e4ca7187529e25726e2527b989b3afe}
#
url ='http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=9e4ca7187529e25726e2527b989b3afe' % (location)
response = requests.get(url)
response.raise_for_status()
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
w = weatherData['list']
todaysMin = float(w[0]['main']['temp_min']) -272.15 
todaysMax = float(w[0]['main']['temp_max']) -272.15 
print('Current weather forecast in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('The minimum temp is : ' + str(round(todaysMin,2))+ ' degree Celsius' + ' and max is : '+ str(round(todaysMax,2))+ ' degree Celsius.' )
print()
print('Tomorrow\'s forecast:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow\'s forecast:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])	