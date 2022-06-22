import script
import tkinter as tk
from tkintertable import TableCanvas, TableModel


def table(info,frame):
    
    data = {}
    if info == 'general':
        head = tk.Label(
            frame,
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
       
        
    # head.pack()
    # tframe = tk.LabelFrame(window)
    # tframe.pack()
   
    table = TableCanvas(frame,rows= len(data),cols=2,read_only=True,height=200,width=420)
    
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