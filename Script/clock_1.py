import time
from tkinter import Tk, Label, Button, Radiobutton, IntVar, Frame

do_format = {"State": True}


def extend():
    x = window.winfo_width() + 120
    y = window.winfo_height()
    window.geometry(f"{x}x{y}")
def shrink():
    x = window.winfo_width() - 120
    y = window.winfo_height()
    window.geometry(f"{x}x{y}")

def format():
    do_format["State"] = not do_format["State"]

def change_time_format():
    if (x.get() == 1):
        am_pm.pack_forget()
        format()
    elif(x.get()== 0):
        am_pm.pack(side="left")
        format()

def transform():
    global transformed
    transformed = not transformed

def create_time_labels(number_of_time_labels: int):
    time_labels_list: list[: Label] = []
    for time_label in range(number_of_time_labels):
        time_labels_list.append(Label(
            content_frame, 
            text="time", 
            font=("Arial", 50), 
            foreground="Green", 
            background="Black", 
            relief="raised", 
            border=10))
    return time_labels_list


def display_time_labels(*args: Label):
    for time_label in args:
        time_label.pack(side="left", fill="x")


def set_time_labels_value(hour, minute, second, am_pm,  hours_label, minutes_label, seconds_label, am_pm_label):
    hours_label.config(text=hour)
    minutes_label.config(text=minute)
    seconds_label.config(text=second)
    am_pm_label.config(text=am_pm)
        


def time_12():
    current_time = time.strftime("%I:%M:%S:%p", time.localtime())
    return current_time.split(":")

def time_24():
    current_time = time.strftime("%H:%M:%S:%p", time.localtime())
    return current_time.split(":")


def update_time_labels():
    if (x.get() == 0):
        hours_value, minutes_value, seconds_value, am_pm_value = time_12()
    else:
        hours_value, minutes_value, seconds_value, am_pm_value = time_24()
    set_time_labels_value(hours_value, minutes_value, seconds_value, am_pm_value, 
                          hours_label=hours, minutes_label=minutes, seconds_label=seconds, am_pm_label=am_pm)
    window.after(1000, update_time_labels)

def time_format_widgets():
    time_formats = ["AM/PM", "24H"]
    for _ in range(len(time_formats)):
        radio_button = Radiobutton(
            time_format_frame, 
            text=time_formats[_], 
            variable=x, 
            value=_, 
            font=("Arial"), 
            foreground="Green", 
            background="Black", 
            activebackground="Black", 
            activeforeground="Green", 
            padx=25, 
            pady=10, 
            width=15, 
            command=change_time_format)
        radio_button.pack(anchor="w")


window = Tk()
window.config(bg="black")
window.resizable(False, False)

window.bind("<Escape>", func=lambda event: window.destroy())

x = IntVar()


content_frame = Frame(window)

time_format_frame = Frame(window)

content_frame.grid(row=0, column=0)
time_format_frame.grid(row=0, column=1)

hours, minutes, seconds, am_pm = create_time_labels(4)

display_time_labels(hours, minutes, seconds, am_pm)
time_format_widgets()
update_time_labels()

window.mainloop()
