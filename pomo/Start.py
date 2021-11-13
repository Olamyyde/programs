from tkinter import *
# from PIL import ImageTk,Image

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timer Mechanism
def start_timer():
    count_down(5)



# Count Down Mechanism
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)
    


# UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #Creates Canvas
canvas.grid(column=1, row=1)
tomato_img = PhotoImage(file=r"C:\Users\Public\Pictures\cat.png")
# tomato_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Public\Pictures\cat.png"))
canvas.create_image(100, 112, image="tomato_img")

timer_text = canvas.create_text(103, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


my_lab = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
my_lab.grid(column=1, row=0)

start_btn = Button(text="start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="reset", highlightthickness=0)
start_btn.grid(column=2, row=2)






check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()