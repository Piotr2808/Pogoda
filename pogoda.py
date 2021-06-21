import requests
import datetime
import pprint
#'http://api.weatherapi.com/v1/current.json?key=0e7e4398f1164df2827105246212106&q=Amsterdam&aqi=no'

class GetData:
    def __init__(self, url):
        self.url = url
        self.data = self.get_data()

    def get_data(self):
        r = requests.get(self.url)
        return r.json()

data = GetData('http://api.weatherapi.com/v1/current.json?key=0e7e4398f1164df2827105246212106&q=Amsterdam&aqi=no')
data.get_data()