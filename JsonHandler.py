import json as json


class JsonHandler:

    def __init__(self):

        with open("./init.json") as jsonFile:
            init_info = json.load(jsonFile)
            jsonFile.close()
            hex_s = init_info['lcd settings']['address']
            self.lcd_settings_address = int(hex_s, 16)
            self.lcd_settings_lines = init_info['lcd settings']['lines']
            self.lcd_settings_width = init_info['lcd settings']['width']
            self.url_list = init_info['url list']
            self.url_rotary_settings_clk_gpio = init_info['url rotary settings']['clk gpio']
            self.url_rotary_settings_dt_gpio = init_info['url rotary settings']['dt gpio']
            self.url_rotary_settings_switch_gpio = init_info['url rotary settings']['switch gpio']
            self.volume_rotary_settings_clk_gpio = init_info['volume rotary settings']['clk gpio']
            self.volume_rotary_settings_dt_gpio = init_info['volume rotary settings']['dt gpio']
            self.volume_rotary_settings_switch_gpio = init_info['volume rotary settings']['switch gpio']

    def print_settings(self):
        print("lcd_settings_address: " + hex(self.lcd_settings_address))
        print("lcd_settings_lines: {} ".format(self.lcd_settings_lines))
        print("lcd_settings_width: {} ".format(self.lcd_settings_width))
        no_of_urls = len(self.url_list)
        for element in range(no_of_urls):
            print("Station: {station} URL: {url}".format(station=self.url_list[element]['station'],
                                                         url=self.url_list[element]['url']))


if __name__ == '__main__':
    jsonHandler = JsonHandler()
    jsonHandler.print_settings()
