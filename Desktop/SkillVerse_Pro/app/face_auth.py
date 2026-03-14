import cv2
import os


def capture_face(email):

    if not os.path.exists("faces"):
        os.makedirs("faces")

    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            face = frame[y:y+h, x:x+w]

            cv2.imwrite(f"faces/{email}.jpg", face)

            cap.release()
            cv2.destroyAllWindows()

            return True

        cv2.imshow("Capture Face - Press ESC", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return False


def verify_face(email):

    path = f"faces/{email}.jpg"

    if not os.path.exists(path):
        return False

    cap = cv2.VideoCapture(0)

    saved = cv2.imread(path)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        resized = cv2.resize(frame, (saved.shape[1], saved.shape[0]))

        diff = cv2.absdiff(saved, resized)

        score = diff.mean()

        if score < 40:
            cap.release()
            cv2.destroyAllWindows()
            return True

        cv2.imshow("Face Login - Press ESC", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return False