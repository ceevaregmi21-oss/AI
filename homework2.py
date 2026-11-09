
import cv2
import numpy as np

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Set webcam resolution
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not camera.isOpened():
    print("Error: Camera not found!")
    exit()

canvas = None
previous_x, previous_y = 0, 0
circle_x, circle_y = 320, 240

lower_color = np.array([35, 40, 40])
upper_color = np.array([85, 255, 255])

while True:
    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    gesture = "No Hand Detected"

    if len(contours) > 0:

        hand_contour = max(contours, key=cv2.contourArea)

        area = cv2.contourArea(hand_contour)

        if area > 2000:

            x, y, w, h = cv2.boundingRect(hand_contour)

            moments = cv2.moments(hand_contour)

            if moments["m00"] != 0:

                cx = int(moments["m10"] / moments["m00"])
                cy = int(moments["m01"] / moments["m00"])

                hull = cv2.convexHull(
                    hand_contour,
                    returnPoints=False
                )

                finger_count = 0

                if hull is not None and len(hull) > 3:

                    defects = cv2.convexityDefects(
                        hand_contour,
                        hull
                    )

                    if defects is not None:

                        for i in range(defects.shape[0]):

                            s, e, f, d = defects[i, 0]

                            start = tuple(hand_contour[s][0])
                            end = tuple(hand_contour[e][0])
                            far = tuple(hand_contour[f][0])

                            a = np.linalg.norm(
                                np.array(end) - np.array(start)
                            )

                            b = np.linalg.norm(
                                np.array(far) - np.array(start)
                            )

                            c = np.linalg.norm(
                                np.array(end) - np.array(far)
                            )

                            if b * c != 0:

                                angle = np.degrees(
                                    np.arccos(
                                        np.clip(
                                            (b*b + c*c - a*a) / (2*b*c),
                                            -1.0,
                                            1.0
                                        )
                                    )
                                )

                                if angle < 90 and d > 10000:
                                    finger_count += 1

                if finger_count >= 2:

                    gesture = "Open Hand - Drawing"

                    if previous_x != 0 and previous_y != 0:

                        cv2.line(
                            canvas,
                            (previous_x, previous_y),
                            (cx, cy),
                            (0, 255, 0),
                            5
                        )

                    previous_x, previous_y = cx, cy

                else:

                    gesture = "Closed Hand - Moving Circle"

                    circle_x = cx
                    circle_y = cy

                    previous_x, previous_y = 0, 0

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x+w, y+h),
                    (0, 255, 0),
                    2
                )

                cv2.circle(
                    frame,
                    (cx, cy),
                    7,
                    (0, 0, 255),
                    -1
                )

                cv2.putText(
                    frame,
                    "Fingers: " + str(finger_count),
                    (x, y-15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2
                )

            else:
                previous_x, previous_y = 0, 0

        else:
            previous_x, previous_y = 0, 0

    else:
        previous_x, previous_y = 0, 0

    cv2.circle(
        frame,
        (circle_x, circle_y),
        30,
        (255, 0, 0),
        -1
    )

    combined = cv2.add(frame, canvas)

    cv2.putText(
        combined,
        "Gesture: " + gesture,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        combined,
        "Open Hand: Draw | Closed Hand: Move Circle",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        combined,
        "Press C to Clear | Q to Quit",
        (20, 115),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow("Hand Gesture Interaction System", combined)
    cv2.imshow("Color Detection Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        canvas = np.zeros_like(frame)

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
