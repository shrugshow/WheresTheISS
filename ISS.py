import json
import urllib.request
import turtle
import time

urlAstronauts = 'http://api.open-notify.org/astros.json'
urlISSpass = 'http://api.open-notify.org/iss-pass.json'

class ISS:
    def __init__ (self):
        self.astronautResponse = urllib.request.urlopen('http://api.open-notify.org/astros.json')
        self.astronautResult = json.loads(self.astronautResponse.read())
        self.people = self.astronautResult['people']
        self.locationResponse = urllib.request.urlopen('http://api.open-notify.org/iss-pass.json')
        self.locationResult = json.loads(self.locationResponse.read())
        self.over = self.locationResult['response'][1]['risetime']
        self.location = self.locationResult['iss_position']
        self.lat = self.location['latitude']
        self.lon = self.location['longitude']
        self.issPic = turtle.Turtle()
        self.issPic.shape('img/satellite-sml.gif')
        self.issPic.setheading(90)
        self.issPic.penup()
        self.issPic.goto(float(self.lon), float(self.lat))
    
    def printLatLong(self):
        print("Latitude: ", self.lat)
        print("Longitude: ", self.lon)

    def printISSCurrLocation(self):
        print("Currently at " + str(self.lat) + " lat, " + str(self.lon) + "\nTime is " + time.ctime(self.over) + " local time")
    
    def printAstronauts(self):
        for p in self.people:
            print(p['name'] + ' in the ', p['craft'])