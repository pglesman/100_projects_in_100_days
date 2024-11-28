from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_marks_label.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        # count_down(LONG_BREAK_MIN * 60)
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        # count_down(SHORT_BREAK_MIN * 60)
        count_down(2)
        timer_label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        # count_down(2)
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = reps // 2 * '✔'
        check_marks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 111, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, 'bold'))
timer_label.grid(column=1, row=0)

check_marks_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, 'bold'))
check_marks_label.grid(column=1, row=3)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
