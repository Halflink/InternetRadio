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
        self.volume = 20
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

    def play_media(self):
        # play the audio
        self.player.play()

    def volume_up(self):
        audio_set_volume(50)

    def player_thread_function(self, thread_name, stop_thread_event, ):
        try:
            self.play_media()
            while True:
                pass
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
    radio.set_media('http://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3')
    radio.start_player_thread()
    while True:
        print("playing")
        radio.time.sleep(10)
