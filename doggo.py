import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True:
	ret, frame = cap.read()
	cv2.imshow("frame", frame)

	if cv2.waitKey(1) == ord('q'):
		break

	if cv2.waitKey(1) == ord("p"):
		cv2.imwrite("rippy.jpg", frame)
		img = cv2.imread("rippy.jpg")
		cv2.imshow("rippy.jpg", img)

cap.release()