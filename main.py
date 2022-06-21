import tkinter as tk
from tkinter import ttk


import script

window = tk.Tk()

window.title('System Information')
window.geometry("700x500")
window.configure(bg='black')








def hide_button(widget):
    widget.pack_forget()
    

main_button = tk.Button(
    text="Get Your System Specifications !!",
    width=26,
    height=3,
    font='Georgia',
    fg="Black",
    bg='Yellow',
    bd=10,
    command=lambda:[hide_button(main_button)]
)

main_button.pack(pady=40)
main_button.pack()
window.mainloop()