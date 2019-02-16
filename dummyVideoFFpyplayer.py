# see http://ffmpeg.org/ffmpeg-formats.html#Format-Options for rtbufsize
# lets use the yuv420p, 320x240, 30fps
# 27648000 = 320*240*3 at 30fps, for 4 seconds.
# see http://ffmpeg.org/ffmpeg-devices.html#dshow for video_size, and framerate

from ffpyplayer import *
from ffpyplayer.player import MediaPlayer
import time, weakref

lib_opts = {'framerate':'30', 'video_size':'320x240',
'pixel_format': 'yuv420p', 'rtbufsize':'27648000'}
ff_opts = {'f':'dshow'}
player = MediaPlayer('video=Integrated Webcam:audio=Microphone (Realtek Audio)',
                     ff_opts=ff_opts, lib_opts=lib_opts)

while 1:
    frame, val = player.get_frame()
    if val == 'eof':
        break
    elif frame is None:
        time.sleep(0.01)
    else:
        img, t = frame
        print (val, t, img.get_pixel_format(), img.get_buffer_size())
        time.sleep(val)