import json

file = open("weather.json","r")

data= file.read()
 #print(type(data))
json_data = json.loads(data)
#print(type(json_data)

print(json_data['main']['temp'])

weather=json_data['weather'][0]['main']
print(weather)

print(json_data['wind']['speed'])

#sunrise
#format and print 10:30 PM



