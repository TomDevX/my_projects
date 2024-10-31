from tkinter import messagebox
import tkinter as tk
window = tk.Tk()
window.title("tic-tac-toe")
window.geometry("600x600")

label = tk.Label (window, text = "Welcome to Tic-tac-toe", font = ("Arial", 30), bg = "red", fg = "yellow")
label.place(x=75,y=0)

def button1_click():
    global turn
    button1.config(text = "X", disabledforeground = "red", font = ("Arial", 40), state = "disable")
    if button1 in priority:
        priority.remove(button1)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def button2_click():
    global turn
    button2.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    button2.config(state = "disable")
    if button2 in priority:
        priority.remove(button2)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def button3_click():
    global turn
    button3.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    button3.config(state = "disable")
    if button3 in priority:
        priority.remove(button3)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def button4_click():
    global turn
    button4.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    button4.config(state = "disable")
    if button4 in priority:
        priority.remove(button4)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def button5_click():
    global turn
    button5.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    button5.config(state = "disable")
    if button5 in priority:
        priority.remove(button5)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def button6_click():
    global turn
    button6.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    button6.config(state = "disable")
    if button6 in priority:
        priority.remove(button6)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def button7_click():
    global turn
    button7.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    button7.config(state = "disable")
    if button7 in priority:
        priority.remove(button7)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def button8_click():
    global turn
    button8.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    button8.config(state = "disable")
    if button8 in priority:
        priority.remove(button8)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def button9_click():
    global turn
    button9.config(text = "X", disabledforeground = "red", font = ("Arial", 40))
    button9.config(state = "disable")
    if button9 in priority:
        priority.remove(button9)
    if check_winner() == True:
        return
    CPU()
    if check_winner() == True:
        return
    turn = turn + 1

def check_rows():
    if button1["text"] == button2["text"] == button3["text"]:
        return button1["text"]
    if button4["text"] == button5["text"] == button6["text"]:
        return button4["text"]
    if button7["text"] == button8["text"] == button9["text"]:
        return button7["text"]
    return None

def check_almost_win_rows():
    if button1["text"] == button2["text"] and button3["text"] not in symbol:
       return button3
    if button2["text"] == button3["text"] and button1["text"] not in symbol:
       return button1
    if button1["text"] == button3["text"] and button2["text"] not in symbol:
       return button2

    if button4["text"] == button5["text"] and button6["text"] not in symbol:
       return button6
    if button5["text"] == button6["text"] and button4["text"] not in symbol:
       return button4
    if button4["text"] == button6["text"] and button5["text"] not in symbol:
       return button5

    if button7["text"] == button8["text"] and button9["text"] not in symbol:
       return button9
    if button8["text"] == button9["text"] and button7["text"] not in symbol:
       return button7
    if button7["text"] == button9["text"] and button8["text"] not in symbol:
       return button8

def check_cols():
    if button1["text"] == button4["text"] == button7["text"]:
        return button1["text"]
    if button2["text"] == button5["text"] == button8["text"]:
        return button2["text"]
    if button3["text"] == button6["text"] == button9["text"]:
        return button3["text"]
    return None

def check_almost_win_cols():
    if button1["text"] == button4["text"] and button7["text"] not in symbol:
       return button7
    if button4["text"] == button7["text"] and button1["text"] not in symbol:
       return button1
    if button1["text"] == button7["text"] and button4["text"] not in symbol:
       return button4

    if button2["text"] == button5["text"] and button8["text"] not in symbol:
       return button8
    if button5["text"] == button8["text"] and button2["text"] not in symbol:
       return button2
    if button2["text"] == button8["text"] and button5["text"] not in symbol:
       return button5

    if button3["text"] == button6["text"] and button9["text"] not in symbol:
       return button9
    if button6["text"] == button9["text"] and button3["text"] not in symbol:
       return button3
    if button3["text"] == button9["text"] and button6["text"] not in symbol:
       return button6

def check_diags():
    if button1["text"] == button5["text"] == button9["text"]:
        return button1["text"]
    if button3["text"] == button5["text"] == button7["text"]:
        return button3["text"]
    return None

def check_almost_win_diags():
    if button1["text"] == button5["text"] and button9["text"] not in symbol:
       return button9
    if button5["text"] == button9["text"] and button1["text"] not in symbol:
       return button1
    if button1["text"] == button9["text"] and button5["text"] not in symbol:
       return button5

    if button3["text"] == button5["text"] and button7["text"] not in symbol:
       return button7
    if button5["text"] == button7["text"] and button3["text"] not in symbol:
       return button3
    if button3["text"] == button7["text"] and button5["text"] not in symbol:
       return button8

def reset():
    global turn, priority
    turn = 1
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
       button.config(text = "", state = "normal")
    priority = [button5, button1, button3, button7, button9, button2, button4, button6, button8]

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

def CPU():
    global turn, priority
    if turn == 0:
        priority[0].config(text = "O", disabledforeground = "blue", font = ("Arial", 40), state = "disabled")
        priority.pop(0)
    else:
        almost_win = check_almost_win_rows()
        if almost_win is not None:
            almost_win.config(text = "O", disabledforeground = "blue", font = ("Arial", 40), state = "disabled")
            if almost_win in priority:
                priority.remove(almost_win)
            return
        almost_win = check_almost_win_cols()
        if almost_win is not None:
            almost_win.config(text = "O", disabledforeground = "blue", font = ("Arial", 40), state = "disabled")
            if almost_win in priority:
                priority.remove(almost_win)
            return

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

turn = 0
priority = [button5, button1, button3, button7, button9, button2, button4, button6, button8]
symbol = ["X", "O"]

window.mainloop()
