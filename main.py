import tkinter as tk
from tkintertable import TableCanvas, TableModel

import script
from table import table



#<-------------------- Window Configuration ----------------------->

window = tk.Tk()
window.title('System Information')
window.geometry("700x500")
window.configure(bg='black')


#<-------------------- Window Configuration ----------------------->


# def raise_frame(frame):
#     frame.tkraise()

# def pack_frame(frame):
#     frame.pack()

def hide_widget(widget):
    widget.pack_forget()  
    



    

    

#<--------------------- Main button --------------------------->



def main_button():   
    main_button = tk.Button(
        text = "Get Your System Specifications !!",
        width = 26,
        height = 5,
        font = ('Georgia',16),
        fg = "Black",
        bg = 'Yellow',
        bd = 10,
        command = lambda:[
            hide_widget(main_button),
            table('general', window),
            table('cpu',window),
            table('gpu',window),
        ]
    )
    main_button.pack()

main_button()

#<--------------------- Main button --------------------------->




#<--------------------- Main Loop ----------------------------->

window.mainloop()

#<--------------------- Main Loop ----------------------------->