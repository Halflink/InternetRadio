# RADIO class
#
# Requisites:
# sudo pip install VNC
#
# tested with:
# http://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3
class Radio:
    import time
    import vlc
    import threading

    def __init__(self):

        # initiate variables
        self.volume = 30
        self.current_url = ""
        self.stop_thread_event = self.threading.Event()

        # creating a vlc instance
        self.vlc_instance = self.vlc.Instance()
        self.player = self.vlc_instance.media_player_new()
        self.player.audio_set_volume(self.volume)

        self.player_thread = self.threading.Thread(target=self.player_thread_function, args=("player thread",
                                                                                             self.stop_thread_event))

    def set_media(self, source):
        # creating a media
        media = self.vlc_instance.media_new(source)

        # setting media to the player
        self.player.set_media(media)

    def play_media(self, url):
        # play the audio
        self.current_url = url

        # in case thread is running, player first needs to stop.
        if self.player_thread.is_alive():
            self.end_player_thread()

        self.set_media(self.current_url)
        self.player.play()
        self.start_player_thread()

    def volume_up(self):
        if self.volume < 100:
            self.volume = self.volume + 1
            self.player.audio_set_volume(self.volume)

    def volume_down(self):
        if self.volume > 1:
            self.volume = self.volume + 1
            self.player.audio_set_volume(self.volume)

    def player_thread_function(self, thread_name, stop_thread_event, ):
        try:
            self.player.play()
            while True:
                self.time.sleep(1)
        except KeyboardInterrupt as e:
            print("Quit")
        except Exception as e:
            print("Quit")
            # self.powerLed.led_set("RED")
            # self.log.exception("Error occurred in sensor thread")
            # self.log.exception(e)

    def end_player_thread(self):
        self.stop_thread_event.set()
        print('Wait for tread to stop...')
        self.player_thread.join()

    def start_player_thread(self):
        self.player_thread.start()


if __name__ == '__main__':
    radio = Radio()
    radio.play_media('http://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3')

    while True:
        print('playing {0} on volume = {1} '.format(radio.current_url, str(radio.volume)))
        radio.time.sleep(30)
        radio.play_media('https://playerservices.streamtheworld.com/api/livestream-redirect/KINK_DNA.mp3')



