# Standard library imports
import os
import shutil
import threading
from PIL import ImageGrab, Image, ImageTk

# Third-party imports
from tkinter import Tk, Canvas, Button, Toplevel, Label, font, Frame, LEFT, RIGHT

# Local application imports
from .path import get_model_path, get_temp_path
from .model import predict_digit, generate
from .image_processing import prepare_image, confirmed_digit

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

def cleanup(canvas):
    canvas.delete("all")
    temp_path = get_temp_path()
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    os.makedirs(temp_path)

def btn_clear(canvas):
    cleanup(canvas)

def popup_def(popup_msg, size=(400, 70), disable_close=False):
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

def popup_guess(ranking, img_file, canvas, default_font, index=0):

    if index>=len(ranking):
        popup_def("NumberGuy is out of digits...")
        cleanup(canvas)
        return
    else:
        popup = Toplevel()
        popup.geometry("600x350")
        popup.transient()
        popup.grab_set()
        popup.attributes('-topmost', True)
        popup.resizable(False, False)
        popup.protocol("WM_DELETE_WINDOW", lambda: None)

        digit, confidence = ranking[index]

        popup.title("Result")

        img = Image.open(img_file).resize((150, 150))
        tk_img = ImageTk.PhotoImage(img)

        border_frame = Frame(popup, borderwidth=2, relief="solid", background="teal")
        border_frame.pack(pady=10)

        img_label = Label(border_frame, image=tk_img)
        img_label.image = tk_img  # keep reference
        img_label.pack()

        msg = Label(popup, text=f"Number Guy is {confidence:.2%} confident \n you've drawn the number:")
        msg.pack()

        big_font = default_font.copy()
        big_font.configure(size=32)
        digit_label = Label(popup, text=str(digit), font=big_font, fg="black")
        digit_label.pack()

        def ans_yes(canvas):
            print(f"{digit} correct")
            popup.destroy()
            confirmed_digit(digit)
            cleanup(canvas)

        def ans_no():
            print(f"{digit} incorrect")
            popup.destroy()
            popup_guess(ranking, img_file, default_font, index + 1)

        button = Frame(popup)
        button.pack(pady=10)

        button_yes = Button(button, text="yes", command=lambda: ans_yes(canvas))
        button_yes.pack(side=LEFT, padx=10)

        button_no = Button(button, text="no", command=ans_no)
        button_no.pack(side=RIGHT, padx=10)

def popup_load():
    popup_def(popup_msg="generating model...", size=(300, 70), disable_close=True)

def save_img(window, canvas, temp_path):
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    image = ImageGrab.grab(bbox=(x, y, x1, y1))
    image.save(os.path.join(temp_path, "img.png"))
    print("Image saved to temp/img.png")
    canvas.delete("all")

def btn_submit(canvas, window, default_font):
    temp_path = get_temp_path()
    model_path = get_model_path()
    model_files = [f for f in os.listdir(model_path) if f.endswith(".h5")]
    if model_files:
        save_img(window, canvas, temp_path)
        img_array, img_file = prepare_image()
        ranking= predict_digit(img_array, model_files)
        popup_guess(ranking, img_file, canvas, default_font)
    else:
        popup_def("no model found, please generate a model first", size=(600, 60))

def btn_generate():
    popup = popup_load()

    def run_model():
        generate()
        popup.after(0, popup.destroy)

    threading.Thread(target=run_model).start()