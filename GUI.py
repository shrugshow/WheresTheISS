import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.background_image=tkinter.PhotoImage('~/WheresTheISS/img/map.gif')
        self.background_label = tkinter.Label(image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.findbutton = tkinter.Button(self.main_window, text='Find it!', 
                                         fg='white', bg='blue', 
                                         command=self.do_something)
        self.findbutton.pack()
        self.quitbutton = tkinter.Button(self.main_window, text='Quit', 
                                         fg='white', bg='blue', 
                                         command=self.main_window.destroy)
        self.quitbutton.pack()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.top_frame, text='Where is the ISS?')
        self.label2 = tkinter.Label(self.bottom_frame, text='Where is the ISS?')
        self.label1.pack(side='top')
        self.label2.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.background_label.image = self.background_image
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'The ISS was found at: ')

gui = GUI()
gui.main_window.title("Where is the ISS?")
gui.main_window.maxsize(1000, 400)
gui.mainloop()


