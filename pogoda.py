import requests
import datetime
import pprint

# My API:
# 'http://api.weatherapi.com/v1/current.json?key=0e7e4398f1164df2827105246212106&q=Amsterdam&aqi=no'

information = []
show_info = []

class Weather:
    def __init__(self, name, temp_c, localtime):
        self.name = name
        self.temp_c = temp_c
        self.localtime = localtime
    def __str__(self):
        return f'Miasto: {self.name},Temperatura: {self.temp_c},Data: {self.localtime}'


class GetData:
    def __init__(self, url):
        self.url = url
        self.data = self.get_data()

    def get_data(self):
        r = requests.get(self.url)
        return r.json()
# 'http://api.weatherapi.com/v1/current.json?key=0e7e4398f1164df2827105246212106&q=Amsterdam&aqi=no'
city = input("City: ")
data = GetData(f'http://api.weatherapi.com/v1/current.json?key=0e7e4398f1164df2827105246212106&q={city}&aqi=no')
# pprint.pprint(data.data)

for entry in data.data.items():
        information.append(entry)
for word in information[0]:
    if 'name' in word:
        w_n = word['name']
        show_info.append(w_n)
    if 'localtime' in word:
        # format = yyyy-mm-dd
        w_l = word['localtime'][0:10]
        # w_l = input("Data(yyyy-mm-dd): ")
        show_info.append(w_l)
for word_two in information[1]:
    if 'temp_c' in word_two:
        w_t_t = word_two['temp_c']
        show_info.append(w_t_t)

weather = Weather(show_info[0], show_info[2], show_info[1])
print(weather)