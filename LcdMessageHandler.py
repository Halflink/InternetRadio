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

    def cap_string(input, size):

        if len(input) > size:
            input = input[0:size]

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

    def display_selector(self, current_option, next_option):
        display_line_0 = '>' + current_option.ljust(self.lcd_width-2, ' ')[0:13] + '<'
        display_line_1 = ' ' + next_option.ljust(self.lcd_width - 2, ' ')[0:13] + ' '
        self.Lcd.lcd_string(display_line_0, self.Lcd.LCD_LINE_ADDRESS[0])
        self.Lcd.lcd_string(display_line_1, self.Lcd.LCD_LINE_ADDRESS[1])

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
    berichten = ['Today - The Smashing Pumpkins', 'Enter The Sandman - Metallica',
                 'Black Hole Sun - Soundgarden', 'No Rain - Blind Melon']
    i = 0
    try:
        while True:
            k = i + 1
            if k > len(berichten)-1:
                k = 0
            lcdMessage.display_selector(berichten[i], berichten[k])
            i = i + 1
            if i > len(berichten)-1:
                i = 0

    except KeyboardInterrupt:
        pass
    finally:
        lcdMessage.clean_up()
