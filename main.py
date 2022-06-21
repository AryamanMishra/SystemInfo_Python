import tkinter as tk
from tkintertable import TableCanvas, TableModel


import script



#<-------------------- Window Configuration ----------------------->

window = tk.Tk()
window.title('System Information')
window.geometry("700x500")
window.configure(bg='black')
scrollBar = tk.Scrollbar(window)
scrollBar.pack(side = tk.RIGHT, fill = tk.Y)

#<-------------------- Window Configuration ----------------------->






#<--------------------- Main button --------------------------->

def hide_button(widget):
    widget.pack_forget()
    
main_button = tk.Button(
    text = "Get Your System Specifications !!",
    width = 26,
    height = 3,
    font = ('Georgia',16),
    fg = "Black",
    bg = 'Yellow',
    bd = 10,
    command = lambda:[
        hide_button(main_button),
        table('general'),
        table('cpu'),
        table('gpu'),
        table('disk'),
        table('memory'),
        table('network'),
        table('user'),
        table('versions'),
        table('environment')
    ]
)
main_button.pack(pady=40)



#<--------------------- Main button --------------------------->






#<--------------------- Table --------------------------------->
def table(info):
    
    data = {}
    if info == 'general':
        head = tk.Label(
            text='General Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getGeneralInfo()
        
    elif info == 'cpu':
        head = tk.Label(
            text='CPU Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getCpuInfo()
    
    elif info == 'gpu':
        head = tk.Label(
            text='GPU Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getGPUInfo()
        
    
    elif info == 'disk':
        head = tk.Label(
            text='Disk Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getDiskInfo()
        
    
    elif info == 'memory':
        head = tk.Label(
            text='Memory Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getMemoryInfo()
        
    elif info == 'network':
        head = tk.Label(
            text='Network Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getNetworkInfo()   
     
    elif info == 'user':
        head = tk.Label(
            text='Users Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getUserInfo()
    
    elif info == 'versions':
        head = tk.Label(
            text='Versions Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getVersionsInfo()
    
    elif info == 'environment':
        head = tk.Label(
            text='Environment Information: ',
            font=("Georgia", 16),
            bg="black",
            fg="yellow"
        )
        data = script.getEnvironmentInfo()
       
        
    head.pack()
    tframe = tk.Frame(window)
    tframe.pack()
    table = TableCanvas(tframe,rows= len(data),cols=2,read_only=True,height=200,width=1000)
    i=0
    j=0
    for key,value in data.items():
        table.model.setValueAt(key,i,j)
        j=j+1
        table.model.setValueAt(value,i,j)
        i=i+1
        j=0
    table.show()
    
#<--------------------- Table --------------------------------->  
    
    
    
    
#<--------------------- Main Loop ----------------------------->

window.mainloop()

#<--------------------- Main Loop ----------------------------->