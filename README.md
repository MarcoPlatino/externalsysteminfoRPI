# External System Information for Raspberry Pi 5
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Last Commit](https://img.shields.io/github/last-commit/MarcoPlatino/externalsysteminfoRPI)
![Issues](https://img.shields.io/github/issues/MarcoPlatino/externalsysteminfoRPI)

This is an external system information display for the Raspberry Pi 5. I took inspiration from Conky, and Conky Rings, and thought noticed how convenient it was to have that kind of information, but the one drawback to Conky is that it is only on the homescreen -- This becomes one of your peripherals and is always active.

---
## Table of Contents
- [Features](#features)
- [Requirements](#stuff-you-will-need)
- [Setup](#setup)
- [Common Issues](#common-issues)
- [Stand](#stand)
- [License](#license)
- [Acknowledgments](#acknowledgments)
---
## Features:
The display shows the following:
- CPU temperature (in degrees Celcius)
- CPU load (in percent)
- RAM usage (as a percentage)
- Disk Space (As a fraction showing the current used space versus the total space)
---

## Stuff you will need:
### Hardware
  1. You need 4 female-to-female jumper wires to wire the LCD to the Pi
  2. A Raspberry Pi (I have only tested this on the pi5)
  3. An LCD screen. I used [this one](https://www.amazon.com/GeeekPi-Interface-Backlight-Raspberry-Electrical/dp/B0BCWJWKG2/141-8914070-5124150?pd_rd_w=aiDfA&content-id=amzn1.sym.751acc83-5c05-42d0-a15e-303622651e1e&pf_rd_p=751acc83-5c05-42d0-a15e-303622651e1e&pf_rd_r=FDYZRA57ETS49SXH0ZRA&pd_rd_wg=FOuh7&pd_rd_r=ce61adae-9817-4b25-9350-e5aa9f382d58&pd_rd_i=B0BCWJWKG2&psc=1)
  
  OPTIONAL THINGS (that will improve your experience):
  1. A 3D printer
  2. Filament (I used BambuLab Matte PLA)
  3. 4 (or 2) M3 screws.

### Python Requirements
Install all of the dependencies by just running this command:

`pip install -r requirements.txt`


> [!Tip]
> Depending on how you have your Pi configured, it may request that you create a .venv


If you already have all of the necessary stuff to run your pi and everything in the list, you should be set!

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
Start by cloning the repository onto your machine, and configuring the `externalsystemdisplay.sh` file to direct the python run command to the location of your `ExternalSystemMonitor.py` file. 
It will look something like this:
```
#!/bin/bash
sleep 20
python /home/(username)/externalsysteminfoRPI/ExternalSystemMonitor.py
```
You should replace the `(username)` with your actual username and modify it to actually be the location of the file. If you have cloned it properly, all the libraries will be configured correctly.

Once you have done that, make the file executable by running this command:

`sudo chmod +x externalsystemdisplay.sh`

This will allow the file to run.

> [!NOTE]
> It is probably a good idea to just run `ExternalSystemMonitor.py` file to be sure that you have everything wired correctly and it works...

### Configuring it to run on start
This code was testing by addind it to the crontab file. Here is the steplist to follow:
- Start by opening a terminal
- Type `crontab -e`.
You will be presented with a menu asking what editor you would like to open the file with. I *highly* recomend opening it with nano because it is the easiest option (As indicated on the menu).

Once you have it open, it should look something like this:
![20250703_19h24m52s_grim](https://github.com/user-attachments/assets/3ee27baa-2f42-4c40-9d6f-1027a9985dcd)

You are going to have to scroll all the way down to the end of the comments and add this line:
`@reboot /home/(your name)/externalsystemdisplay.sh`
You should replace `(your name)` with the actual name of the account on the pi. If you do not move the `externalsystemdisplay.sh` file to the home directory on your pi, you may have to modify the command to reflect that.

Once you are done you should press `CTRL + X` to exit and confirm any requests to save your changes.

### Finishing Up
If you have followed the instructions correctly, you should be able to reboot your pi (by running `sudo reboot`) or rebooting it from the power menu, and the program should successfully boot and update the LCD once a second with your system information. 

---
## Common Issues
### *"I configured everything correctly, but it does not turn on when I boot the pi!"*
If when you ran the `ExternalSystemMonitor.py` file, it did work, then there is likely a very simple fix. What is probably happening is that the program is trying to run before the i2c protocol is activated on your pi. What you should do is open `externalsystemdisplay.sh` and increase the value of the line that has `sleep 20` to a larger number. This means that the pi will not run the program until later, and by that point, the i2c protocol will have been turned on already.

If you have any other issues than these submit an issue I guess...

---
## Stand
You can find the `3mf` files in the 3D files folder. They have some settings modified that I think will improve the print quality, such as enabling supports, and also adding a brim. On my Bambu Labs H2D, it prints in about 2.5 hours using the 0.2 mm layer height. 

### Assembly
> [!Important]
> When assembling the stand, I *highly* recomend first attaching all of your jumper wires to the LCD screen, passing them through the hole, screwing everything in, and only then connect > them to the pi. If you do not do that, you will have a very tough time. 

To attach the screen to the stand, you will need 4 M3 screws. Just use the holes on the back of the stand to pass the screwdriver in.

### Photos
![462935674-c68daf85-abc6-4d0c-8a1c-371d4e4fbe4b](https://github.com/user-attachments/assets/71c4c71f-c36b-4e7a-9762-9473f3c86634)
![IMG_20250706_113348169_HDR](https://github.com/user-attachments/assets/6ba8c85c-82ec-407c-a361-bb7def9c9d89)
![ahaphtot](https://github.com/user-attachments/assets/2eee3f99-adee-4e8d-81c4-42f2bd3c6792)



---
## License

MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

Portions of this project are adapted from [rpi-lcd](https://github.com/bogdal/rpi-lcd) by Adam Bogdał, used under the MIT License.
