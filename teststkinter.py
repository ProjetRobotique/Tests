from tkinter import *

window = Tk()

window.title("Test Tkinter")

window.geometry("720x480")

window.minsize(480, 480)

window.config(background='#41B77F')


label_title = Label(window, text="Bienvenue sur cette fenêtre inutile", font = ("",20), bg='#41B77F', fg='white')
label_title.pack()


window.mainloop()
