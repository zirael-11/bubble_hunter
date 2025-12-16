import tkinter

window = tkinter.Tk()


class Color:
    def __init__(self, name, bg, fg):
        self.name = name
        self.bg = bg
        self.fg = fg


window.geometry('800x600')
window.title('Color btn')

button_colors = [
    Color('green', 'pink', '#7be9ed'),
    Color('black', 'red', '#7b42f5'),
    Color('red', '#d142f5', '#215e16'),
    Color('white', '#7be9ed', 'yellow'),
    Color('black', 'red', '#7b42f5'),
    Color('red', '#d142f5', '#215e16'),
    Color('white', '#7be9ed', 'yellow')
]

def handle_click(color_text:str):
    color_lbl.config(text=f'Текущий цвет: {color_text}.')

def make_btn(color: Color):
    action_btn = tkinter.Button(
        window,
        text=color.name,
        bg=color.bg,
        fg=color.fg,
        width=14,
        command=lambda: handle_click(color.name)
    )
    action_btn.pack()


color_lbl = tkinter.Label(window, text='Текущий цвет: ')
color_lbl.pack()
for button_color in button_colors:
    make_btn(button_color)

window.mainloop()

