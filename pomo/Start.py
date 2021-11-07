from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20



# UI setup
window = Tk()
window.title("Pomodoro")

canvas = Canvas(width=900, height=1000)
tomato_img = PhotoImage(file=r"C:\Users\MYYDE\Documents\MY\last_opened_files\practise\pomo\Front.png")
canvas.create_image(100, 112, Image="tomato_img")
canvas.pack()

window.mainloop()