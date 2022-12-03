class LcdMessageHandler:

    from LcdDriver import LcdDriver
    import time
    import datetime

    def __init__(self):
        self.Lcd = self.LcdDriver(lcd_address=0x27, lcd_with=16, lcd_lines=2)

    def get_datetime(self):
        # see https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        current_time = self.datetime.datetime.now()
        time_string = current_time.strftime('%H:%M:%S')
        return time_string

    def clock(self):
        while True:
            self.Lcd.lcd_string(self.get_datetime(), self.Lcd.LCD_LINE_ADDRESS[0])
            self.time.sleep(1)

    def clean_up(self):
        self.Lcd.clean_up()


if __name__ == '__main__':
    lcdMessage = LcdMessageHandler()
    try:
        lcdMessage.clock()
    except KeyboardInterrupt:
        pass
    finally:
        lcdMessage.clean_up()