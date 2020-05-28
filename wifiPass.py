# snippet to extract passwords for saved wifi profiles
import subprocess
import tkinter as tk


def getPasswords():
    pass


# ------------- GUI -------------------
win = tk.Tk()
win.title('Wifi Passwords')

label = tk.Label(win, text='Click start to get your saved wifi passes')
label.grid(row=0, column=0, pady=5)

button = tk.Button(
    win, text='Show saved Passwords for Wifis', command=getPasswords)
button.grid(row=0, column=1, pady=5)

data = tk.Text(win, height=40, width=100)
data.grid(row=1, column=0, columnspan=2)

labelFooter = tk.Label(
    win, text='Sample non official Copy- Under dev version majid.shockoohi@gmail.com')
labelFooter.grid(row=2, column=0, columnspan=2, padx=10, pady=1)

win.mainloop()
