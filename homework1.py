
import cv2
from deepface import DeepFace

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not camera.isOpened():
    print("Error: Camera not found!")
    exit()

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

frame_count = 0
analyze_interval = 10
emotions = []

while True:
    success, frame = camera.read()

    if not success:
        print("Error: Unable to read camera frame")
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.equalizeHist(gray)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(40, 40)
    )

    frame_count += 1

    if len(emotions) != len(faces):
        emotions = ["Detecting..."] * len(faces)

    for i, (x, y, w, h) in enumerate(faces):

        face = frame[y:y+h, x:x+w]

        if frame_count % analyze_interval == 0:
            try:
                result = DeepFace.analyze(
                    face,
                    actions=["emotion"],
                    detector_backend="skip",
                    enforce_detection=False,
                    silent=True
                )

                if isinstance(result, list):
                    emotions[i] = result[0]["dominant_emotion"]
                else:
                    emotions[i] = result["dominant_emotion"]

            except Exception:
                emotions[i] = "Unknown"

        emotion = emotions[i]

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        label = emotion.upper()

        cv2.rectangle(
            frame,
            (x, y-35),
            (x+w, y),
            (0, 255, 0),
            -1
        )

        cv2.putText(
            frame,
            label,
            (x+5, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 0),
            2
        )

    cv2.putText(
        frame,
        "Faces Detected: " + str(len(faces)),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Press Q to Exit",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow("Face and Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
