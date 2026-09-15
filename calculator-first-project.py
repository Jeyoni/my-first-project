import math
import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="],
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey = "#505050"
color_orange = "#FF9900"
color_white = "#FFFFFF"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 45),
    background=color_black,
    foreground=color_white,
    anchor="e",
    width=column_count,
)

label.grid(row=0, column=0, columnspan=column_count, sticky="nsew")
for row in range(row_count):
    for column in range(column_count):
        button_value = button_values[row][column]
        button = tkinter.Button(
            frame,
            text=button_value,
            font=("Arial", 30),
            width=column_count - 1,
            height=1,
            command=lambda value=button_value: button_click(value),
        )

        if button_value in top_symbols:
            button.config(background=color_light_gray, foreground=color_black)
        elif button_value in right_symbols:
            button.config(background=color_orange, foreground=color_white)
        else:
            button.config(background=color_dark_grey, foreground=color_white)
        button.grid(row=row + 1, column=column, sticky="nsew")

frame.pack()

A = None
operator = None
reset_screen = False


def clear_all():
    global A, operator, reset_screen
    A = None
    operator = None
    reset_screen = False
    label["text"] = "0"


def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_click(value):
    global A, operator, reset_screen

    if value in ["+", "-", "×", "÷"]:
        A = float(label["text"])
        operator = value
        reset_screen = True

    elif value == "=":
        if A is not None and operator is not None:
            B = float(label["text"])
            if operator == "+":
                result = A + B
            elif operator == "-":
                result = A - B
            elif operator == "×":
                result = A * B
            elif operator == "÷":
                result = A / B if B != 0 else "Error"

            if result != "Error":
                label["text"] = remove_zero_decimal(result)
            else:
                label["text"] = "Error"

            A = None
            operator = None
            reset_screen = True

    elif value == "AC":
        clear_all()

    elif value == "+/-":
        result = float(label["text"]) * -1
        label["text"] = remove_zero_decimal(result)

    elif value == "%":
        result = float(label["text"]) / 100
        label["text"] = remove_zero_decimal(result)

    elif value == "√":
        num = float(label["text"])
        if num >= 0:
            label["text"] = remove_zero_decimal(math.sqrt(num))
        else:
            label["text"] = "Error"
        reset_screen = True

    elif value == ".":
        if reset_screen:
            label["text"] = "0."
            reset_screen = False
        elif "." not in label["text"]:
            label["text"] += value

    elif value in "0123456789":
        if label["text"] == "0" or reset_screen:
            label["text"] = value
            reset_screen = False
        else:
            label["text"] += value


window.update()
width = window.winfo_width()
window_height = window.winfo_height()
screen_window_width = window.winfo_screenwidth()
screen_window_height = window.winfo_screenheight()

screen_center_x = int((screen_window_width / 2) - (width / 2))
screen_center_y = int((screen_window_height / 2) - (window_height / 2))
screen_center = f"{width}x{window_height}+{screen_center_x}+{screen_center_y}"
window.geometry(screen_center)

window.mainloop()