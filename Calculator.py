import tkinter as tk


window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")
window.resizable(False, False)

def sum():
    answer.delete(0, tk.END)
    answer.insert(0, "{:g}".format(float(entry_1.get()) + float(entry_2.get())))
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")

def sub():
    answer.delete(0, tk.END)
    answer.insert(0, "{:g}".format(float(entry_1.get()) - float(entry_2.get())))
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
def mul():
    answer.delete(0, tk.END)
    answer.insert(0, "{:g}".format(float(entry_1.get()) * float(entry_2.get())))
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
def div():
    answer.delete(0, tk.END)
    answer.insert(0, "{:g}".format(float(entry_1.get()) / float(entry_2.get())))
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")




label = tk.Label(window, text="Calculator")
label_1 = tk.Label(window, text="First Number")
label_2 = tk.Label(window, text="Second Number")
answer_l = tk.Label(window, text="Result")

entry_1 = tk.Entry(window)
entry_2 = tk.Entry(window)
answer = tk.Entry(window)

button_sum = tk.Button(window,text = "+", height = 4, width = 4,command = sum)
button_sub = tk.Button(window,text = "-", height = 4, width = 4, command = sub)
button_mil = tk.Button(window,text = "*", height = 4, width = 4, command = mul)
button_div = tk.Button(window,text = "/", height = 4, width = 4, command = div)


entry_1.place(x=100,y=50)
entry_2.place(x=100,y=100)
answer.place(x=100,y=150)

label_1.place(x=150,y=25)
label_2.place(x=150,y=75)
answer_l.place(x=150,y=125)

button_sum.place(x=200,y=200)
button_sub.place(x=120,y=200)
button_mil.place(x=200,y=280)
button_div.place(x=120,y=280)


window.mainloop()
