import mediapipe as mp
import numpy as np
import screen_brightness_control as sbc
import cv2

Hands = mp.solutions.hands
hands = Hands.Hands()
draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Set webcam resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ok, img = cap.read()
    if not ok:
        break

    img = cv2.flip(img, 1)
    h, w = img.shape[:2]
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        for hand in res.multi_hand_landmarks:
            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)
            lm = hand.landmark

            x1, y1 = int(lm[4].x * w), int(lm[4].y * h)
            x2, y2 = int(lm[8].x * w), int(lm[8].y * h)

            dist = np.hypot(x2 - x1, y2 - y1)
            brightness = int(np.interp(dist, [30, 300], [0, 100]))

            sbc.set_brightness(brightness)

            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(img, f"Brightness: {brightness}%",(20, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 2)

    cv2.imshow("Brightness Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()