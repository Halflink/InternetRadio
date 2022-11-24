# RADIO class
#
# Requisites:
# sudo pip install VNC
#
# tested with:
# http://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3
class Radio:

    import time
    import vnc

    def __init__(self):

        # initiate variables
        self.volume = 20
        self.current_url = ""

        # creating a vlc instance
        self.vlc_instance = self.vlc.Instance()
        self.player = self.vlc_instance.media_player_new()

    def set_media(self, source):
        # creating a media
        media = self.vlc_instance.media_new(source)

        # setting media to the player
        self.player.set_media(media)

    def play_media(self):
        # play the audio
        self.player.play()

        # wait time
        self.time.sleep(100)


if __name__ == '__main__':
    radio = Radio()
    radio.set_media('http://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3')
    radio.play_media()