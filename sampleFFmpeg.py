import ffmpeg

stream = ffmpeg.input('bird.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream,'output.mp4')
ffmpeg.run(stream)