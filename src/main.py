import cv2
import os
from utils import load_cascade, create_directory, save_image

def detect_number_plate():
    cascade_path = "haarcascades/haarcascade_russian_plate_number.xml"
    plate_cascade = load_cascade(cascade_path)
    if plate_cascade is None:
        print("Error: Cascade classifier not loaded.")
        return

    min_area = 500
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not accessible.")
        return

    count = 0
    save_path = "../data/saved_images/"
    create_directory(save_path)

    while True:
        success, img = cap.read()
        if not success:
            print("Error: Failed to capture image.")
            break

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        number_plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
        img_roi = None

        for (x, y, w, h) in number_plates:
            area = w * h
            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, "NUMBER PLATE", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                img_roi = img[y:y + h, x:x + w]
                cv2.imshow("ROI", img_roi)

        cv2.imshow("RESULT", img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            if img_roi is not None:
                save_image(save_path, count, img_roi)
                count += 1
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_number_plate()
