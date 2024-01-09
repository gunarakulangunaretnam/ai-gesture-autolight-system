import cv2
import modules.finger_detection as FingerDetection
from pyfirmata import Arduino, util

board = Arduino('COM4') # Change 'COM4' to your Arduino's serial port

red_pin = board.get_pin('d:13:o')     # Digital output pin 13
green_pin = board.get_pin('d:12:o')   # Digital output pin 12
blue_pin = board.get_pin('d:11:o')    # Digital output pin 11

cap = cv2.VideoCapture(0)  # Use 0 for the default camera

while True:
    # Initialize OpenCV

    ret, frame = cap.read()

    frame, num = FingerDetection.hand_process(frame)

    if num == 2:
        red_pin.write(1)
        green_pin.write(0)
        blue_pin.write(0)
    elif num == 3:
        red_pin.write(1)
        green_pin.write(1)
        blue_pin.write(0) 
    elif num == 4:
        red_pin.write(1)
        green_pin.write(1)
        blue_pin.write(1)
    else:
        red_pin.write(0)
        green_pin.write(0)
        blue_pin.write(0)


    # Display the frame
    cv2.imshow('Display', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all windows
cap.release()
cv2.destroyAllWindows()
