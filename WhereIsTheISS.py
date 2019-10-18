import json
import turtle
import urllib.request
import time
import ScreenSetup
import ISS

# attempted object usage
# I don't work! The "location response" on line 14 breaks when looking at the json
# issObj = ISS.ISS()
# issObj.printAstronauts()
# issObj.printLatLong()

#pull the number and names of people in space, and print to the console
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('People in Space: ', result['number'])
people = result['people']
for p in people:
    print(p['name'] + ' in the ', p['craft'])

# Some methods: print to map

def printToMap(lat, long, color, message):
    style = ('Gotham', 8, 'italic')
    turtle.goto(long, lat)
    turtle.color(color)
    turtle.write(message, style)

#pull the current longitude and lattitude of the ISS, print it to the console
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print("Latitude: ", lat)
print("Longitude: ", lon)
# set up turtle graphics 
# look to the ScreenSetup object to comment out the proper path
screen = ScreenSetup.ScreenSetup()
iss = turtle.Turtle()
iss.shape('img/satellite-sml.gif')
# iss.shape('/home/neb/PythonProjects/WheresTheISS/satellite-sml.gif')
iss.setheading(90)

#place turtle at current ISS location
iss.penup()
iss.goto(float(lon), float(lat))

#find next overhead pass of location (lat, lon) and print it to the console
url = "http://api.open-notify.org/iss-pass.json"

# AM - url for the current location: this was just to get it to work on my system.
urlCurrentISS = url +"?lat="+str(lat)+"&lon="+str(lon)
response = urllib.request.urlopen(urlCurrentISS)
result = json.loads(response.read())
over = result['response'][1]['risetime']
currLocationPrintout = "Currently at " + str(lat) + " lat, " + str(lon) + "\nTime is " + time.ctime(over) + " local time"

# AM - Rocky Hill variables
latRH = 41.0000
lonRH = -71.0000
urlRH = url + "?lat=" + str(latRH) + "&lon=" + str(lonRH)
responseRH = urllib.request.urlopen(urlRH)
resultRH = json.loads(responseRH.read())
timeOverRH = resultRH['response'][1]['risetime']
rockyHillPrintout = "Next Rocky Hill Fly-Over: " + time.ctime(timeOverRH)

print("Rocky Hill flyover: ", time.ctime(timeOverRH))
print(time.ctime(over))

turtle.penup()

printToMap(latRH, lonRH, "red", "X")
printToMap(-70, -170, "white", rockyHillPrintout)
printToMap(-80, -170, "white", currLocationPrintout)

turtle.mainloop()

