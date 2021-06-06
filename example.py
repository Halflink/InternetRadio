#!/usr/bin/python
#
# Script for Raspberry Pi Internet Radio
#
# Author: Kyle Prier
# Site: http://wwww.youtube.com/meistervision
#
# LCD author : Matt Hawkins
# Site   : http://www.raspberrypi-spy.co.uk/
#
# Rework: Solino C. de Backlight
# Added functionality for Volume UP and DOWN, Shutdown
# Added interrupts for reading buttons
#
# Date   : 26-03-2017
#

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN! We do not want the LCD to send anything to the Pi @ 5v
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V
# 16: LCD Backlight GND (Red, Optional)
# 17: LCD Backlight GND (Green, Optional)
# 18: LCD Backlight GND (Blue, Optional)

# import
import RPi.GPIO as GPIO
import time
import os
import alsaaudio
import LCDLib
import sys

# Create Audio Object
mixer = alsaaudio.Mixer()
mixer.setvolume(50)
currentvol = mixer.getvolume()
currentvol = int(currentvol[0])

# GPIO Setup

# Define GPIO for Radio Controls
NEXT = 8
PREV = 7
VOLUP = 6
VOLDOWN = 5
SHUTDOWN = 13

GPIO.setwarnings(False)  # Mute warnings
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers

GPIO.setup(NEXT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Next Channel button
GPIO.setup(PREV, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Previous Channel button
GPIO.setup(VOLUP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Volume Up
GPIO.setup(VOLDOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Volume Down
GPIO.setup(SHUTDOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Bring OS down

# Initialize display
LCDLib.lcd_init()


# define volume function
def change_volume(volume):
    global currentvol
    if (currentvol <= 100) and (currentvol >= 0):
        LCDLib.lcd_init()
        newVol = currentvol + volume
        mixer.setvolume(newVol)
        currentvol = mixer.getvolume()
        currentvol = int(currentvol[0])
        displayvolume = "Volume: " + str(newVol)
        LCDLib.lcd_display("", 1, displayvolume, 2, "", 1, "", 1)
        time.sleep(2)
        LCDLib.lcd_clear()
        display_current_station()


def display_current_station():
    f = os.popen("mpc current")
    station = ""
    for i in f.readlines():
        station += i
    # Send some text
    LCDLib.lcd_display(station, 1, "", 2, "", 1, "", 1)


def callback_next(channel):
    os.system("mpc next")
    time.sleep(1)
    os.system("mpc play")
    display_current_station()


def callback_prev(channel):
    os.system("mpc prev")
    time.sleep(1)
    os.system("mpc play")
    display_current_station()


def callback_volup(channel):
    change_volume(5)


def callback_voldown(channel):
    change_volume(-5)


def callback_shutdown(channel):
    LCDLib.lcd_display("", 1, "System shutting down!", 2, "", 1, "", 1)
    time.sleep(2)
    GPIO.cleanup()
    os.system("sudo shutdown -H now")
    sys.exit(0)


GPIO.add_event_detect(NEXT, GPIO.RISING, callback=callback_next, bouncetime=300)
GPIO.add_event_detect(PREV, GPIO.RISING, callback=callback_prev, bouncetime=300)
GPIO.add_event_detect(VOLUP, GPIO.RISING, callback=callback_volup, bouncetime=300)
GPIO.add_event_detect(VOLDOWN, GPIO.RISING, callback=callback_voldown, bouncetime=300)
GPIO.add_event_detect(SHUTDOWN, GPIO.RISING, callback=callback_shutdown, bouncetime=300)


# Main program block
def main():
    LCDLib.lcd_display("Raspberry Pi", 2, "Internet Radio", 2, "by", 2, "Solino de Baay", 2)
    time.sleep(4)
    os.system("mpc play")
    while 1:
        LCDLib.lcd_clear()
        display_current_station()
        time.sleep(20)


if __name__ == '__main__':
    main()