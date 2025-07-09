import psutil

def temperature():
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            cpu_temp = float(file.read()) / 1000
    # return (f"CPU Temperature: {cpu_temp}°C")
    return cpu_temp

def diskspace(r):
    def GB(amount):
        return amount/1073741824
    disk = psutil.disk_usage('/')
    if r == 1:
        return f'{round(GB(disk.used), 1)}/{round(GB(disk.total), 1)} GB'
    else: 
         return f'({disk.percent}%)'
    
def cpuLoad():
     return f'{psutil.cpu_percent(interval=1)}%'

def RAM():
    ram = psutil.virtual_memory()
    return ram.percent
if __name__ == "__main__": #Just some stuff for some testing and whatever...
    print(cpuLoad())  