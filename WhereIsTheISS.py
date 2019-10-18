import json
import turtle
import urllib.request
import time

#pull the number and names of people in space, and print to the console
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('People in Space: ', result['number'])
people = result['people']
for p in people:
    print(p['name'] + ' in the ', p['craft'])

#pull the current longitude and lattitude of the ISS, print it to the console
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print("Latitude: ", lat)
print("Longitude: ", lon)
#set up turtle graphics
screen = turtle.Screen()
screen.setup(1080, 480)
screen.setworldcoordinates(-180, -90, 180, 90)

# AM changed to reflect local path of map and satellite images
screen.bgpic('img/map.gif')
# screen.bgpic('/home/neb/PythonProjects/WheresTheISS/map.gif')
screen.register_shape('img/satellite-sml.gif')
# screen.register_shape('/home/neb/PythonProjects/WheresTheISS/satellite-sml.gif')
iss = turtle.Turtle()
iss.shape('img/satellite-sml.gif')
# iss.shape('/home/neb/PythonProjects/WheresTheISS/satellite-sml.gif')
iss.setheading(90)

#place turtle at current ISS location
iss.penup()
iss.goto(float(lon), float(lat))

#find next overhead pass of location (lat, lon) and print it to the console
# lat = -72
# lon = 41
url = "http://api.open-notify.org/iss-pass.json"

# AM - url for the current location: this was just to get it to work on my system.
urlCurrentISS = url +"?lat="+str(lat)+"&lon="+str(lon)
response = urllib.request.urlopen(urlCurrentISS)
result = json.loads(response.read())
over = result['response'][1]['risetime']

# AM - Rocky Hill variables
latRH = 41.0000
lonRH = -71.0000
urlRH = url + "?lat=" + str(latRH) + "&lon=" + str(lonRH)
responseRH = urllib.request.urlopen(urlRH)
resultRH = json.loads(responseRH.read())
timeOverRH = resultRH['response'][1]['risetime']

style = ('Gotham', 8, 'italic')
print("Rocky Hill flyover: ", time.ctime(timeOverRH))
print(time.ctime(over))
turtle.penup()
turtle.goto(-170, -80)
turtle.color("white")
turtle.write(time.ctime(over), font=style)

turtle.penup()
turtle.goto(-170, -70)
turtle.color("white")
turtle.write("Next Rocky Hill Fly-Over: ", " test", font=style)

turtle.mainloop()