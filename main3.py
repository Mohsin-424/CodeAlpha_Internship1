import cv2
import numpy as np

# Define color ranges and names
colors = [
    {"name": "Red", "low": np.array([161, 155, 84]), "high": np.array([179, 255, 255])},
    {"name": "Blue", "low": np.array([94, 80, 20]), "high": np.array([126, 255, 255])},
    {"name": "Green", "low": np.array([25, 52, 72]), "high": np.array([102, 255, 255])},
    {"name": "Yellow", "low": np.array([20, 100, 100]), "high": np.array([30, 255, 255])},
    {"name": "Black", "low": np.array([0, 0, 0]), "high": np.array([180, 255, 30])},
    {"name": "White", "low": np.array([0, 0, 231]), "high": np.array([180, 18, 255])}
]

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    color_detected = None
    for color in colors:
        mask = cv2.inRange(hsv_frame, color["low"], color["high"])
        if np.any(mask):
            color_detected = color["name"]
            break
    
    if color_detected:
        print(f"Detected color: {color_detected}")
        cv2.putText(frame, color_detected, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

