import script
import tkinter as tk
from tkintertable import TableCanvas, TableModel


def table(info,frame):
    
    data = {}
    if info == 'general':
        data = script.getGeneralInfo()
        
    elif info == 'cpu':
        data = script.getCpuInfo()
    
    elif info == 'gpu':
        data = script.getGPUInfo()
        
    
    elif info == 'disk':
        data = script.getDiskInfo()
            
    elif info == 'memory':
        data = script.getMemoryInfo()
        
    elif info == 'network':
        data = script.getNetworkInfo()   
     
    elif info == 'user':
        data = script.getUserInfo()
    
    elif info == 'versions':
        data = script.getVersionsInfo()
    
    elif info == 'environment':
        data = script.getEnvironmentInfo()
       
        
    # head.pack()
    # tframe = tk.LabelFrame(window)
    # tframe.pack()
   
    table = TableCanvas(frame,rows= len(data),cols=2,read_only=True,height=210,width=410)
    
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