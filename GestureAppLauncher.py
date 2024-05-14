import cv2
from cvzone.HandTrackingModule import HandDetector
import os

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize the HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # Read a frame from the webcam
    status, photo = cap.read()

    if not status:
        print("Failed to capture image")
        continue

    # Detect hands
    hands, photo = detector.findHands(photo)
    
    if hands:
        my_lmlist = hands[0]
        finger_up_list = detector.fingersUp(my_lmlist)

        # Check for specific gestures
        if finger_up_list == [0, 1, 1, 0, 0]:
            os.system("notepad")
        elif finger_up_list == [1, 1, 1, 1, 1]:
            os.system("start chrome")
        else:
            print("idk")

    # Display the image
    cv2.imshow("My photo", photo)
    
    # Break the loop if 'Enter' key is pressed
    if cv2.waitKey(100) == 13:
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
