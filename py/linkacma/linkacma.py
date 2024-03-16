from tkinter import *
import webbrowser as w

def open_links():
    with open("lınk.txt", "r") as file:
        links = file.readlines()
        for link in links:
            w.open(link.strip())

x = Tk()

def clicked():
    open_links()

link_button = Button(x, text="Open Links", command=clicked)
link_button.pack(pady=200, padx=200)

x.mainloop()
