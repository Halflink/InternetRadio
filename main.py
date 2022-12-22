#!/usr/bin/python
#
#
# https://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3

class Main:

    from JsonHandler import JsonHandler
    from LcdMessageHandler import LcdMessageHandler
    from RotaryEncoder import RotaryEncoder
    from time import sleep
    from timer import Timer

    def __init__(self):

        jsonHandler = self.JsonHandler()
        self.lcdMessageHandler = self.LcdMessageHandler(lcd_address=jsonHandler.lcd_settings_address,
                                                        lcd_width=jsonHandler.lcd_settings_width,
                                                        lcd_lines=jsonHandler.lcd_settings_lines)

        self.url_list = jsonHandler.url_list
        self.current_url = 0
        self.set_station(self.current_url)
        self.timer = self.Timer()
        self.state_play = 'PLAY'
        self.state_select = 'SELECT'
        self.state = self.state_play
        self.set_lcd()

        self.playListRotary = self.RotaryEncoder(clk_GPIO=jsonHandler.url_rotary_settings_clk_gpio,
                                                 dt_GPIO=jsonHandler.url_rotary_settings_dt_gpio,
                                                 switch_GPIO=jsonHandler.url_rotary_settings_switch_gpio,
                                                 min_counter=0, max_counter=len(self.url_list)-1,
                                                 back_to_front=True, call_back=self.test)

    def get_station_name(self, no):
        if no < 0:
            index = self.playListRotary.max_counter
        elif no > self.playListRotary.max_counter:
            index = 0
        else:
            index = no
        return self.url_list[index]['station']

    def is_state_play(self):
        if self.state == self.state_play:
            return True
        else:
            return False

    def is_state_select(self):
        if self.state == self.state_select:
            return True
        else:
            return False

    def set_lcd(self):
        self.lcdMessageHandler.clock()
        self.lcdMessageHandler.display_line()

    def set_station(self, station_no):
        self.current_url = station_no
        self.lcdMessageHandler.set_current_message(self.url_list[self.current_url]['station'])

    def set_state_play(self):
        self.state = self.state_play

    def set_state_select(self):
        self.state = self.state_select

    def test(self):
        self.set_state_select()
        self.timer.start()
        print(self.playListRotary.counter)


if __name__ == '__main__':
    main = Main()
    while True:
        main.sleep(0.1)
        if main.is_state_play():
            main.set_lcd()
        elif main.is_state_select() and main.timer.has_time_elapsed(5):
            main.set_state_play()
        elif main.is_state_select():
            main.lcdMessageHandler.display_selector(main.get_station_name(main.playListRotary.counter),
                                                    main.get_station_name(main.playListRotary.counter+1))
