#<------------------- Import required libraries ------------------->

import tkinter as tk
from tkinter import font
from tkinter.ttk import LabelFrame
from tkintertable import TableCanvas, TableModel

import script
from table import table

#<------------------- Import required libraries ------------------->





#<-------------------- tkinter Window Configuration ----------------------->

window = tk.Tk()
window.title('System Information')
window.geometry("700x500")
window.configure(bg='black')


#<-------------------- tkinter Window Configuration ----------------------->






#<--------------- Hide Widget Method for hiding widgets ------------------->

def hide_widget(widget):
    widget.pack_forget()  
    
#<--------------- Hide Widget Method for hiding widgets ------------------->



#<------------------- Initialised frames ---------------------------------->

frame1 = LabelFrame(window, text='General Information')
frame2 = LabelFrame(window, text='CPU Information')
frame3 = LabelFrame(window, text='GPU Information')
frame4 = LabelFrame(window, text='Disk Information')
frame5 = LabelFrame(window, text='Memory Information')
frame6 = LabelFrame(window, text='Network Information')
frame7 = LabelFrame(window, text='User Information')
frame8 = LabelFrame(window, text='Versions Information')
frame9 = LabelFrame(window, text='Environment Information')

#<------------------- Initialised frames ---------------------------------->

    




#<--------------------- Main button --------------------------->


def main_button():   
    main_button = tk.Button(
        text = "View System Specifications !!",
        width = 26,
        height = 5,
        font = ('Georgia',16),
        fg = "Black",
        bg = 'Yellow',
        bd = 10,
        command = lambda:[
            hide_widget(main_button),
            table('general', frame1),
            frame1.grid(row=0,column=0),
            table('cpu', frame2),
            frame2.grid(row=0,column=1),
            table('gpu', frame3),
            frame3.grid(row=0,column=2),
            table('disk', frame4),
            frame4.grid(row=1,column=0),
            table('memory', frame5),
            frame5.grid(row=1,column=1),
            table('network', frame6),
            frame6.grid(row=1,column=2),
            table('user', frame7),
            frame7.grid(row=2,column=0),
            table('versions', frame8),
            frame8.grid(row=2,column=1),
            table('environment', frame9),
            frame9.grid(row=2,column=2)
        ]
    )
    main_button.pack()

main_button()

#<--------------------- Main button --------------------------->




#<--------------------- Main Loop ----------------------------->

window.mainloop()

#<--------------------- Main Loop ----------------------------->