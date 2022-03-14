from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BEIGE = "#F6E7D8"
PINK = "#F68989"
RED = "#C65D7B"
BROWN = "#874356"
GREEN = "#C5D8A4"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    label_Time.config(text="Timer", foreground=BROWN)
    label_check_mark.config(text="")
    image.itemconfig(time_text, text="00:00")
    global repetition
    repetition = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    global repetition
    repetition += 1

    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if repetition == 8:
        count_down(long_break_time)
        label_Time.config(text="Long break", foreground=GREEN)
        label_check_mark.config(text="")
    elif repetition % 2 == 0:
        count_down(short_break_time)
        label_Time.config(text="Short break", foreground=PINK)
    else:
        count_down(work_time)
        label_Time.config(text="Work time", foreground=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(counter):
    timer_min = int(counter / 60)
    timer_sec = counter % 60

    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"
    elif timer_sec >= 10 and timer_sec < 60:
        timer_sec = f"{timer_sec}"
    elif timer_sec == 0:
        timer_sec = "00"
    if timer_min < 10:
        timer_min = f"0{timer_min}"

    image.itemconfig(time_text,text=f"{timer_min}:{timer_sec}")

    if counter > 0:
        global timer
        timer = window.after(1000,count_down,counter-1)
    else:
        start_time()
        if repetition == 2:
            label_check_mark.config(text="✔")
        elif repetition == 4:
            label_check_mark.config(text="✔✔")
        elif repetition == 6:
            label_check_mark.config(text="✔✔✔")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(width=350, height=312)
window.title("Pomodoro Timer")
window.config(background=BEIGE)

image = Canvas(width=202, height=223, background=BEIGE, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
image.create_image(100, 110, anchor=CENTER,image=tomato_image)
time_text = image.create_text(103, 120, text = "00:00", fill="white", font=(FONT_NAME,30))
image.grid(row=1, column=1)


label_Time = Label(text="Time", font=(FONT_NAME,50), foreground=BROWN, background=BEIGE)
label_Time.grid(row=0, column=1)

label_check_mark = Label(text="", foreground=BROWN, background=BEIGE, width=5, height=5, font=(FONT_NAME, 15))
label_check_mark.grid(row=2, column=1)

button_start = Button(text="start", font=(FONT_NAME,20), foreground=BROWN, background=BEIGE,
                      borderwidth=0, padx=10, command= start_time)
button_start.grid(row=2, column=0)

button_reset = Button(text="reset", font=(FONT_NAME,20), foreground=BROWN, background=BEIGE,
                      borderwidth = 0, padx=10, command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
