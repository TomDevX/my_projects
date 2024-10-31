from tkinter import messagebox
import tkinter as tk
window = tk.Tk()
window.title("tic-tac-toe")
window.geometry("600x600")

label = tk.Label (window, text = "Welcome to Tic-tac-toe", font = ("Arial", 30), bg = "red", fg = "yellow")
label.place(x=75,y=0)

turn = 0

def button1_click():
    global turn
    if turn%2 == 0:
        button1.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button1.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button1.config(state = "disable")
    check_winner()

def button2_click():
    global turn
    if turn%2 == 0:
        button2.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button2.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button2.config(state = "disable")
    check_winner()

def button3_click():
    global turn
    if turn%2 == 0:
        button3.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button3.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button3.config(state = "disable")
    check_winner()

def button4_click():
    global turn
    if turn%2 == 0:
        button4.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button4.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button4.config(state = "disable")
    check_winner()

def button5_click():
    global turn
    if turn%2 == 0:
        button5.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button5.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button5.config(state = "disable")
    check_winner()

def button6_click():
    global turn
    if turn%2 == 0:
        button6.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button6.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button6.config(state = "disable")
    check_winner()

def button7_click():
    global turn
    if turn%2 == 0:
        button7.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button7.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button7.config(state = "disable")
    check_winner()

def button8_click():
    global turn
    if turn%2 == 0:
        button8.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button8.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button8.config(state = "disable")
    check_winner()

def button9_click():
    global turn
    if turn%2 == 0:
        button9.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    else:
        button9.config(text = "O", disabledforeground = "blue", font = ("Arial", 40))
    turn = turn + 1
    button9.config(state = "disable")
    check_winner()

def check_rows():
    if button1["text"] == button2["text"] == button3["text"]:
        return button1["text"]
    if button4["text"] == button5["text"] == button6["text"]:
        return button4["text"]
    if button7["text"] == button8["text"] == button9["text"]:
        return button7["text"]
    return None

def check_cols():
    if button1["text"] == button4["text"] == button7["text"]:
        return button1["text"]
    if button2["text"] == button5["text"] == button8["text"]:
        return button2["text"]
    if button3["text"] == button6["text"] == button9["text"]:
        return button3["text"]
    return None

def check_diags():
    if button1["text"] == button5["text"] == button9["text"]:
        return button1["text"]
    if button3["text"] == button5["text"] == button7["text"]:
        return button3["text"]
    return None

def reset():
    global turn
    turn = 0
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
       button.config(text = "", state = "normal")

def check_winner():
    winner_row = check_rows()
    if winner_row in ["X", "O"]:
        messagebox.showinfo("Message", winner_row + " wins")
        reset()
        return True
    winner_col = check_cols()
    if winner_col in ["X", "O"]:
        messagebox.showinfo("Message", winner_col + " wins")
        reset()
        return True
    winner_diag = check_diags()
    if winner_diag in ["X", "O"]:
        messagebox.showinfo("Message", winner_diag + " wins")
        reset()
        return True
    if turn == 9:
        messagebox.showinfo("Message", "Tie! Lol noobs")
        reset()
        return True
    return False



button_size = 150
button1 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button1_click)
button1.place(x = 75, y = 60, width = button_size, height = button_size)
button2 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button2_click)
button2.place(x = 75+button_size, y = 60, width = button_size, height = button_size)
button3 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button3_click)
button3.place(x = 75+button_size*2, y = 60, width = button_size, height = button_size)
button4 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button4_click)
button4.place(x = 75, y = 60+button_size, width = button_size, height = button_size)
button5 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button5_click)
button5.place(x = 75+button_size, y = 60+button_size, width = button_size, height = button_size)
button6 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button6_click)
button6.place(x = 75+button_size*2, y = 60+button_size, width = button_size, height = button_size)
button7 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button7_click)
button7.place(x = 75, y = 60+button_size*2, width = button_size, height = button_size)
button8 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button8_click)
button9 = tk.Button(fg = "blue", activebackground = "white", activeforeground = "blue", disabledforeground = "blue", command = button9_click)
button8.place(x = 75+button_size, y = 60+button_size*2, width = button_size, height = button_size)
button9.place(x = 75+button_size*2, y = 60+button_size*2, width = button_size, height = button_size)
