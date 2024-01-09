import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def count_open_fingers(hand_landmarks):
    # Define the finger landmark indices
    finger_indices = [4, 8, 12, 16, 20]

    # Check each finger if it is open
    open_fingers = 0
    for finger_index in finger_indices:
        # Check if the finger tip is above the middle landmark of the same finger
        if hand_landmarks[finger_index].y < hand_landmarks[finger_index - 2].y:
            open_fingers += 1

    return open_fingers

def hand_process(frame):

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Initialize open_fingers before the if statement
    open_fingers = 0

    # If hands are detected, mark them on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count and display the number of open fingers
            open_fingers = count_open_fingers(hand_landmarks.landmark)
    return frame, int(open_fingers)
