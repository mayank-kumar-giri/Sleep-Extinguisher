__author__ = 'Mayank Kumar Giri'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2
import numpy as np

from kivy.core.audio import SoundLoader


class sleep_extinguisher(App):

    def build(self):
        self.img1 = Image(source='a.jpg')
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #opencv2 stuffs
        # self.capture = cv2.VideoCapture(0)
        # ret, frame = self.capture.read()
        # cv2.namedWindow("CV2 Image")
        # cv2.imshow("CV2 Image", frame)

        k = 1
        blink_frame_count = 0

        face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')  # Replace this with the path where you reside the file
        eye_cascade = cv2.CascadeClassifier(
            'haarcascade_eye.xml')  # Replace this with the path where you reside the file
        self.capture = cv2.VideoCapture(0)
        # Change these parameters to play with sensitivity
        c1 = 7
        c2 = 5
        defaultflag = 0
        tflag = 0

        while (True):
            if defaultflag==1:
                sound = SoundLoader.load('fa.wav')
                sound.seek(0)
                sound.play()
            if blink_frame_count < 5:
                print("All fine!Have a safe driving!!", blink_frame_count, "\n")
                defaultflag = 0
                tflag=0

            else:
                print("WAKE UP, YOU'RE DRIVING!!!", blink_frame_count, "\n")


            ret, img = self.capture.read()
            img = cv2.flip(img, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                k = 1
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # u1 = x + w
                # u2 = y + h
                cir = cv2.circle(img, (int(int(x) + int(w) / 2), int(int(y) + int(h) / 2)), 1, (0, 255, 255), 2)

                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
                for (ex, ey, ew, eh) in eyes:
                    k = 0
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)

            if k == 1:
                blink_frame_count = blink_frame_count + 1
                if blink_frame_count>5:
                    defaultflag = 1

            if k == 0:
                if blink_frame_count > 0:
                    blink_frame_count = blink_frame_count - 1
                    tflag = tflag + 1
                    if tflag > 5:
                        defaultflag = 0
                else:
                    blink_frame_count = 0

            cv2.namedWindow("img", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("img", 600, 450)
            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        #self.capture.release()
        #cv2.destroyAllWindows()

        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

if __name__ == '__main__':
    sleep_extinguisher().run()
