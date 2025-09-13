
import numpy as np
import cv2 as cv


class Video():
    
    def __init__(self, window = False):
        self.capture = cv.VideoCapture(0)
        self.window = window


    def capture_frame(self, callback = None):
        if not self.capture.isOpened():
            print("The camara is not open")
            return
        
        while True:
            ret, frame = self.capture.read()

            if not ret:
                print("Can't receive the frame")
                break

            frame = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

            if(self.window):
                cv.imshow('frame', frame)
                if cv.waitKey(1) == ord('q'):
                    break
        
        self.capture.release()
        if(self.window):
            cv.destroyAllWindows()

    
