# Internet radio
## PROJECT
| Project name:    | Halflink/InternetRadio |
|------------------|------------------------|
| Author:          | Jeroen van Zwam        |
| Date:            | 2022-11-24             |  
| Last update: | 2022-11-24             |
| Project type:    | Raspberry Pi           |
***

## Executable
* Start  

## PROJECT DESCRIPTION

### Scope
- Use VLC to play internetstream
- power button 
- Volume control
- Channel selector
- Show time & volume

### Pi 3 Model B choice
Currently im using the Pi 3 model b, but i'm checking if I can switch to 
a Pi Zero 2 instead

### HIFIBerry AP2

## PI INSTALLATION NOTES
* Connect remotely so we can use the raspberry headless
  * Set up SSH 
  * Set up WIFI
  * Install GIT `sudo apt-get install git`
* HIFIBerry  
  * Enable I2C bus (in Raspberry config)
  * Note the address HIFIBerry uses
  * sudo pip install VNC
* LCD screen
  * Enable I2C bus
  * Note the address the screen uses (make sure its different from the address HiFi Berry uses)


## PARTS LIST*
* 1x Raspberry Pi 3 Model B
* 2x [rotary encoder](https://www.bitsandparts.nl/Rotary-Encoder-Pulsgever-EC11-20mm-p1911600)
* 6x 10K resistors
* 1x [LCD display with I2C interface](https://www.bitsandparts.nl/Display-LCD-HD44780-16x2-wit-op-blauw-met-I2C-interface-p1067338)
* 1x [logic level converter (bi-directional)](https://www.bitsandparts.nl/Logic-Level-Shifter-4-kanaals-bidirectioneel-p100233)

## TO DO LIST

## Progress

### Test set-up

### 3D printing rotary button
![Rotary buttons](/docs/rotaryholder.jpg)
