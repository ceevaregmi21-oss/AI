import cv2
import mediapipe as mp

hands = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

i = 0
filters = ['Sepia', 'Blur', 'Negative', 'Edge']
while True:
    ret,cam = cap.read()
    if not ret:
        break
    else:
        cam = cv2.flip(cam, 1)
        result = hands.process(cv2.cvtColor(cam, cv2.COLOR_BGR2RGB))

        if(result.multi_hand_landmarks):
            hand = result.multi_hand_landmarks[0]
            mp.solutions.drawing_utils.draw_landmarks(cam, hand, mp.solutions.hands.HAND_CONNECTIONS)

            t,p = hand.landmark[4], hand.landmark[8]
            if (abs(t.x-p.x) < 0.03 and abs(t.y-p.y) < 0.03):
                cv2.imwrite('image.jpg', cam)

        if(filters[i] == 'Negative'):
            cam = cv2.bitwise_not(cam)

        elif(filters[i] == 'Blur'):
            cam = cv2.GaussianBlur(cam, (15, 15), 0)

        elif(filters[i] == 'Edge'):
            cam = cv2.Canny(cam, 40, 60)

        else:

            cam = cv2.applyColorMap(cam, cv2.COLORMAP_BONE)
        cv2.imshow('image', cam)

        key = cv2.waitKey(1) & 0xFF

        if(key == ord('f')):
            i = (i+1)%4
        elif(key == ord('q')):
            break

cv2.destroyAllWindows()
cap.release()
hands.close()


           