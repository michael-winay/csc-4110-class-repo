import random
import tkinter as tk
import tkinter.ttk as ttk
import turtle
import re
from tkinter import Canvas

def madLibsView():
    madLibsView = tk.Toplevel(root)
    madLibsView.geometry('500x400')

    ad1 = ttk.Label(madLibsView, text = "Adjective:").grid(row = 0, column = 0)
    noun1 = ttk.Label(madLibsView, text = "Noun:").grid(row = 1, column = 0)
    verb1 = ttk.Label(madLibsView, text = "Verb:").grid(row = 2, column = 0)

    ad1_entry = ttk.Entry(madLibsView, width = 25)
    ad1_entry.grid(row = 0, column = 1)
    noun1_entry = ttk.Entry(madLibsView, width = 25)
    noun1_entry.grid(row = 1, column = 1)
    verb1_entry = ttk.Entry(madLibsView, width = 25)
    verb1_entry.grid(row = 2, column = 1)

    submit_button = ttk.Button(madLibsView, text="Submit", command=lambda:madLibsAction(noun1_entry.get(), ad1_entry.get(), verb1_entry.get())).grid(row = 3, column = 0)

def madLibsAction(noun1, ad1, verb1):
    #Special character filtering
    noun1 = re.sub(r"[^a-zA-Z ]", "", noun1)
    ad1 = re.sub(r"[^a-zA-Z ]", "", ad1)
    verb1 = re.sub(r"[^a-zA-Z ]", "", verb1)
    lib = {'noun': noun1, 'adjective': ad1, 'verb': verb1}

    madLibsAction = tk.Toplevel(root)

    #Text display
    madlib = tk.Text(madLibsAction)
    madlib.insert(tk.INSERT, "You are a %s %s who can %s things." % (lib["adjective"], lib["noun"], lib["verb"]))
    madlib.pack()

def drawRandom():
    #declaring random values
    sides = random.randint(2, 20)
    length = random.randint(20, 50)
    colors = ["red", "orange", "yellow", "blue", "purple", "green"]
    random_color = random.randint(0, 5)

    regular_polygon = turtle.Turtle()
    regular_polygon.fillcolor(colors[random_color])
    regular_polygon.begin_fill()

    angle = 360 / sides

    #draw polygon
    while(sides != 0):
        regular_polygon.forward(length)
        regular_polygon.left(angle)
        sides -= 1

    regular_polygon.end_fill()

def drawPolygonAction(sides, length, color):
    #declaring user values
    sides = int(sides)
    length = int(length)

    regular_polygon = turtle.Turtle()
    regular_polygon.fillcolor(color)
    regular_polygon.begin_fill()

    angle = 360 / sides

    #draw polygon
    while(sides != 0):
        regular_polygon.forward(length)
        regular_polygon.left(angle)
        sides -= 1

    regular_polygon.end_fill()

#user form for user polygon
def drawPolygonView():
    drawPolygonView = tk.Toplevel(root)
    drawPolygonView.title = ("Draw polygon")
    drawPolygonView.geometry('500x400')

    sides_label = ttk.Label(drawPolygonView, text = "Number of sides:").grid(row = 0, column = 0)
    length_label = ttk.Label(drawPolygonView, text = "Side length:").grid(row = 1, column = 0)
    color_label = ttk.Label(drawPolygonView, text = "Color:").grid(row = 2, column = 0)

    sides_entry = ttk.Entry(drawPolygonView, width = 25)
    sides_entry.grid(row = 0, column = 1)
    length_entry = ttk.Entry(drawPolygonView, width = 25)
    length_entry.grid(row = 1, column = 1)
    color_entry = ttk.Entry(drawPolygonView, width = 25)
    color_entry.grid(row = 2, column = 1)

    submit_button = ttk.Button(drawPolygonView, text="Submit", command = lambda:drawPolygonAction(sides_entry.get(), length_entry.get(), color_entry.get())).grid(row = 3, column = 0)

#quit button action
def quit():
    root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Assignment 08")
    root.geometry('500x400')

    madLibsButton = ttk.Button(root, text="Mad Libs", command = madLibsView)
    madLibsButton.pack()

    drawRandomButton = ttk.Button(root, text="Draw Random Shape", command = drawRandom)
    drawRandomButton.pack()

    drawPolygonButton = ttk.Button(root, text="Draw Your Own Shape", command = drawPolygonView)
    drawPolygonButton.pack()

    quitButton = ttk.Button(root, text="Quit", command = quit)
    quitButton.pack()

    root.mainloop()
