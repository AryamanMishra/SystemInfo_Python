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
    



# frame1 = tk.Frame(window)
# frame1_a = tk.Frame(window)
# frame1_b = tk.Frame(window)
# frame1_c = tk.Frame(window)
# frame2 = tk.Frame(window)
# frame2_a = tk.Frame(window)
# frame2_b = tk.Frame(window)
# frame2_c = tk.Frame(window)
# frame2_d = tk.Frame(window)
# frame3 = tk.Frame(window)
# frame3_a = tk.Frame(window)
# frame3_b = tk.Frame(window)
# frame3_d = tk.Frame(window)

# # for frame in (frame1,frame1_a, frame1_b,frame1_c,frame2_a,frame2_b,frame3,frame3_b):
# #     frame.grid(row=0, column=0, sticky='news')



# def showPrevButton(frame):
#     prev_button = tk.Button(
#         frame,
#         text="Previous Page", 
#         command=lambda:[
#             hide_widget(frame2),
#             hide_widget(frame2_a),
#             hide_widget(frame2_b),
#             hide_widget(frame2_c),
#             hide_widget(frame2_d),
#             table('general', frame1),
#             pack_frame(frame1),
#             raise_frame(frame1),
            
#             raise_frame(frame1_a),
#             raise_frame(frame1_b),
#             raise_frame(frame1_c)
#         ],
#         font = ('Georgia',16),
#         fg = "Black",
#         bg = 'Yellow',
#     )
#     prev_button.pack()    
    


# def showNextButton(frame):
#     next_button = tk.Button(
#         frame,
#         text="Next Page", 
#         command=lambda:[
#             hide_widget(frame1),
#             hide_widget(frame1_a),
#             hide_widget(frame1_b),
#             hide_widget(frame1_c),
#             table('disk', frame2),
#             pack_frame(frame2),
#             raise_frame(frame2),
#             table('memory', frame2_a),
#             pack_frame(frame2_a),
#             raise_frame(frame2_a),
#             table('network', frame2_b),
#             pack_frame(frame2_b),
#             raise_frame(frame2_b),
#             showNextButton2(frame2_c),
#             pack_frame(frame2_c),
#             showPrevButton(frame2_d),
#             pack_frame(frame2_d)
#         ],
#         font = ('Georgia',16),
#         fg = "Black",
#         bg = 'Yellow',
#     )
#     next_button.pack()
    
    

# def showNextButton2(frame):
#     next_button = tk.Button(
#         frame,
#         text="Next Page", 
#         command=lambda:[
#             hide_widget(frame2),
#             hide_widget(frame2_a),
#             hide_widget(frame2_b),
#             hide_widget(frame2_c),
#             hide_widget(frame2_d),
#             table('user', frame3),
#             pack_frame(frame3),
#             raise_frame(frame3),
#             table('versions', frame3_a),
#             pack_frame(frame3_a),
#             raise_frame(frame3_a),
#             table('environment', frame3_b),
#             pack_frame(frame3_b),
#             raise_frame(frame3_b),
#         ],
#         font = ('Georgia',16),
#         fg = "Black",
#         bg = 'Yellow',
#     )
#     next_button.pack()    
    
    
    
    
    

    

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