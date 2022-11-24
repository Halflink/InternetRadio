# importing time and vlc
import time, vlc


# method to play video
def radio(source):
    # creating a vlc instance
    vlc_instance = vlc.Instance()

    # creating a media player
    player = vlc_instance.media_player_new()

    # creating a media
    media = vlc_instance.media_new(source)

    # setting media to the player
    player.set_media(media)

    # play the video
    player.play()

    # wait time
    time.sleep(10)

    # getting the duration of the video
    duration = player.get_length()

    # printing the duration of the video
    print("Duration : " + str(duration))


# call the video method
radio("http://playerservices.streamtheworld.com/api/livestream-redirect/KINKK.mp3")
