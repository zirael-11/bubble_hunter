import random
import tkinter
from math import radians

from tkinter import Canvas

window = tkinter.Tk()

window.geometry('800x600')
window.title('Bubble Haunter')

canvas = Canvas(window, background='#000485', height=600, width=800)
window.focus_set()
canvas.pack()

ball = canvas.create_oval(200, 200, 240, 240, outline='yellow')
#
# bubbles_x = [ random.randint(10, 800) for _ in range(5)]
# bubbles_y = [ random.randint(10, 600) for _ in range(5)]
# bubbles_r = [ random.randint(10, 30) for _ in range(5)]
#
# bubbles = []
# for i in range(5):
#     bubbles.append(canvas.create_oval(
#         bubbles_x[i],
#         bubbles_y[i],
#         bubbles_x[i] + bubbles_r[i],
#         bubbles_y[i] + bubbles_r[i],
#         outline="white"
#     ))
# import threading

class Bubble:
    def __init__(self, x, y, r, color):
        self.color = color
        self.r = r
        self.y = y
        self.x = x
        self.image = canvas.create_oval(
            self.x,
            self.y,
            self.x + self.r,
            self.y + self.r,
            outline=self.color
        )

bubbles= []
for i in range(5):
    bubbles.append(Bubble(
        random.randint(10, 800),
        random.randint(10, 600),
        random.randint(10, 30),
        "white"
    ))

def move(event):
    if event.keysym == "Up":
        canvas.move(ball, 0, -5)
    if event.keysym == "Down":
        canvas.move(ball, 0, 5)
    if event.keysym == "Left":
        canvas.move(ball, -5, 0)
    if event.keysym == "Right":
        canvas.move(ball, 5, 0)


window.bind("<Key>", move)

window.mainloop()
