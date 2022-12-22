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
    from radio import Radio

    def __init__(self):

        jsonHandler = self.JsonHandler()

        # Set up url list
        self.url_list = jsonHandler.url_list
        self.current_url_no = 0

        # set up LCD
        self.lcdMessageHandler = self.LcdMessageHandler(lcd_address=jsonHandler.lcd_settings_address,
                                                        lcd_width=jsonHandler.lcd_settings_width,
                                                        lcd_lines=jsonHandler.lcd_settings_lines)

        # LCD can have the following states: PLAY, showing the time and current radio station, and SELECT, showing
        # current selection on line 1 and the next on line 2. switching from one to the other state happens when you use
        # the rotary switch. If you do no use the rotary switch for 5 seconds, it switches back. The timer class is used
        # for that.
        self.timer = self.Timer()
        self.lcd_state_play = 'PLAY'
        self.lcd_state_select = 'SELECT'
        self.lcd_state = self.lcd_state_play

        # set up rotary: url selector
        self.playListRotary = self.RotaryEncoder(clk_GPIO=jsonHandler.url_rotary_settings_clk_gpio,
                                                 dt_GPIO=jsonHandler.url_rotary_settings_dt_gpio,
                                                 switch_GPIO=jsonHandler.url_rotary_settings_switch_gpio,
                                                 min_counter=0, max_counter=len(self.url_list)-1,
                                                 back_to_front=True, call_back=self.run_selector,
                                                 call_back_switch=self.set_select)

        # set up rotary: volume control
        self.volumeRotary = self.RotaryEncoder(clk_GPIO=jsonHandler.volume_rotary_settings_clk_gpio,
                                               dt_GPIO=jsonHandler.volume_rotary_settings_dt_gpio,
                                               switch_GPIO=jsonHandler.volume_rotary_settings_switch_gpio,
                                               min_counter=0, max_counter=99,
                                               back_to_front=False, call_back=self.run_volume_select,
                                               call_back_switch=self.toggle_mute)

        # set up radio
        self.radio = self.Radio()
        self.set_station(self.current_url_no)
        self.set_lcd()

    def get_station_name(self, no):
        if no < 0:
            index = self.playListRotary.max_counter
        elif no > self.playListRotary.max_counter:
            index = 0
        else:
            index = no
        return self.url_list[index]['station']

    def is_lcd_state_play(self):
        if self.lcd_state == self.lcd_state_play:
            return True
        else:
            return False

    def is_lcd_state_select(self):
        if self.lcd_state == self.lcd_state_select:
            return True
        else:
            return False

    def run_radio(self):
        while True:
            self.sleep(0.1)
            if self.is_lcd_state_play():
                self.set_lcd()
            elif self.is_lcd_state_select() and self.timer.has_time_elapsed(5):
                self.playListRotary.counter = self.current_url_no
                self.set_lcd_state_play()
            elif self.is_lcd_state_select():
                self.lcdMessageHandler.display_selector(self.get_station_name(self.playListRotary.counter),
                                                        self.get_station_name(self.playListRotary.counter + 1))

    def run_selector(self):
        self.set_lcd_state_select()
        self.timer.start()

    def run_volume_select(self):
        self.radio.set_volume(self.volumeRotary.counter)

    def set_lcd(self):
        self.lcdMessageHandler.clock_volume(self.radio.volume)
        self.lcdMessageHandler.display_line()

    def set_station(self, station_no):
        self.current_url_no = station_no
        self.lcdMessageHandler.set_current_message(self.url_list[self.current_url_no]['station'])
        self.radio.play_media(self.url_list[self.current_url_no]['url'])

    def set_lcd_state_play(self):
        self.lcd_state = self.lcd_state_play

    def set_lcd_state_select(self):
        self.lcd_state = self.lcd_state_select

    def set_select(self, counter):
        self.current_url_no = counter
        self.set_station(self.current_url_no)

    def toggle_mute(self, counter):
        self.radio.toggle_mute()


if __name__ == '__main__':
    main = Main()
    main.run_radio()
