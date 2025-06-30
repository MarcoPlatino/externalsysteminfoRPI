import time
from LCD import LCD

lcd = LCD(2, 0x27, True)

lcd.message("Marco", 3)
lcd.message("Says hello", 2)

time.sleep(5)

lcd.clear()
