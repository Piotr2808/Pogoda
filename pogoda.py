# importy

import requests
import datetime
import pprint

# listy

information = []
show_info = []

# klasy

class Weather:
    def __init__(self, name, temp_c, rain):
        self.name = name
        self.temp_c = temp_c
        self.rain = rain
    def __str__(self):
        return f'Miasto: {self.name},Temperatura: {self.temp_c},Deszcz: {self.rain}'

    def write_txt(self):
        with open("Weather.txt", "w") as file:
            file.write(f'{self.name},{self.temp_c},{self.rain}')

    def reader_txt(self):
        with open("Weather.txt", "r") as read_file:
            read_file.readline()

class GetData:
    def __init__(self, url, city, date):
        self.date = date
        self.city = city
        self.url = url
        self.data = self.get_data()

    def get_data(self):
        params = {'q': self.city, 'dt': self.date}
        r = requests.get(self.url, params=params)
        return r.json()

# dane

city = input("City: ")
date = input("Data: (yyyy-mm-dd): ")
data = GetData('http://api.weatherapi.com/v1/current.json?key=0e7e4398f1164df2827105246212106', city, date)

# Fory i inne mieszanki

czytacz = open("Weather.txt", "r")

for entry in data.data.items():
        information.append(entry)
for word in information[0] or information[1]:
    if 'name' in word:
        w_n = word['name']
        show_info.append(w_n)
for word_two in information[1]:
    if 'temp_c' in word_two:
        w_t_t = word_two['temp_c']
        show_info.append(w_t_t)
for word_three in information[1]:
    if 'precip_mm' in word_three:
        if float(word_three['precip_mm']) == 0.0:
            warun_1 = "Nie będzie padać"
            show_info.append(warun_1)
        if float(word_three['precip_mm']) > 0.0 and float(word_three['precip_mm']) < 0.9:
            warun_2 = "Może będzie padać"
            show_info.append(warun_2)
        if float(word_three['precip_mm']) > 1.0:
            warun_3 = "Będzie padać"
            show_info.append(warun_3)

# dalsze dane

weather = Weather(show_info[0], show_info[1], show_info[2])
print(weather)

# zapis do txt

weather.write_txt()