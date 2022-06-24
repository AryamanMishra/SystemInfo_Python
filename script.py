import json
import math,os
import platform,socket,psutil
from textwrap import indent
import wmi



general_info = {}
disk_info = {}
memory_info = {}
network_info = {}
user_info = {}
versions_info = {}
environment_info = {}
cpu_info = {}
# sensors_info = {}
gpu_info = {}




def formulate(memB):
    
    memKB = memB/1024
    memMB = memKB/1024
    memGB = memMB/1024

    memGB = math.floor(memGB)
    memMB = math.floor(memMB)
    memKB = math.floor(memKB)

    memMB = memMB % 1024
    memKB = memKB % 1024
    memB =  memB % 1024
    
    return str(memGB) + 'GB ' + str(memMB) + 'MB ' + str(memKB) + 'KB ' + str(memB) + 'B '
    

      
def filledDiskStats(drive):
    
    disk_stats = psutil.disk_usage(str(drive))
    disk_info['Total space in ' + str(drive) + ' drive'] = formulate(disk_stats.total)
    disk_info['Used space in ' + str(drive) + ' drive'] = formulate(disk_stats.used)
    disk_info['Free space in ' + str(drive) + ' drive'] = formulate(disk_stats.free)
 


def getGeneralInfo():
    
    general_info['System Name'] = platform.node()
    general_info['Version'] = platform.version()
    general_info['Platform'] = platform.platform()
    general_info['Machine Type'] = platform.machine()
    general_info['Architecture'] = str(platform.architecture()[0]) + ' ' + str(platform.architecture()[1])
    general_info['Processor'] = platform.processor()
    general_info['System'] = platform.system()
    general_info['System Release'] = platform.release()
    return general_info    



def getDiskInfo():
    partitions = psutil.disk_partitions()
    for p in partitions:
        if p.opts != 'cdrom':
            filledDiskStats(str(p.device[:-1]))
    return disk_info




def getNetworkInfo():
    
    network_info['IP address']=socket.gethostbyname(socket.gethostname())
    return network_info
   
   
    
def getMemoryInfo():
    
    memory_stats = psutil.virtual_memory()
    memory_info['Total Memory'] = formulate(memory_stats.total)
    memory_info['Available Memory'] = formulate(memory_stats.available)
    memory_info['Used Memory'] = formulate(memory_stats.used)
    return memory_info
   


def getUserInfo():
    
    user_stats = psutil.users()
    user_info['User name'] = user_stats[0].name
    return user_info




def getVersionsInfo(): 
    versions_info['Python Version: '] = platform.python_version()
    return versions_info



def getEnvironmentInfo():
    for key,value in os.environ.items():
        environment_info[key] = value
    return environment_info



def getCpuInfo():
    cpu_info['CPU count'] = psutil.cpu_count()
    cpu_info['Current Frequency'] = str(psutil.cpu_freq().current) + 'GHz'
    cpu_info['Min Frequency'] = str(psutil.cpu_freq().min) + 'GHz'
    cpu_info['Max Frequency'] = str(psutil.cpu_freq().max) + 'GHz'
    return cpu_info

# print(psutil.disk_partitions())

# def getSensorsInfo():
#     sensors_info['Fans'] = psutil.sen
#     print(sensors_info)



def getGPUInfo():
    pc = wmi.WMI()
    gpu = pc.Win32_VideoController()[0]
    gpu_info['Name'] = gpu.Caption
    gpu_info['Manufacturer'] = gpu.AdapterCompatibility
    gpu_info['Current Refresh Rate'] = str(gpu.CurrentRefreshRate) + 'Hz'
    gpu_info['Max Refresh Rate'] = str(gpu.MaxRefreshRate) + 'Hz'
    gpu_info['Min Refresh Rate'] = str(gpu.MinRefreshRate) + 'Hz'
    gpu_info['Video Mode'] = gpu.VideoModeDescription
    gpu_info['RAM'] = formulate(gpu.AdapterRAM)
    gpu_info['Status'] = gpu.Status
    return gpu_info
    



whole_data = {}
whole_data['General Information'] = getGeneralInfo()
whole_data['CPU Information'] = getCpuInfo()
whole_data['GPU Information'] = getGPUInfo()
whole_data['Disk Information'] = getDiskInfo()
whole_data['Memory Information'] = getMemoryInfo()
whole_data['Network Information'] = getNetworkInfo()
whole_data['Users Information'] = getUserInfo()
whole_data['Versions Information'] = getVersionsInfo()
whole_data['Environment Variables'] = getEnvironmentInfo()




def getWholeData():
    whole_data_json = json.dumps(whole_data, indent=4)
    return whole_data_json
