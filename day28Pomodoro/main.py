from tkinter import *
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TICK = ""
refresh = None
pygame.init()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global TICK
    window.after_cancel(refresh)
    canvas.itemconfig(time_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS == 8:
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TICK
    count_min = str(int(count / 60)).zfill(2)
    count_sec = str(count % 60).zfill(2)
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global refresh
        refresh = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            TICK += "✔"
            checkmark.config(text=TICK)
            pygame.mixer.music.load("ping.mp3")
            pygame.mixer.music.play()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

checkmark = Label(font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
