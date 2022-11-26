#!/usr/bin/python

import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
import time


# import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
# lcd_rs = 25
# lcd_en = 24
# lcd_d4 = 23
# lcd_d5 = 17
# lcd_d6 = 18
# lcd_d7 = 22
# lcd_backlight = 1

# Define LCD column and row size for 16x2 LCD.
# lcd_columns = 16
# lcd_rows    = 2

# Initialize the LCD using the pins above.
# lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
#                           lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
# print('probeer ')
# lcd.message('Hello!\nraspberrytips.nl')

lcd_rs = digitalio.DigitalInOut(board.D25)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d7 = digitalio.DigitalInOut(board.D22)
lcd_backlight = digitalio.DigitalInOut(board.D9)

lcd_columns = 16
lcd_rows = 2

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows,
                                       lcd_backlight)


print('probeer')
lcd.backlight = True
lcd.message = "Hello\nCircuitPython"

scroll_message = "Eens kijken hoe scrollen werkt"

while True:
    lcd.backlight = True
    lcd.message = scroll_message
    time.sleep(2)
    for i in range(len(scroll_message)):
        lcd.move_left()
        time.sleep(0.5)
    time.sleep(2)
    lcd.clear()
    lcd.backlight = False
    time.sleep(2)