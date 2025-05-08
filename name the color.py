import tkinter as tk
import random

window = tk.Tk()
window.title("name the color")
window.geometry("500x500")

colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown", "white"]

right_answer = 0
mistake_answer = 0
time = 30
a = 0
def timer():
    global time
    if time > 0:
        time -= 1
        time_label["text"] = f"time left: {time} "
        time_label.after(1000, timer)

def new_word():
    color_label["fg"] = random.choice(colors)
    color_label["text"] = random.choice(colors)

def check (event):

    global right_answer
    global mistake_answer
    global time
    global a
    if a == 0:
        timer()
        a += 1
    if time > 0:
        instruction["text"] = ""
        user_color = entry.get()
        if user_color != "":
            word_color = color_label["fg"]
            if word_color == user_color:
                right_answer += 1
                right["text"] = f"right: {right_answer}"
            else:
                mistake_answer += 1
                mistake["text"] = f"mistake: {mistake_answer}"

            new_word()
        entry.delete(0, tk.END)


instruction = tk.Label(window, text = "Введи цвет слова, а не слово! Жми Enter, чтобы играть.", font = ("Helvetica",12))
color_label = tk.Label(window, text = "color", font = ("Helvetica",60))
right = tk.Label(window, text = f"right: 0", font = ("Helvetica",20))
mistake = tk.Label(window, text = f"mistake: 0", font = ("Helvetica",20))
time_label = tk.Label(window, text = time, font = ("Helvetica",20))

right.place(x = 50,y = 300)
mistake.place(x = 50,y = 350)
time_label.place(x = 0,y = 0)

entry = tk.Entry(window)

entry.place(x = 10, y = 180)
instruction.pack()
color_label.place(x=10, y=80)
entry.focus_set()



window.bind("<Return>", check)

window.mainloop()

