
import cv2
import numpy as np


def apply_filter(image, ftype):
    img = image.copy()

    if ftype == "red_tint":
        img[:, :, 0] = 0
        img[:, :, 1] = 0

    elif ftype == "green_tint":
        img[:, :, 0] = 0
        img[:, :, 2] = 0

    elif ftype == "blue_tint":
        img[:, :, 1] = 0
        img[:, :, 2] = 0

    elif ftype == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sob = cv2.convertScaleAbs(cv2.bitwise_or(
            cv2.convertScaleAbs(sx),
            cv2.convertScaleAbs(sy)
        ))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)

    elif ftype == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)

    elif ftype == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, 9, 9
        )
        color = cv2.bilateralFilter(image, 9, 300, 300)
        img = cv2.bitwise_and(color, color, mask=edges)

    return img


def main():
    # Use DirectShow instead of MSMF on Windows
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Set webcam resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    ftype = "original"

    print("r=Red, g=Green, b=Blue")
    print("s=Sobel, c=Canny, t=Cartoon")
    print("o=Original, q=Quit")

    while True:
        ret, frame = cap.read()

        if not ret or frame is None:
            print("Can't Receive Frame. Retrying...")
            cv2.waitKey(100)
            continue

        out = apply_filter(frame, ftype)
        cv2.imshow("Filter", out)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            ftype = "red_tint"
        elif key == ord('g'):
            ftype = "green_tint"
        elif key == ord('b'):
            ftype = "blue_tint"
        elif key == ord('s'):
            ftype = "sobel"
        elif key == ord('c'):
            ftype = "canny"
        elif key == ord('t'):
            ftype = "cartoon"
        elif key == ord('o'):
            ftype = "original"
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


