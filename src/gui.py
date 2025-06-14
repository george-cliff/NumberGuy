# Standard library imports
import os
import threading
from PIL import ImageGrab

# Third-party imports
from tkinter import Tk, Canvas, Button, Toplevel, Label, font

# Local application imports
from .path import get_model_path, get_temp_path
from .model import predict_digit, generate
from .image import prepare_image

def draw(event, canvas):
    x, y = event.x, event.y
    r = 10
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")

def setup():
    window = Tk()
    window.geometry("400x500")
    window.configure(background="teal")
    window.title("NumberGuy")

    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=14)

    canvas = Canvas(window, width=280, height=280, bg= "white")
    canvas.bind("<B1-Motion>", lambda event: draw(event, canvas))
    canvas.pack(pady=10)

    button_clear = Button(window, text="clear", command=lambda: btn_clear(canvas))
    button_clear.pack(pady=10)

    button_submit = Button(window, text="submit", command=lambda: btn_submit(canvas, window, default_font))
    button_submit.pack(pady=10)

    button_generate = Button(window, text="generate model", command=btn_generate)
    button_generate.pack(pady=10)

    window.mainloop()

def btn_clear(canvas):
    canvas.delete("all")

def popup_def(popup_msg, size=(400, 60), disable_close=False):
    popup = Toplevel()
    popup.title("Alert")
    msg = Label(popup, text=popup_msg)
    msg.pack(padx=20, pady=20)
    w, h = size
    popup.geometry(f"{w}x{h}")
    popup.transient()
    popup.grab_set()
    popup.attributes('-topmost', True)
    popup.resizable(False, False)
    if disable_close:
        popup.protocol("WM_DELETE_WINDOW", lambda: None)
    return popup

def popup_ans(digit, default_font):
    popup = Toplevel()
    popup.title("Result")

    # Message label (normal font)
    msg = Label(popup, text="I, the Number Guy, think you've drawn the number\n")
    msg.pack(padx=10, pady=(10, 0))

    big_font = default_font.copy()
    big_font.configure(size=48)  # Adjust size as you want

    # Digit label with bigger font
    digit_label = Label(popup, text=str(digit), font=big_font, fg="black")
    digit_label.pack(padx=10, pady=(0, 20))

    # Set popup size roughly, adjust if you want
    popup.geometry("600x150")
    popup.transient()
    popup.grab_set()
    popup.attributes('-topmost', True)
    popup.resizable(False, False)

    return popup


def save_img(window, canvas, temp_path):
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    image = ImageGrab.grab(bbox=(x, y, x1, y1))
    image.save(os.path.join(temp_path, "img.png"))
    print("Image saved to temp/img.png")

def btn_submit(canvas, window, default_font):
    temp_path = get_temp_path()
    model_path = get_model_path()
    model_files = [f for f in os.listdir(model_path) if f.endswith(".h5")]
    if model_files:
        save_img(window, canvas, temp_path)
        img_array = prepare_image()
        digit = predict_digit(img_array, model_files)
        popup_ans(digit, default_font)
    else:
        popup_def("no model found, please generate a model first", size=(600, 60))

def btn_generate():
    popup = popup_def("generating model...", disable_close=True)

    def run_model():
        generate()
        popup.after(0, popup.destroy)

    threading.Thread(target=run_model).start()