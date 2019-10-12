import tkinter

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text='Where is the ISS?')
        self.label2 = tkinter.Label(self.main_window, text='Where is the ISS?')
        self.label1.pack()
        self.label2.pack()
        tkinter.mainloop()

gui = GUI()


