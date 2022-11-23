import vlc
import time

url = 'http://prem1.rockradio.com:80/bluesrock?9555ae7caa92404c73cade1d'

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(url)

#Set player media
player.set_media(media)

#Play the media
player.play()