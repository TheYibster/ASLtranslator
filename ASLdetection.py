# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os

def predict(frame, signNet):
	img_size = 64
	image = cv2.resize(frame, (img_size, img_size))
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	image = np.asarray(image).reshape((-1, img_size, img_size, 3))

	pred = signNet.predict(image, batch_size=64)

	return pred


signNet = load_model(".\ModelTraining\Model_asl_dense_nospin.model")

# initialize the video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)


	pred = predict(frame, signNet)


	if True:

		label_map = {0: 'A', 1: 'B', 2 : 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16 : 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',25: 'Z', 26: 'del', 27: 'space', 28: 'nothing'}
		if 1 in list(list(pred)[0]):
			label = label_map[list(list(pred)[0]).index(1)]
		else:
			label = "null"

		# display the label and bounding box rectangle on the output
		# frame
		cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 2)
		
	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()