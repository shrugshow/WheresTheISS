import turtle

benPath = '/home/neb/PythonProjects/WheresTheISS/'
alexPath = 'img/'

class ScreenSetup:
    def __init__ (self):
        self.screen = turtle.Screen()
        self.screen.setup(1080, 480)
        self.screen.setworldcoordinates(-180, -90, 180, 90)
        self.screen.bgpic(alexPath + 'map.gif')
        self.screen.register_shape(alexPath + 'satellite-sml.gif')
        # self.screen.bgpic(benPath, 'map.gif')
        # self.screen.register_shape(benPath, 'satellite-sml.gif')

