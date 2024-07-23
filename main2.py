import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # For Red COLOR
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    # For Blue COLOR
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    
    # For Green COLOR
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    
    # For Black COLOR
    low_black = np.array([0, 0, 0])
    high_black = np.array([180, 255, 30])
    black_mask = cv2.inRange(hsv_frame, low_black, high_black)
    black = cv2.bitwise_and(frame, frame, mask=black_mask)
    
    # Combine all the masks
    combined_mask = red_mask | blue_mask | green_mask | black_mask
    result = cv2.bitwise_and(frame, frame, mask=combined_mask)
    
    # Display the result
    cv2.imshow("Result", result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
