import cv2
import os

def register_face(email):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    os.makedirs("static/faces", exist_ok=True)
    cv2.imwrite(f"static/faces/{email}.jpg", frame)

def verify_face(email):
    saved_image = cv2.imread(f"static/faces/{email}.jpg")

    cap = cv2.VideoCapture(0)
    ret, current_frame = cap.read()
    cap.release()

    # Simple comparison using pixel difference
    difference = cv2.absdiff(saved_image, current_frame)
    score = difference.sum()

    if score < 5000000:
        return True
    else:
        return False