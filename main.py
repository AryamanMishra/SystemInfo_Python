import tkinter as tk
from tkinter import ttk

import script

window = tk.Tk()

window.title('System Information')
window.geometry("700x500")
window.configure(bg='black')

print(script.getGeneralInfo())
main_button = tk.Button(
    text="Get Your System Specifications !!",
    width=26,
    height=3,
    font='Georgia',
    fg="Black",
    bg='Yellow',
    bd=10
)

main_button.pack()
main_button.place(relx=0.5, rely=0.5, anchor='center')
window.mainloop()