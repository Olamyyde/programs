from tkinter import *
# from PIL import ImageTk,Image
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Timer Mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # for 1,3,5,7th rep
    # for 8th rep
    # for 2,4,6th rep

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)




# Count Down Mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        # Add a checkmark for every 2 reps
        mark = ""
        work_sessions = math.floor(reps/2)  # Total work sessions is equal to the round of the reps divided by 2
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)
    

# RESET MECHANISM
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")



# UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #Creates Canvas
canvas.grid(column=1, row=1)
# tomato_img = PhotoImage(file=r"C:\Users\Public\Pictures\cat.png")
# # tomato_img = ImageTk.PhotoImage(Image.open(r"C:\Users\Public\Pictures\cat.png"))
# canvas.create_image(100, 112, image="tomato_img")

timer_text = canvas.create_text(103, 112, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
title_label.grid(column=1, row=0)

start_btn = Button(text="start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()