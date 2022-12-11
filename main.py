#!/usr/bin/python
#
#
# https://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3

class Main:

    from JsonHandler import JsonHandler
    from LcdMessageHandler import LcdMessageHandler
    from time import sleep

    def __init__(self):

        jsonHandler = self.JsonHandler()
        self.lcdMessageHandler = self.LcdMessageHandler(lcd_address=jsonHandler.lcd_settings_address,
                                                        lcd_width=jsonHandler.lcd_settings_width,
                                                        lcd_lines=jsonHandler.lcd_settings_lines)

        self.url_list = jsonHandler.url_list
        self.current_url = 0
        self.set_station(self.current_url)
        self.set_lcd()

    def set_lcd(self):
        self.lcdMessageHandler.clock()
        self.lcdMessageHandler.display_line()

    def set_station(self, station_no):
        self.current_url = station_no
        self.lcdMessageHandler.set_current_message(self.url_list[self.current_url]['station'])


if __name__ == '__main__':
    main = Main()
    while True:
        main.sleep(1)
        main.set_lcd()
