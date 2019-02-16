import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter Object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(680,480))

while (cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		frame = cv2.flip(frame,0)
		out.write(frame)

		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()