import tkinter as tk
import random
from curses.ascii import isalpha
from tkinter import messagebox as mb

window = tk.Tk()

window.title("Guess the word")
window.geometry("400x400")
words = ["cake", "make", "take"]
letters = []
guess = random.choice(words)
attempts = 3

def validate_input(value):
    return len(value) <= 1 and (value.isalpha() or value == "")

vcmd = window.register(validate_input)
def new():
    global guess
    global letters
    global attempts
    m = mb.askyesno("New Game", "Wanna start a new game?")
    if m == True:
        attempts = 3
        lab_att["text"] = f"attempts left: {attempts}"
        letters = []
        guess = random.choice(words)
        label["text"] = "GUESS AGAIN"
    else:
        window.destroy()


def check():
    global guess
    global attempts
    global letters

    lab = ""
    letter = entry.get()
    letters.append(letter)
    entry.delete(0, tk.END)

    for char in guess:
        if char in letters:
            lab += char
        else:
            lab += "*"
        label["text"] = lab
    if letter not in guess:
        attempts -= 1
        lab_att["text"] = f"attempts left: {attempts}"

    if lab == guess:
        mb.showinfo("Correct!", "U won")
        new()

    if attempts == 0:
        mb.showinfo("((", "You lost")
        new()




label = tk.Label(window, text="Guess the word")
lab_att = tk.Label(window, text=f"attempts: {attempts}")
lab_att.place(x = 0, y = 0)
label.place(x=100, y=50)

entry = tk.Entry(window, validate="key",validatecommand=(vcmd, '%P'))
entry.focus_set()
entry.place(x=100, y=100)


check = tk.Button(window, text="Check", command=check)
check.place(x=200, y=300)
window.mainloop()