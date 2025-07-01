# External System Information for Raspberry Pi 5
This is an external system information display for the Raspberry Pi 5. I took inspiration from Conky, and Conky Rings, and thought noticed how convenient it was to have that kind of information, but the one drawback to Conky is that it is only on the homescreen -- This becomes one of your peripherals and is always active.

---
## Setup:
### i2c
First of all, you have to make sure that you have the i2c interface on your pi enabled correctly. You have to first go to the main menu, going to preferences, and then clicking on Raspberry Pi Configuration.
![20250630_17h52m55s_grim](https://github.com/user-attachments/assets/cc184b76-221e-4f67-a1a0-6f18fe17f528)

Then, click on the Interfaces tab, and enable i2c!
![20250630_17h53m05s_grim](https://github.com/user-attachments/assets/ec01cef7-98cd-4863-a37a-0a141431b74c)

### Wiring the LCD to the Pi
Follow this very convenient wiring chart that I have made:
![RPI_LCD_connections_bb](https://github.com/user-attachments/assets/ff390d91-f48f-4f4b-8de8-7ec5ee3dde17)

Make sure that you have 4 female-to-female connectors so that you can wire everything together properly. If you did it right and your pi is powered on, the screen should light up. There may be a potentiometer on the back that you will have to adjust for contrast. You won't really be able to tell how it needs to be adjusted until you actually have the program running, so leave that alone for now...

### Setting up the code
Start by cloning the repository onto your machine, and configuring the `externalsystemdisplay.sh` file to direct the python run command to the location of your `externalsystemmonitor.py` file. 
It will look something like this:
```
#!/bin/bash
sleep 20
python /home/(username)/externalsysteminfoRPI/ExternalSystemMonitor.py
```
You should replace the `(username)` with your actual username and modify it to actually be the location of the file. If you have cloned it properly, all the libraries will be configured correctly.

### Configuring it to run on start
Nothing here for now...

---
