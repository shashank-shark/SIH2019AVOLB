import cv2
import numpy as np

from ffpyplayer.player import MediaPlayer

cap = cv2.VideoCapture(0)

while True:
	grabbed, frame = cap.read()
	audio_frame, val = player.get_frame()

	if not grabbed:
		print ("End of video")
		break
	if cv2.waitKey(28) & 0xFF == ord('q'):
		break

	cv2.imshow("video", frame)

	if val != 'eof' and audio_frame is not None:
		img, t = audio_frame

video.release()
cv2.destroyAllWindows()
