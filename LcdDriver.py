#!/usr/bin/python

class LcdDriver:

    import smbus
    import time
    import datetime

    def __init__(self, lcd_address = 0x27, lcd_with = 16, lcd_lines = 2):

        # Define some device constants
        self.I2C_ADDR = lcd_address # I2C device address
        self.LCD_WIDTH = lcd_with  # Maximum characters per line
        self.LCD_CHR = 1  # Mode - Sending data
        self.LCD_CMD = 0  # Mode - Sending command
        self.LCD_BACKLIGHT = 0x08  # On 0X08 / Off 0x00
        self.ENABLE = 0b00000100  # Enable bit
        self.E_PULSE = 0.0005
        self.E_DELAY = 0.0005
        self.bus = self.smbus.SMBus(1)  # Rev 2 Pi uses 1
        self.lcd_line_address = []

        for i in range(lcd_lines):
            if i == 0:
                self.lcd_line_address.append(0x80)
            elif i == 1:
                self.lcd_line_address.append(0xC0)
            elif i == 2:
                self.lcd_line_address.append(0x94)
            elif i == 3:
                self.lcd_line_address.append(0xD4)

        self.lcd_byte(0x33, self.LCD_CMD)  # 110011 Initialise
        self.lcd_byte(0x32, self.LCD_CMD)  # 110010 Initialise
        self.lcd_byte(0x06, self.LCD_CMD)  # 000110 Cursor move direction
        self.lcd_byte(0x0C, self.LCD_CMD)  # 001100 Display On,Cursor Off, Blink Off
        self.lcd_byte(0x28, self.LCD_CMD)  # 101000 Data length, number of lines, font size
        self.lcd_byte(0x01, self.LCD_CMD)  # 000001 Clear display
        self.time.sleep(self.E_DELAY)

    def lcd_byte(self, bits, mode):

        bits_high = mode | (bits & 0xF0) | self.LCD_BACKLIGHT
        bits_low = mode | ((bits << 4) & 0xF0) | self.LCD_BACKLIGHT

        self.bus.write_byte(self.I2C_ADDR, bits_high)
        self.lcd_toggle_enable(bits_high)

        self.bus.write_byte(self.I2C_ADDR, bits_low)
        self.lcd_toggle_enable(bits_low)

    def lcd_toggle_enable(self, bits):
        self.time.sleep(self.E_DELAY)
        self.bus.write_byte(self.I2C_ADDR, (bits | self.ENABLE))
        self.time.sleep(self.E_PULSE)
        self.bus.write_byte(self.I2C_ADDR, (bits & ~self.ENABLE))
        self.time.sleep(self.E_DELAY)

    def lcd_string(self, message, line):

        message = message.ljust(self.LCD_WIDTH, " ")

        self.lcd_byte(line, self.LCD_CMD)

        for i in range(self.LCD_WIDTH):
            self.lcd_byte(ord(message[i]), self.LCD_CHR)

    def test(self):

        while True:
            now = self.datetime.datetime.now()

            self.lcd_string("WHOOPIE goldberg", self.LCD_LINE_2)
            stringetje = str(now.hour) + ":" + str(now.minute) + " ola"
            self.lcd_string(stringetje, self.LCD_LINE_1)
            print(stringetje)
            self.time.sleep(1)


if __name__ == '__main__':

    lcd = LcdDriver()
    try:
        lcd.test()
    except KeyboardInterrupt:
        pass
    finally:
        lcd.lcd_byte(0x01, lcd.LCD_CMD)
