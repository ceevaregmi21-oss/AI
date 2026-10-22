
import cv2
from deepface import DeepFace

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

emotion = "Detecting..."
frame_count = 0

while True:
    success, frame = camera.read()

    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    frame_count += 1

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]

        if frame_count % 10 == 0:
            try:
                result = DeepFace.analyze(
                    face,
                    actions=["emotion"],
                    detector_backend="skip",
                    enforce_detection=False
                )
                emotion = result[0]["dominant_emotion"]
            except Exception:
                emotion = "Unknown"

        cv2.rectangle(
            frame, (x, y), (x+w, y+h), (0, 255, 0), 2
        )

        cv2.putText(
            frame,
            emotion,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face and Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
