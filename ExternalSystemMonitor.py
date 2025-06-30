from LCD import LCD
import time
import system

lcd = LCD(2, 0x27, True) #You have to say 2, because this is a different library but it works for 4 row LCDS.

lcd.clear()

while True:
    lcd.message(f'CPU temp: {str(system.temperature())} C', 1)
    lcd.message(f'CPU load: {system.cpuLoad()}', 2)
    lcd.message(f'RAM usage: {str(system.RAM())}%', 3)
    lcd.message(f'Disk: {system.diskspace(1)}', 4)
    time.sleep(1)
