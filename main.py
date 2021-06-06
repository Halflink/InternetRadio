#!/usr/bin/python
#
# Requisites
# updated/installed MPC / MPD: sudo apt-get install mpd mpc
# Installed pyalsaaudio: sudo pip3 install pyalsaaudio
# added snd_bcm2835 to /etc/modules to boot sound
#
# tested with:
# https://playerservices.streamtheworld.com/api/livestream-redirect/KINK.mp3

class MainRadio:

    # import
    import os
    import alsaaudio as alsaaudio
    import sys

    #def __init__(self):
    #    mixer = self.alsaaudio.Mixer('HDMI')
    #    mixer.setvolume(50)
    #    currentvol = mixer.getvolume()
    #    currentvol = int(currentvol[0])

    def get_devices(self):
        for device in self.alsaaudio.pcms('PCM_PLAYBACK'):
            print("Device:", device)


if __name__ == '__main__':
    mainRadio = MainRadio()
    mainRadio.get_devices()
