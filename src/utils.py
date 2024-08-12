import cv2
import os

def load_cascade(cascade_path):
    cascade = cv2.CascadeClassifier(cascade_path)
    if cascade.empty():
        print(f"Error: Failed to load cascade from {cascade_path}")
        return None
    return cascade

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def save_image(save_path, count, image):
    file_path = os.path.join(save_path, f"{count}.jpg")
    cv2.imwrite(file_path, image)
    print(f"Image saved at {file_path}")
