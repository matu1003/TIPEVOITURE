import cv2
import time

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    
    def get_img(self):
        success, img = self.cap.read()
        return img

cam = Camera()
img = cam.get_img()
cv2.imshow("Image", img)
cv2.waitKey()


