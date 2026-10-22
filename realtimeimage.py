
import cv2
import numpy as np
from datetime import datetime

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found")
    exit()

cv2.namedWindow("Color Filter")

cv2.createTrackbar("Blue", "Color Filter", 100, 200, lambda x: None)
cv2.createTrackbar("Green", "Color Filter", 100, 200, lambda x: None)
cv2.createTrackbar("Red", "Color Filter", 100, 200, lambda x: None)

filter_type = "normal"

while True:
    ret, frame = camera.read()

    if not ret:
        print("Cannot read camera")
        break

    blue = cv2.getTrackbarPos("Blue", "Color Filter") / 100
    green = cv2.getTrackbarPos("Green", "Color Filter") / 100
    red = cv2.getTrackbarPos("Red", "Color Filter") / 100

    filtered = frame.copy()

    if filter_type == "gray":
        filtered = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)

    elif filter_type == "warm":
        filtered[:, :, 2] = np.clip(frame[:, :, 2] * 1.4, 0, 255)
        filtered[:, :, 0] = np.clip(frame[:, :, 0] * 0.7, 0, 255)

    elif filter_type == "cool":
        filtered[:, :, 0] = np.clip(frame[:, :, 0] * 1.4, 0, 255)
        filtered[:, :, 2] = np.clip(frame[:, :, 2] * 0.7, 0, 255)

    else:
        filtered[:, :, 0] = np.clip(frame[:, :, 0] * blue, 0, 255)
        filtered[:, :, 1] = np.clip(frame[:, :, 1] * green, 0, 255)
        filtered[:, :, 2] = np.clip(frame[:, :, 2] * red, 0, 255)

    cv2.imshow("Color Filter", filtered)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    elif key == ord("1"):
        filter_type = "normal"

    elif key == ord("2"):
        filter_type = "gray"

    elif key == ord("3"):
        filter_type = "warm"

    elif key == ord("4"):
        filter_type = "cool"

    elif key == ord("s"):
        filename = datetime.now().strftime("filtered_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, filtered)
        print("Image saved:", filename)

camera.release()
cv2.destroyAllWindows()
