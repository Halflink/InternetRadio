class LcdMessageHandler:

    from LcdDriver import LcdDriver
    import time
    import datetime

    def __init__(self):
        self.lcd_width = 16
        self.Lcd = self.LcdDriver(lcd_address=0x27, lcd_with=self.lcd_width, lcd_lines=2)
        self.message_start = 0
        self.message_end = 0
        self.current_message = ''

    def clean_up(self):
        self.Lcd.clean_up()

    def clock(self):
        self.Lcd.lcd_string(self.get_datetime(), self.Lcd.LCD_LINE_ADDRESS[0])

    def display_news_ticker(self):
        work_message = self.current_message.ljust(len(self.current_message) + 15, ' ')
        display_message = work_message[self.message_start:self.message_end].rjust(self.lcd_width, ' ')

        # set new range to display
        if self.message_end < len(work_message):
            self.message_end = self.message_end + 1
            if self.message_start < self.message_end - 16:
                self.message_start = self.message_end - 16
        else:
            self.message_start = 0
            self.message_end = 0

        self.Lcd.lcd_string(display_message, self.Lcd.LCD_LINE_ADDRESS[1])

    def get_datetime(self):
        # see https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        current_time = self.datetime.datetime.now()
        time_string = current_time.strftime('%H:%M:%S')
        return time_string

    def set_current_message(self, message):
        self.current_message = message
        self.message_start = 0
        self.message_end = 0


if __name__ == '__main__':
    lcdMessage = LcdMessageHandler()
    bericht = 'http://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3'
    lcdMessage.set_current_message(bericht)
    try:
        while True:
            lcdMessage.clock()
            lcdMessage.display_news_ticker()
            lcdMessage.time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        lcdMessage.clean_up()
