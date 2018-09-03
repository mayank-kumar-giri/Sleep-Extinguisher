# Sleep-Extinguisher
An application that alarms the vehicle driver whenever he/she sleeps while driving.

## Working
Using OpenCV (cv2) library of Python, we process each image through HaarCascades to detect blinks. We keep counting number of frames that have blinks and raise alarm when it crosses a pre-defined threshold. The alarm goes off as soon as the person wakes up, i.e., opens his eyes.

## Using
I plan to develop this into an Android application for real use.

To see the working of the code, it can be run on any standard Python IDE like PyCharm. The system must have the following Python libraries installed to be able to run it:
<ol>
  <li>kivy (Python library for developing mobile apps) (https://kivy.org/doc/stable/)</li>
  <li>cv2 (OpenCV library) (https://docs.scipy.org/doc/)</li>
</ol>
